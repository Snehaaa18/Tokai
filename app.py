from web3 import Web3
from flask import Flask, render_template, request

# Setup
alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/lYX7-yxVlGyqpNSajOonWwLVDz4ik-Ka"
w3 = Web3(Web3.HTTPProvider(alchemy_url))
if w3.is_connected():
    print("Connected to Alchemy Mainnet")
else:
    print("Failed to connect to Alchemy Mainnet")
    exit()
    
# ERC-20 Token ABI
erc20_abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    },
]

def get_token_balance(wallet_address, token_address):
    # Create a contract instance
    token_contract = w3.eth.contract(address=token_address, abi=erc20_abi)
    
    # Get token balance
    balance = token_contract.functions.balanceOf(wallet_address).call()
    
    # Get token decimals
    decimals = token_contract.functions.decimals().call()
    
    # Convert balance to human-readable format
    human_readable_balance = balance / (10 ** decimals)
    
    return human_readable_balance
    


app=Flask(__name__)
@app.route('/')

def index():
    if request.method == 'POST':
        wallet_address = request.form['wallet_address']
        token_address = request.form['token_address']
        try:
            balance = get_token_balance(wallet_address, token_address)
            message = f"Token Balance: {balance}"
        except Exception as e:
            message = str(e)
        return render_template('home.html', message=message)
    return render_template('home.html')

def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
    