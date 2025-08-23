from flask import Flask, request, jsonify
from flask_cors import CORS

# This is a placeholder for your IBM Cloud API key.
# It is better practice to use environment variables for this.
API_KEY = "YOUR_IBM_CLOUD_API_KEY_HERE"

app = Flask(__name__)
# Enable CORS to allow the front-end (running locally on your machine)
# to make requests to this back-end.
CORS(app)

# This is your main API endpoint.
@app.route('/api/interview_trainer', methods=['POST'])
def handle_request():
    """
    Handles POST requests from the front-end to get a response from the agent.
    """
    try:
        # Get the JSON data from the request body
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({"error": "No prompt provided"}), 400

        user_prompt = data['prompt']
        
        # -----------------------------------------------------------------
        # IMPORTANT: This is the section you need to replace!
        # This is where you will integrate with your IBM Cloud agent.
        # You will use the API_KEY defined above to make a secure call.
        #
        # For example, you would use the 'requests' library:
        # import requests
        #
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Authorization': f'Bearer {API_KEY}'
        # }
        # payload = { 'text': user_prompt }
        # ibm_response = requests.post('YOUR_IBM_CLOUD_API_URL', json=payload, headers=headers)
        # agent_response = ibm_response.json().get('some_key')
        # -----------------------------------------------------------------

        # Placeholder logic for demonstration
        if "python" in user_prompt.lower():
            agent_response = "Great! Let's discuss Python. What is a decorator and how is it used?"
        elif "java" in user_prompt.lower():
            agent_response = "Java is a fantastic choice. Let's start with a question about object-oriented programming. Can you explain the four pillars of OOP?"
        else:
            agent_response = f"Thank you for the prompt: '{user_prompt}'. I'm ready to continue. What's your first question for me?"

        # Return the response as JSON
        return jsonify({"response": agent_response})
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # You can change the port if needed. debug=True allows for auto-reloading.
    app.run(debug=True, port=5000)
