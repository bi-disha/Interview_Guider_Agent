from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("IBM_API_KEY")
API_URL = os.getenv("IBM_API_URL")

app = Flask(__name__)
CORS(app)

@app.route('/api/interview_trainer', methods=['POST'])
def handle_request():
    """
    Handles POST requests from the front-end to get a response from IBM Cloud agent.
    """
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({"error": "No prompt provided"}), 400

        user_prompt = data['prompt']

        # If API key or URL not provided, return demo response
        if not API_KEY or not API_URL:
            if "python" in user_prompt.lower():
                agent_response = "Great! Let's discuss Python. What is a decorator and how is it used?"
            elif "java" in user_prompt.lower():
                agent_response = "Java is a fantastic choice. Let's start with a question about OOP. Can you explain the four pillars of OOP?"
            else:
                agent_response = f"Demo response for: '{user_prompt}'"
            return jsonify({"response": agent_response})

        # Actual IBM Cloud call (only works if API key & URL provided in .env)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        payload = {"input": {"text": user_prompt}}
        ibm_response = requests.post(API_URL, json=payload, headers=headers)

        result = ibm_response.json()
        agent_response = result.get("output", {}).get("generic", [{}])[0].get("text", "No response from IBM Agent")

        return jsonify({"response": agent_response})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
