from flask import Flask, request, jsonify
from blockchain_utils import create_blockchain_escrow, release_blockchain_milestone

app = Flask(__name__)

@app.route('/api/payment', methods=['POST'])
def handle_payment():
    data = request.json
    order_id = data.get('order_id')
    amount = data.get('amount', 1.0)
    print(f"--- [Flask] New Payment for Order {order_id} ---")
    tx_hash = create_blockchain_escrow(order_id, amount)
    return jsonify({"msg": "Escrow created on Blockchain", "tx": tx_hash})

@app.route('/api/shipping-update', methods=['POST'])
def handle_shipping():
    data = request.json
    order_id = data.get('order_id')
    status = data.get('status') 
    mapping = {"vessel_departed": 0, "port_arrival": 1, "delivered": 2}
    index = mapping.get(status)
    if index is not None:
        print(f"--- [Flask] Releasing funds for {status} ---")
        tx_hash = release_blockchain_milestone(order_id, index)
        return jsonify({"msg": f"Funds released for {status}", "tx": tx_hash})
    return jsonify({"error": "Invalid status"}), 400

if __name__ == '__main__':
    app.run(port=5000)
