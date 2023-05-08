## Get user information
## GET https://cloud.leonardo.ai/api/rest/v1/me
## This endpoint will return your user information, including your user ID.

###############################################################################

## Get program path and name
from pathlib import Path
myfile = Path(__file__).stem

## Read in configuration file
import yaml

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

myPrivateConfig = "../myprivate.config"
myprivate = read_yaml(myPrivateConfig)


## Validation configuration file
import pytest

def test_validation_yaml():
    with pytest.raises(FileNotFoundError):
        read_yaml(file_path=myPrivateConfig)

    with pytest.raises(yaml.scanner.ScannerError):
        # only show the first error
        read_yaml(file_path=myPrivateConfig)

    with pytest.raises(yaml.parser.ParserError):
        # only show the first error
        read_yaml(file_path=myPrivateConfig)

###############################################################################

## Main
import requests

url = "https://cloud.leonardo.ai/api/rest/v1/me"

headers = {
    "accept": "application/json",
    "authorization": myprivate['LEONARDOAI']['APIKey']
}

response = requests.get(url, headers=headers)
print(response.text)

import json
mydata = response.text

with open(myfile + "-raw.json", "w") as write_file:
    json.dump(mydata, write_file)

with open(myfile + "-pretty.json", "w") as write_file:
    json.dump(mydata, write_file, indent=4)

with open(myfile + "-sorted.json", "w") as write_file:
    json.dump(mydata, write_file, indent=4, sort_keys=True)
