## Get user information
## GET https://cloud.leonardo.ai/api/rest/v1/me
## This endpoint will return your user information, including your user ID.

## Read in configuration file
import yaml

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)
    
myprivate = read_yaml("myprivate.config")
# print(myprivate)
# print(myprivate['LEONARDOAI'])
# print(myprivate['LEONARDOAI']['APIKey'])

## Validation configuration file
import pytest

def test_validation_yaml():
    with pytest.raises(FileNotFoundError):
        read_yaml(file_path="source/data/non_existing_file.yaml")

    with pytest.raises(yaml.scanner.ScannerError):
        # only show the first error
        read_yaml(file_path="source/data/sample_invalid.yaml")

    with pytest.raises(yaml.parser.ParserError):
        # only show the first error
        read_yaml(file_path="source/data/sample_invalid.json")


## Main
import requests

url = "https://cloud.leonardo.ai/api/rest/v1/me"

headers = {
    "accept": "application/json",
    "authorization": myprivate['LEONARDOAI']['APIKey']
}

response = requests.get(url, headers=headers)

print(response.text)
