import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('API_USERNAME')
PASSWORD = os.getenv('API_PASSWORD')
DOMAIN = f"https://{os.getenv('API_DOMAIN')}.zendesk.com"