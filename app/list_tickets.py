from flask import Blueprint, render_template, request
import requests
import config
import json
from app import PAGE_SZIE
from . import utils

bp = Blueprint('list_tickets', __name__, url_prefix='/')
    
def fetch_all_tickets(page=1):
    try:
        page = max(1, int(page))
    except (ValueError, TypeError):
        page = 1
    
    url = config.DOMAIN + f'{config.LIST_TICKETS}&page={page}&per_page={PAGE_SZIE}'
    response = requests.get(url, auth=(config.USERNAME, config.PASSWORD))
    response_data = json.loads(response.text)

    if 'tickets' not in response_data:
        response_data['tickets'] = []
        return response_data

    data = utils.set_namefields(response_data)
    
    return data

@bp.route('/')
def show_tickets():
    page = request.args.get('page')

    try:
        data = fetch_all_tickets(page)
    except (requests.exceptions.RequestException, requests.exceptions.ConnectionError):
        return render_template('error.html', message='Failed to connect to the server.')
    
    if 'tickets' not in data:
        data['tickets'] = []
    if 'previous_page' not in data:
        data['previous_page'] = "null"
    if 'next_page' not in data:
        data['next_page'] = "null"
    if 'count' not in data:
        data['count'] = 0

    tickets = data['tickets']
    previous_page = data['previous_page']
    next_page = data['next_page']
    count = data['count']
    return render_template("list_tickets.html", tickets=tickets, previous_page=previous_page, next_page=next_page, count=count)
    