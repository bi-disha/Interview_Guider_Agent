import os
import requests
from dotenv import load_dotenv
from backend.ibm_auth import get_access_token  # should return IAM token

load_dotenv()
AGENT_URL = os.getenv("IBM_AGENT_URL")  # e.g., https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/<deployment_id>/ai_service_stream?version=2021-05-01

def call_ibm_api(prompt: str, access_token: str):
    """
    Sends a prompt to the IBM ML deployment and returns the generated response.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Correct payload structure based on IBM's messages format
    payload = {
        "messages": [
            {"content": prompt, "role": "user"}
        ]
    }

    try:
        response = requests.post(AGENT_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise error if HTTP status is 4xx/5xx

        result = response.json()
        # Parse the response — IBM usually returns messages array
        try:
            return result["messages"][-1]["content"]
        except (KeyError, IndexError, TypeError):
            return result  # fallback: return raw response

    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {str(e)}", "details": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

def ask_agent(prompt: str):
    """
    Helper to get IAM token and call IBM API
    """
    access_token = get_access_token()  # Must return IAM token
    return call_ibm_api(prompt, access_token)
