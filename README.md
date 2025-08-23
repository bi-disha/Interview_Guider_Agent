Interview Trainer Agent 🎯

An AI-powered Interview Trainer Agent built with Flask (Python backend) and a modern chat UI (HTML + TailwindCSS frontend).
This project was developed as part of the IBM Cloud Agentic AI Project.

🚀 Features

🧑‍💻 Interactive chat interface to simulate interview practice.

🔄 Backend API (Flask) that connects to IBM Cloud Agent service.

🌍 CORS enabled so frontend and backend work together seamlessly.

🔒 Environment variables (.env) for API keys (secure, not hardcoded).

🛠️ Demo mode if no IBM Cloud API key is provided (uses sample interview Q&A).

📂 Project Structure
IBM-Interview-Trainer-Agent/
│
├── app.py              # Flask backend
├── index.html          # Chat UI (frontend)
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (NOT committed to GitHub)
└── .gitignore          # Ignore .env and cache files

⚙️ Installation & Setup

Clone this repository

git clone https://github.com/your-username/IBM-Interview-Trainer-Agent.git
cd IBM-Interview-Trainer-Agent


Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)


Install dependencies

pip install -r requirements.txt


Set up environment variables
Create a .env file in the project root:

IBM_API_KEY=YOUR_IBM_CLOUD_API_KEY_HERE
IBM_API_URL=YOUR_IBM_CLOUD_ASSISTANT_ENDPOINT_HERE


Run the backend server

python app.py


The server will start at http://127.0.0.1:5000
.

Run the frontend

Option 1: Open index.html directly in your browser.

Option 2 (recommended): Start a simple HTTP server:

python -m http.server 8000


Open: http://127.0.0.1:8000/index.html

🖼️ Screenshots

Add your screenshots here (taken from your IBM Cloud preview page).
Example:




📌 Notes

If .env is not configured, the backend runs in demo mode with sample responses.

If .env is properly configured with IBM Cloud credentials, the backend will connect to the real IBM Watson Assistant / Agent service.

🛡️ Security

Never commit your .env file with real API keys to GitHub.

.gitignore already ensures .env is not pushed.

🧑‍💻 Author

Your Name
Project developed for IBM SkillsBuild Agentic AI Project