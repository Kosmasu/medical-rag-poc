import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

DEEPINFRA_API_KEY = os.getenv("DEEPINFRA_API_KEY")
if not DEEPINFRA_API_KEY:
    raise ValueError("Please set the DEEPINFRA_API_KEY environment variable")

