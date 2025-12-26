import requests
import time
import random

BASE_URL = "http://127.0.0.1:5000/api"
ORDER_ID = f"TRADE_{random.randint(1000, 9999)}"

def run_full_demo():
    print(f"\n🎬 STARTING AUTOMATED HACKATHON DEMO: {ORDER_ID}")
    print("="*50)
    res = requests.post(f"{BASE_URL}/payment", json={"order_id": ORDER_ID, "amount": 10.5})
    print(f"BLOCKCHAIN RESPONSE: {res.json()['msg']}\nTX HASH: {res.json()['tx']}")

    milestones = ["vessel_departed", "port_arrival", "delivered"]
    for status in milestones:
        time.sleep(2)
        print(f"\n[Logistics] Status Update: {status.upper()}")
        res = requests.post(f"{BASE_URL}/shipping-update", json={"order_id": ORDER_ID, "status": status})
        print(f"BLOCKCHAIN SETTLEMENT: {res.json()['msg']}\nTX HASH: {res.json()['tx']}")
    print("\n✅ DEMO COMPLETE")

if __name__ == "__main__":
    run_full_demo()
