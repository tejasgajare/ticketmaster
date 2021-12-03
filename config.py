import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('API_USERNAME')
PASSWORD = os.getenv('API_PASSWORD')
DOMAIN = f"https://{os.getenv('API_DOMAIN')}.zendesk.com"
LIST_TICKETS = '/api/v2/tickets.json?include=users,organizations'

def get_show_ticket_url(id):
    return f'/api/v2/tickets/{id}.json?include=users,organizations'