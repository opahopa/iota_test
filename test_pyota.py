from iota import Iota, TryteString, \
    ProposedTransaction, Address, Tag, Bundle, Transaction
from six import binary_type

import sys

from config import SEED, NODE_URL

# Specify seed.
api = Iota(NODE_URL, SEED)


def print_api_resp(resp):
    print(resp)
    for key, value in resp.items():
        print('{} : {}'.format(key, value))


def get_node_info():
    resp = api.get_node_info()
    print_api_resp(resp)


def generate_wallet():
    index = 0
    count = 1

    try:
        resp = api.get_new_addresses(index, count)
        print(resp)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    else:
        #Walidate address by "attaching" to tangle
        for addy in resp['addresses']:
            # addr = binary_type(addy).decode('ascii')
            addr = Address(addy)
            print('addr: {} length: {} \n'.format(addr.address, len(addr.address)))

            confirm_wallet_transaction = ProposedTransaction(
                address=addr,
                value=0,
            )

            transfer_result = api.send_transfer(depth=4, transfers=[confirm_wallet_transaction])
            print_api_resp(transfer_result)

            transaction_bundle = Bundle(transfer_result)
            for tr in transaction_bundle:
                for key, value in tr:
                    print('{} : {}'.format(key, value))


if __name__ == "__main__":
    generate_wallet()
    # get_node_info()
