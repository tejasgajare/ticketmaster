from flask import Blueprint, render_template, redirect, url_for
import requests
import config
import json
from . import utils

bp = Blueprint('show_ticket', __name__, url_prefix='/ticket')

def fetch_ticket(id=None):
    if id is None or id == '':
        return None

    url = config.DOMAIN + config.get_show_ticket_url(id)
    response = requests.get(url, auth=(config.USERNAME, config.PASSWORD))
    data = json.loads(response.text)
    data = utils.set_namevalues(data)

    if 'ticket' not in data:
        return None

    ticket = data['ticket']
    return ticket

@bp.route('/<id>', strict_slashes=False)
def show_ticket(id=None):
    if id is None:
        return redirect(url_for('list_tickets'))

    try:
        ticket = fetch_ticket(id)
    except (requests.exceptions.RequestException, requests.exceptions.ConnectionError):
        return render_template('error.html', message='Failed to connect to the server.')
    
    return render_template("show_ticket.html", ticket=ticket)