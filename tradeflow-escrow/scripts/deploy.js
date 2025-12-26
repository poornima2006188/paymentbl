const hre = require("hardhat");
const fs = require('fs');

async function main() {
    console.log("STARTING DEPLOYMENT SCRIPT...");
    const Escrow = await hre.ethers.getContractFactory("TradeFlowEscrow");
    const escrow = await Escrow.deploy();

    await escrow.waitForDeployment();
    const address = await escrow.getAddress();

    console.log("\n\n----------------------------------------------------");
    console.log("DEPLOYMENT COMPLETE");
    console.log("Escrow Contract Address:", address);
    console.log("----------------------------------------------------\n\n");

    fs.writeFileSync('contract_address.txt', address);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
