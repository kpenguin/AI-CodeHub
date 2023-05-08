## Get generations by user ID
## GET https://cloud.leonardo.ai/api/rest/v1/generations/user/{userId}
## This endpoint returns all generations by a specific user

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

userId = myprivate['LEONARDOAI']['userId']
offset = '0'
limit = '1'
url = "https://cloud.leonardo.ai/api/rest/v1/generations/user/" + userId + "?offset=" + offset + "&limit=" + limit


headers = {
    "accept": "application/json",
    "authorization": myprivate['LEONARDOAI']['APIKey']
}

response = requests.get(url, headers=headers)

print(response.text)

with open("studentWithoutPrettyPrint.json", "w") as write_file:
    json.dump(student, write_file)
print("Done writing JSON data into file without Pretty Printing it")


with open("studentWithPrettyPrint2.json", "w") as write_file:
    json.dump(student, write_file, indent=0)
print("Done writing PrettyPrinted JSON data into file with indent=0")

with open("studentWithPrettyPrint3.json", "w") as write_file:
    json.dump(student, write_file, indent=4, sort_keys=True)
print("Done writing Sorted and PrettyPrinted JSON data into file")

import pandas as pd
d = pd.read_json(response.text)
df = pd.json_normalize(d)
print(df)
# df.to_csv('gen_by_userid.csv', encoding='utf-8', index=False)
