import requests, os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("IBM_API_KEY")

def get_access_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"apikey": API_KEY, "grant_type": "urn:ibm:params:oauth:grant-type:apikey"}
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]
