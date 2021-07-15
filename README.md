# Unit19_MultiBlockchain_Wallet
Assignment for unit 19

# Overview
This assignment focuses on the creation of a mult-currency crypto wallet via "hd-wallet" (Hierarchical Deterministic Wallet). An HD wallet allows for a group of wallets to be generated from a single seed phrase.  The HD wallet contains a tree structure where each node has a private and public key. As mentioned above, this allows for multiple unique currencies to be held in the same wallet.

# Steps
The code contained in wallet.py has all of the necessary functions for deriving the wallets, storing the output from the derivation, and sending transactions.
Our function to derive the wallet creates 3 separate wallets for each ETH, and BTCTEST.  The output of this can be found in wallet.txt.  Each wallet has a unique address, private key, and public key.
Here is the code snippet needed to generate the wallets:

'''def derive_wallets(coin=BTC,mnemonic=mnemonic, numderive=3):
   
        command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --numderive={numderive} --coin="{coin}" --format=json' 
    
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        keys = json.loads(output)
        return  keys
'''

