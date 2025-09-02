# IBM AI Agent

A local chatbot application built with **FastAPI** and a **HTML frontend**, powered by **IBM Watsonx.ai**.

---

## Features

- FastAPI backend serving the IBM AI agent
- Interactive frontend at `/home` with a modern chat interface
- Scrollable chat window for long responses
- POST `/api/generate` endpoint for sending prompts
- Works locally at `http://localhost:8000`

---

## Project Structure


IBM AI AGENT PROJECT/

├── backend/

│ ├── main.py # FastAPI server

│ ├── ibm_client.py # API call functions

│ └── ibm_auth.py # IBM authentication functions

├── index.html # Chatbot frontend

├── venv/ # Python virtual environment (ignored in Git)

└── .env # Environment variables (API keys, ignored)



## Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- Requests
- python-dotenv

Install dependencies:


pip install -r requirements.txt


Setup


Clone the repository


git clone https:https://github.com/bi-disha/Interview_Guider_Agent.git


cd IBM-AI-Agent


Create .env file in project root and add your IBM credentials:

## env

IBM_API_KEY=<your_ibm_api_key>



IBM_AGENT_URL=<your_ibm_agent_url>



Activate virtual environment


# Windows PowerShell
source venv/Scripts/activate

# Or Linux/Mac
source venv/bin/activate
Run the FastAPI server


python -m backend.main
Usage
Open the chatbot frontend in your browser:


http://localhost:8000/home



Type your message and click Send to communicate with the IBM AI agent.

## For API testing (Swagger UI):


http://localhost:8000/docs



## Notes


Do not commit .env or venv/ to GitHub — these contain secrets and environment-specific files.




Ensure your IBM credentials are valid and have access to the deployed Watsonx.ai model.

## License
MIT License

