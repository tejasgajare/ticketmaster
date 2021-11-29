from flask import Blueprint, render_template
import requests
import config
import json

bp = Blueprint('show_ticket', __name__, url_prefix='/ticket')

def fetch_ticket(id):
    url = config.DOMAIN + f'/api/v2/tickets/{id}.json'
    response = requests.get(url, auth=(config.USERNAME, config.PASSWORD))
    data = json.loads(response.text)
    # TODO: No ticket found in Data? KeyError
    ticket = data['ticket']
    return ticket

@bp.route('/<id>')
def show_ticket(id):
    ticket = fetch_ticket(id)
    return render_template("show_ticket.html", ticket=ticket)