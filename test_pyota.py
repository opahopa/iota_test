from iota import Iota, TryteString
import json

from config import SEED

# Specify seed.
api = Iota('http://iota.bitfinex.com:80', SEED)


def print_api_resp(resp):
    print(resp)
    for key, value in resp.items():
        print('{} : {}'.format(key, value))


def get_node_info():
    resp = api.get_node_info()
    print_api_resp(resp)


def generate_wallet():
    resp = api.get_new_addresses()
    print_api_resp(resp)


if __name__ == "__main__":
    generate_wallet()
