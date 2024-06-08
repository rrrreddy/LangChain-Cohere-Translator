# LangChain-Cohere-Translator

## LangChain Cohere Translator

A GenAI application that uses LangChain and Cohere to translate text. The application also integrates with LangSmith for tracking requests and responses.

## Features

- Translates text from English to a specified language using Cohere.
- Tracks requests and responses using LangSmith.
- Exposes a RESTful API via FastAPI.
- app to access the API

## Prerequisites

- Python 3.9+
- FastAPI
- LangChain
- Cohere API key
- LangSmith API key


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/rrrreddy/LangChain-Cohere-Translator.git
    cd LangChain-Cohere-Translator
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root and add your API keys and project details:

    ```bash
    COHERE_API_KEY=your_cohere_api_key
    LANGCHAIN_API_KEY=your_langsmith_api_key
    ```

## Running the Application

1. **Start the FastAPI server:**

    ```bash
    python serve.py
    ```

2. **Access the application:**

    Open your browser and navigate to `http://localhost:8000/docs`. You should see list of api and information

3. **Test the API:**

    Use Postman or `curl` to send a POST request to the `/cohere-translator` endpoint:

    ```bash
    curl -X POST "http://localhost:8000/cohere-translator" -H "Content-Type: application/json" -d '{"text": "Hello", "language": "Spanish"}'
    ```

## Project Structure

- `serve.py`: Main application file containing FastAPI setup and route definitions.
- `app.py` : Client application file containing streamlit app setup accessing and to send request to the api from ui
- `requirements.txt`: List of dependencies required for the project.
- `.env`: Environment variables file (not included, should be created manually).

## Environment Variables

- `COHERE_API_KEY`: Your Cohere API key.
- `LANGCHAIN_API_KEY`: Your LangSmith API key.

## Dependencies

- fastapi
- langchain
- langchain_cohere
- streamlit
- langserve[all]
- python-dotenv
## License

This project is licensed under the MIT License.

