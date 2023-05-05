# Get user information
# GET https://cloud.leonardo.ai/api/rest/v1/me
# This endpoint will return your user information, including your user ID.

import requests

url = "https://cloud.leonardo.ai/api/rest/v1/me"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
