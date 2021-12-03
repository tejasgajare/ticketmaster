# Ticket Master

### An application to View Tickets from Zendesk API
Project created as a part of Zendesk Coding Challenge Summer - 2022

```console
> git clone git@github.com:tejasgajare/ticketmaster.git
> cd ticketmaster
> pip install pipenv    # we'll use pipenv to manage our virtual environment
> pipenv install
```

### Create a .env file in the ticketmaster directory to store our environment variables
```
└── ticketmaster
    ├── .env
    ├── .gitignore
    ├── .venv
    ├── LICENSE
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── app
    └── run.py
```
### Add the following environment variables to .env file with your domain name and credentials
We will be using these environment variables inside our project for authentication and other settings
```
API_DOMAIN=<yourdomain>         # If your domain name is zccstudents.zendesk.com, please just put zccstudents.
API_USERNAME=<yourusername>     # Zendesk account email address
API_PASSWORD=<yourpassword>     # Zendesk account password
API_PAGESIZE=25
```
### Start the flask server
```console
> pipenv shell      # activate the virtual environment with pipenv
> python run.py     # start the application
```
### To run unit tests
```console
> pytest
```

### To check the coverage for unit tests
```console
> coverage run -m pytest
> coverage report
```

### Screenshots
![alt text](https://github.com/tejasgajare/ticketmaster/blob/main/screenshots/ScreeshotListTickets.png)

![alt text](https://github.com/tejasgajare/ticketmaster/blob/main/screenshots/ScreenshotShowTicket.png)