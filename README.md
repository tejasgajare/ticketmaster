# Ticket Master

### An application to View Tickets from Zendesk API. Project created as a part of Zendesk Coding Challenge Summer - 2022.

```console
> git clone git@github.com:tejasgajare/ticketmaster.git
> cd ticketmaster
> pip install pipenv    # we'll use pipenv to manage our virtual environment
> pipenv install
```

### Create .env file in the ticketmaster directory.
```
└── ticketmaster
    ├── .env
    ├── .git
    ├── .gitignore
    ├── .venv
    ├── LICENSE
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── app
    └── run.py
```
### Add the following environment variables to .env with your domain name and credentials.

```
API_DOMAIN=<sampledomainhere>
API_USERNAME=<yourusername>
API_PASSWORD=<yourpassword>
```
Start the flask server
```console
> pipenv shell      # activate the virtual environment with pipenv
> python run.py     # start the application
```

