
# TODO: this can be in a deployment config
HOST = "localhost"
PORT = 27017
MONGO_URI = f"mongodb://{HOST}:{PORT}" 
APP_PORT = PORT + 1
# TODO: until here

# TODO: setting should contain all the info 
# like app documentation
# endpoints documentataion etc.


HTTP_VERBS = {
    "GET": {
        404: 'f"No {collection.capitalize()} Found."',
    },
    "POST": {
        409: 'f"{collection.capitalize()} Already Exists."',
    },
    "PUT": {
        404: 'f"No {collection.capitalize()} Found."',
    },
    "DELETE": {
        404: 'f"No {collection.capitalize()} Found."',
    },
}

COUNTRIES = [
    "canada",
    "unitedstates",
    "mexico",
]

CITIES = [
    "vancouver",
    "toronto",
    "mexicocity",
    "guadalajara",
    "seattle",
    "atlanta",
]

STADIUMS = [
    "bcplace",
    "bmofield",
    "akron",
    "azteca",
    "lumen",
    "mercbenz"
]

POSITIONS = [
    "keeper",
    "defender",
    "midfield",
    "forward"
]

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/wcapp.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'world-cup-app': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

# TODO: debug should come from deployment config as env. var
DEBUG = False
if DEBUG:
    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']

