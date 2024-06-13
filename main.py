# main.py
from web3 import Web3

# Setup
alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/lYX7-yxVlGyqpNSajOonWwLVDz4ik-Ka"
w3 = Web3(Web3.HTTPProvider(alchemy_url))

if w3.is_connected():
    print("Connected to Alchemy Mainnet")
else:
    print("Failed to connect to Alchemy Mainnet")
    exit()

def get_token_balance(address, token_contract_address):