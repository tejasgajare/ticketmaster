from flask import Blueprint, render_template, request
import requests
import config
import json
from app import PAGE_SZIE

bp = Blueprint('list_tickets', __name__, url_prefix='/')


def fetch_all_tickets(page=1):
    try:
        page = max(1, int(page))
    except (ValueError, TypeError):
        page = 1
    
    url = config.DOMAIN + f'/api/v2/tickets.json?page={page}&per_page={PAGE_SZIE}'
    response = requests.get(url, auth=(config.USERNAME, config.PASSWORD))
    data = json.loads(response.text)

    # TODO: No ticket found in Data? KeyError
    return data

@bp.route('/')
def show_tickets():
    page = request.args.get('page')
    data = fetch_all_tickets(page)
    return render_template("list_tickets.html", data=data)
    