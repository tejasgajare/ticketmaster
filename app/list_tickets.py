from flask import Blueprint, render_template
import requests
import config
import json

bp = Blueprint('list_tickets', __name__, url_prefix='/')

def fetch_all_tickets():
    url = config.DOMAIN + '/api/v2/tickets.json?page[size]=25'
    print("password: ", config.PASSWORD)
    print("username: ", config.USERNAME)
    print("url: ", url)
    response = requests.get(url, auth=(config.USERNAME, config.PASSWORD))
    data = json.loads(response.text)
    # import pdb; pdb.set_trace()
    # TODO: No ticket found in Data? KeyError
    tickets = data['tickets']
    return tickets

@bp.route('/')
def show_tickets():
    tickets = fetch_all_tickets()
    return render_template("list_tickets.html", tickets=tickets)
