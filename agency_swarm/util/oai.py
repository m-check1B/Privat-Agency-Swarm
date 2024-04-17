#import threading
#import openai
import os
from groq_client import GroqClient  # Make sure GroqClient is correctly implemented and imported
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class OpenAIClient:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                logging.debug("Creating a new instance of OpenAIClient")
                cls._instance = super(OpenAIClient, cls).__new__(cls)
                cls._instance.initialize_client()
            else:
                logging.debug("Using existing instance of OpenAIClient")
        return cls._instance

    def initialize_client(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            logging.error("OpenAI API key is not set. Please set it.")
            raise ValueError("OpenAI API key is not set. Please set it.")
        logging.debug("Initializing OpenAI client with API key.")
        self.client = openai.OpenAI(api_key=api_key, timeout=5, max_retries=5)

    # ... (rest of the OpenAIClient class)

def get_llm_client(client_type, api_key):
    logging.debug(f"Getting LLM client of type: {client_type}")
    if client_type == "openai":
        return OpenAIClient(api_key)
    elif client_type == "groq":
        return GroqClient(api_key)  # Make sure GroqClient is correctly implemented and imported
    else:
        logging.error(f"Unsupported LLM client type: {client_type}")
        raise ValueError(f"Unsupported LLM client type: {client_type}")

if __name__ == "__main__":
    logging.info("Script started.")
    client_type_input = "groq"
    api_key_input = input("Enter the API key: ").strip()

    logging.debug(f"User selected LLM client type: {client_type_input}")
    llm_client = get_llm_client(client_type_input, api_key_input)

    prompt_input = input("Enter the prompt for the LLM: ").strip()
    logging.debug(f"Sending prompt to LLM: {prompt_input}")
    response = llm_client.send_prompt(prompt_input)
    logging.info("Response received from LLM:")
    print(response)
