# Import dependencies
import subprocess
import os
import json
from dotenv import load_dotenv
from pprint import pprint
# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from constants import *
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3 import Account, middleware, Web3
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import geth_poa_middleware

def derive_wallets(coin=BTC,mnemonic=mnemonic, numderive=3):
   
    command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --numderive={numderive} --coin="{coin}" --format=json' 
    
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
   
    keys = json.loads(output)
    return  keys

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {
   ETH: derive_wallets(coin =ETH),
   BTCTEST: derive_wallets(coin = BTCTEST)
  }
pprint(coins)
#print("Hello there")
# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin,priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin,account,to,amount):
    if coin == ETH: 
        gas = w3.eth.estimateGas(
            {"from":eth_acc.address, "to":recipient, "value": amount}
        )
        return { 
            "from": eth_acc.address,
            "to": recipient,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(eth_acc.address)
        }
    
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    
# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin,account,to,amount):
    tx = create_tx(coin, account, to, amount)
    if coin == ETH:
        signed_txn = eth_acc.sign_transaction(tx)
        result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(result.hex())
        return result.hex()
    elif coin == BTCTEST:
        tx_btctest = create_tx(coin, account, to, amount)
        signed_txn = account.sign_transaction(tx)
        print(signed_txn)
        return NetworkAPI.broadcast_tx_testnet(signed_txn)
   
