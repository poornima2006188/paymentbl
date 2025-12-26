from web3 import Web3

RPC_URL = "http://127.0.0.1:8545"
CONTRACT_ADDRESS = "0xB7f8BC63BbcaD18155201308C8f3540b07f84F5e"
PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
ACCOUNT_ADDRESS = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

ABI = [
    {"inputs":[{"name":"paymentId","type":"bytes32"},{"name":"amount","type":"uint256"}],"name":"createEscrow","outputs":[],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[{"name":"paymentId","type":"bytes32"},{"name":"index","type":"uint256"}],"name":"releaseMilestone","outputs":[],"stateMutability":"nonpayable","type":"function"}
]

w3 = Web3(Web3.HTTPProvider(RPC_URL))
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def create_blockchain_escrow(order_id, amount_in_eth):
    payment_id = w3.keccak(text=order_id)
    amount_wei = w3.to_wei(amount_in_eth, 'ether')
    nonce = w3.eth.get_transaction_count(ACCOUNT_ADDRESS)
    
    txn = contract.functions.createEscrow(payment_id, amount_wei).build_transaction({
        'from': ACCOUNT_ADDRESS,
        'nonce': nonce,
        'gas': 300000,
        'gasPrice': w3.eth.gas_price
    })

    signed_txn = w3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    return w3.to_hex(tx_hash)

def release_blockchain_milestone(order_id, milestone_index):
    payment_id = w3.keccak(text=order_id)
    nonce = w3.eth.get_transaction_count(ACCOUNT_ADDRESS)

    txn = contract.functions.releaseMilestone(payment_id, milestone_index).build_transaction({
        'from': ACCOUNT_ADDRESS,
        'nonce': nonce,
        'gas': 300000,
        'gasPrice': w3.eth.gas_price
    })

    signed_txn = w3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    return w3.to_hex(tx_hash)
