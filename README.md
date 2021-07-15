# Unit19_MultiBlockchain_Wallet
Assignment for unit 19

# Overview
This assignment focuses on the creation of a mult-currency crypto wallet via "hd-wallet" (Hierarchical Deterministic Wallet). An HD wallet allows for a group of wallets to be generated from a single seed phrase.  The HD wallet contains a tree structure where each node has a private and public key. As mentioned above, this allows for multiple unique currencies to be held in the same wallet.

# Steps
The code contained in wallet.py has all of the necessary functions for deriving the wallets, storing the output from the derivation, and sending transactions.
Our function to derive the wallet creates 3 separate wallets for each ETH, and BTCTEST.  The output of this can be found in [Wallet.txt](https://github.com/msvt37/Unit19_MultiBlockchain_Wallet/blob/55d9fdaccde091a5a051d1acf907fb0dd7b07e18/wallet.txt)

Each wallet has a unique address, private key, and public key.
Here is the code snippet needed to generate the wallets:

```Python
   def derive_wallets(coin=BTC,mnemonic=mnemonic, numderive=3):
   
        command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --numderive={numderive} --coin="{coin}" --format=json' 
    
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        keys = json.loads(output)
        return  keys
  ```

Called from the following:
```Python
# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {
   ETH: derive_wallets(coin =ETH),
   BTCTEST: derive_wallets(coin = BTCTEST)
  }
```
Per the assigment instructions, we fund one of the BTCTEST addresses from a testnet faucet so that transactions may be sent from it.  For our purposes, we simply picked the first address in the list as our funded account: *msEyH6qigVri1xLxxGkPq4ZBdajvSNvdNj*  

The following image shows a successful funding for that address:
![Funded](https://github.com/msvt37/Unit19_MultiBlockchain_Wallet/blob/04ec129ede62421681c0f5b3445b9ff0e6d84dbb/1stTransaction.PNG)

From a terminal on the local machine I ran the followin to send a transaction to one of the other addresses in the wallet:
```
from wallet import *
account1  = priv_key_to_account(BTCTEST,"cUwwm3Vhzkf37y4PcRKTT1N4T4z7bJFHtk8HMZaeEyrG2RgmzoPP")
result = send_tx(BTCTEST, account1, "mgXbaS3U9KvX4Y6kBPfGZc1PnccYsHuvho", .0001)
```

