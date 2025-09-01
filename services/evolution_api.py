import os

import requests

from dotenv import load_dotenv


load_dotenv()


class EvolutionAPI:

    BASE_URL = os.getenv('EVO_BASE_URL')
    INSTANCE_NAME = 'AcreditaBahia'

    def __init__(self):
        self.__api_key = os.getenv('AUTHENTICATION_API_KEY')
        self.__headers = {
            'apikey': self.__api_key,
            'Content-Type': 'application/json'
        }

    def send_message(self, number, text):
        payload = {
            'number': number,
            'text': text,
        }
        url = f'{self.BASE_URL}/message/sendText/{self.INSTANCE_NAME}'
        print(f"Attempting to POST to: {url}")  # Print the URL for debugging
        try:
            response = requests.post(
                url=url,
                headers=self.__headers,
                json=payload,
                timeout=30  # Add a 30-second timeout
            )
            # Raise an exception for bad status codes (4xx or 5xx)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            print("Error: The request timed out.")
            raise
        except requests.exceptions.ConnectionError as e:
            print(f"Error: Connection to {self.BASE_URL} failed. Please check the URL and ensure the API is running.")
            print(f"Underlying error: {e}")
            raise
        except requests.exceptions.HTTPError as e:
            print(f"Error: Received an HTTP error. Status code: {e.response.status_code}")
            print(f"Response body: {e.response.text}")
            raise
