# Web scraping from the website INVESTIDOR10.

from bs4 import BeautifulSoup
from botocore.exceptions import ClientError

import boto3
import pandas as pd
import requests

import datetime
import json, os


DATA_PATH = "."
BASE_URL = "https://investidor10.com.br/acoes"
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")


def get_codes_list() -> list:
    """
    Used to load the codes for scraping.
    """

    filtered_output = []

    # with open(f"{DATA_PATH}/codes.txt", "r") as code_file:
    #     code_list = code_file.readlines()
    
    # for code in code_list:
    #     filtered_output.append(code.replace('\n', '').lower())

    index_reference = os.getenv("INDEX_LIST")
    filtered_output = index_reference.split(";")
    
    return filtered_output


def get_metrics_from_code(code: str) -> dict:
    """
    Get the main metrics for a specific code via web scraping.
    """

    print(f"Starting scrape for {code}")

    headers = {
        'User-Agent': 'Chrome/125.0.0.0 Safari/537.36',
        'Connection': 'keep-alive',
    }

    session = requests.Session()

    page = session.get(f"{BASE_URL}/{code}", headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    date = datetime.datetime.now().isoformat()
    metrics = {}

    name = soup.find('h2', class_="name-company").text
    price = soup.find('div', class_="_card cotacao").find('div', class_="_card-body").find('span').text
    pl = soup.find('div', class_="_card pl").find('div', class_="_card-body").find('span').text
    pvp = soup.find('div', class_="_card vp").find('div', class_="_card-body").find('span').text
    dy = soup.find('div', class_="_card dy").find('div', class_="_card-body").find('span').text

    for indicators_table in soup.find('div', id="indicators").find_all(class_="cell"):
        target = indicators_table.find("span").text
        if "ROE" in target:
            roe = indicators_table.find("div").find("span").text.replace(' ', '').replace('\n', '')
        elif "MARGEM LÍQUIDA" in target:
            margem_liquida = indicators_table.find("div").find("span").text.replace(' ', '').replace('\n', '')

    metrics["code"] = code
    metrics["name"] = name
    metrics["price"] = price
    metrics["P/L"] = pl
    metrics["P/VP"] = pvp
    metrics["DY (ano)"] = dy
    metrics["ROE"] = roe
    metrics["margem liquida"] = margem_liquida
    metrics["date"] = date

    return metrics


def save_result_in_json(metrics_list: list):
    """
    Used to save the scraped metrics for each code in a json file.
    """

    with open('metrics.json', 'w', encoding='utf-8') as f:
        json.dump(metrics_list, f, ensure_ascii=False, indent=4)


def convert_json_to_csv(input_file_path: str, output_file_path: str):
    json_file = pd.read_json(input_file_path)
    json_file.to_csv(output_file_path, index=False)


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client(
        's3',
        endpoint_url=f'http://{MINIO_ENDPOINT}',
        region_name='us-east-1' 
    )

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print(e)
        return False
    return True

def main():
    all_results_list = []
    codes_list = get_codes_list()

    for code in codes_list:
        metrics = get_metrics_from_code(code)
        all_results_list.append(metrics)

    save_result_in_json(all_results_list)

    convert_json_to_csv(
        input_file_path = f"{DATA_PATH}/metrics.json",
        output_file_path = f"{DATA_PATH}/metrics.csv"
    )

    upload_file(file_name=f"{DATA_PATH}/metrics.csv", bucket="app", object_name="metrics.csv")
    upload_file(file_name=f"{DATA_PATH}/metrics.json", bucket="app", object_name="metrics.json")


if __name__ == "__main__":
    main()
