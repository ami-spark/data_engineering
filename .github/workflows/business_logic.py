# This is the business logic. It knows nothing about who invokes it.
from jupyter_server.terminal import initialize


def read_Config():
    config = 0
    pass


def do_some_logic(data):
    # Global variables used to store static data

    config = 0

    # Do something with config object
    return data


def initialize(config):
    read_Config()

    print("This is my result")
    return config
