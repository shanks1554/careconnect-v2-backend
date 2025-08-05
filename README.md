# CareConnect v2 – Backend

This is the backend of the **CareConnect v2** project – an AI-powered mental health assistant built using IBM Watsonx, LangGraph, and FastAPI.

## 🌐 Overview

The backend serves as the brain of CareConnect. It dynamically routes user messages through a network of intelligent agents using LangGraph and IBM's Granite model via Watsonx.

## 🧠 Key Features

- Dynamic agent-based reasoning using LangGraph

- IBM Watsonx Granite model for all AI responses

- Modular agent structure (affirmation, sentiment, suggestion, etc.)

- JSON API endpoint (`/chat`) for frontend communication

- Fully stateless and cold-start optimized

## 🚀 Technologies Used

- FastAPI

- LangGraph

- IBM Watsonx (Granite model)

- Python 3.12

- Render (for deployment)

## 📁 Folder Structure
```bash
careconnect-v2-backend/
├── agents/ # All LLM-based agents
├── helpers/ # Watsonx auth + generation
├── main.py # FastAPI app
├── .env # Environment variables (not included in repo)
├── requirements.txt
├── .gitignore
├── test.ipynb
└── README.md
```

## ⚙️ Setup Instructions

### 1. Clone the repo:

```bash
git clone https://github.com/shanks1554/careconnect-v2-backend.git
cd careconnect-v2-backend
```

### 2. Install Dependencies:

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file with:

```bash
WATSONX_API_KEY = your_watsonx_api_key
WATSONX_PROJECT_ID = your_watsonx_project_id
WATSONX_REGION = your_watsonx_region
WATSONX_MODEL_ID = your_watsonx_model_id
WATSONX_BASE_URL = your_watsonx_base_url
```

### 4. Run the app:

```bash
uvicorn main:app --reload
```

## 🔗 API Endpoint

- POST /chat

    Accepts a JSON payload:
    
    ```bash
    {
    "message": "Hello"
    }
    ```

- Returns:
    
    ```bash
    {
        "agent": "greeting_agent",
        "response": "Hi there! How can I support you today?"
    }
    ```

## 🌍 Deployment
Deployed on ```Render``` with automatic cold-start handling.