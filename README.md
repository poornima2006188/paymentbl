# 🚢 TradeFlow Escrow: Blockchain-Powered Trade Settlements

A high-performance, automated escrow system designed for international trade. This project integrates **Ethereum Smart Contracts** with a **Flask Backend** to automate milestone-based payouts based on logistics updates.

---

## ✨ Key Features
- **🛡️ Milestone-Based Escrow**: Funds are locked in a smart contract and released only when specific shipping milestones are met (30/40/30 split).
- **🤖 Automated Settlement**: Flask backend simulates real-world logistics updates (e.g., from Port APIs) to trigger blockchain payouts.
- **📊 Premium Dashboard**: A glassmorphic management UI to track escrow status, total value, and released funds in real-time.
- **🛡️ Security First**: Prevents double-release of milestones and ensures funds are on-hold if disputes arise.
- **⚡ Local-First Testing**: Optimized for hackathon demonstrations using Hardhat's local network for instant, zero-cost transactions.

---

## 🛠️ Tech Stack
- **Blockchain**: Solidity, Hardhat, Ethers.js
- **Backend**: Python (Flask), Web3.py
- **Frontend**: Vanilla JavaScript (ES6+), CSS3 (Modern Glassmorphism)
- **Logistics Simulation**: Requests, JSON-RPC

---

## 📂 Project Structure
```bash
/
├── backend/                  # Python Flask Logic
│   ├── app.py                # Bridge API between Logistics & Blockchain
│   ├── blockchain_utils.py   # W3.py utilities for transaction signing
│   └── simulate_demo.py      # Script to run end-to-end automation
├── tradeflow-escrow/         # Blockchain Infrastructure
│   ├── contracts/            # Solidity Smart Contracts
│   ├── scripts/              # Deployment & Testing JS scripts
│   ├── index.html            # Management Dashboard UI
│   └── hardhat.config.js     # Blockchain environment config
└── README.md                 # Project Documentation
```

---

## 🚀 Quick Start Guide

### 1. Setup Blockchain (Terminal 1)
```powershell
cd tradeflow-escrow
npm install
npx hardhat node
```

### 2. Deploy Contract (Terminal 2)
```powershell
cd tradeflow-escrow
npx hardhat run scripts/deploy.js --network localhost
```

### 3. Start Backend API (Terminal 3)
```powershell
pip install flask web3 requests
python backend/app.py
```

### 4. Run Automated Demo (Terminal 4)
```powershell
python backend/simulate_demo.py
```

---

## 📈 Demo Lifecycle
1. **User Pays**: A unique Trade ID is created and ETH is locked in the contract.
2. **Vessel Departed**: Logistics API triggers the first **30% payout**.
3. **Port Arrival**: Logistics API triggers the second **40% payout**.
4. **Delivered**: Logistics API triggers the final **30% payout** & completes the trade.

---

## 👨‍💻 Developed By
**Poornima** - *Hackathon Project*
