from web3 import Web3
import hashlib

# Initialize web3 connection
w3 = Web3(Web3.HTTPProvider('https://neox-network-url'))

# Smart contract details
contract_address = '0xYourSmartContractAddress'
contract_abi = [...]  # ABI for the smart contract

# Load the smart contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Function to store video hash
def store_video_hash(video_path):
    # Generate hash of video
    hasher = hashlib.sha256()
    with open(video_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    video_hash = hasher.hexdigest()
    
    # Store hash on blockchain
    tx_hash = contract.functions.storeVideoHash(video_hash).transact({'from': w3.eth.default_account})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt
