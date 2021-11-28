import os
from flask import Blueprint, render_template
import requests
import json

bp = Blueprint('tickets', __name__, url_prefix='/')

def fetch_all_tickets():
    username = os.getenv('API_USERNAME')
    password = os.getenv('API_PASSWORD')
    URL = f"https://{os.getenv('API_DOMAIN')}.zendesk.com/api/v2/tickets"

    response = requests.get(URL, auth=(username, password))

    data = json.loads(response.text)
    tickets = data['tickets']
    return tickets

@bp.route('/')
def show_tickets():
    tickets = fetch_all_tickets()
    return render_template("tickets.html", tickets=tickets)
