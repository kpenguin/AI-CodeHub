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
# print(myprivate)
# print(myprivate['LEONARDOAI'])
# print(myprivate['LEONARDOAI']['APIKey'])


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


## Get Leonardo.AI Generations
import requests

def get_user_information():
    url = "https://cloud.leonardo.ai/api/rest/v1/me"

    headers = {
        "accept": "application/json",
        "authorization": myprivate['LEONARDOAI']['APIKey']
    }

    response = requests.get(url, headers=headers)
    ##Type: <class 'requests.models.Response'>

    status_code = response.status_code
    status_ok = response.ok

    print(f'The status code is {status_code}.')
    print(f'The response is {status_ok}.')

    if response.status_code > 400:
        print("Response isn't ok!")

    else:
        print('Response is ok!')
        response_dict = response.json()
        ##Type: <class 'dict'>

        with open("raw.json", "w") as write_file:
            json.dump(response_dict, write_file)

        with open(myfile + "-raw.json", "w") as write_file:
            json.dump(response_dict, write_file)

        with open(myfile + "-pretty.json", "w") as write_file:
            json.dump(response_dict, write_file, indent=4)

        with open(myfile + "-sorted.json", "w") as write_file:
            json.dump(response_dict, write_file, indent=4, sort_keys=True)

        return response_dict

import json

def read_file(file_name):
    with open(file_name) as f:
        mydataf = json.load(f)
    print("Done reading data from a file")
    #print (type(mydataf))
    ##Type: <class 'dict'>
    return mydataf

###############################################################################


## Main
mydata = get_user_information()
