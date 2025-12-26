const hre = require("hardhat");

async function main() {
    const contractAddress = "0xB7f8BC63BbcaD18155201308C8f3540b07f84F5e";
    const Escrow = await hre.ethers.getContractFactory("TradeFlowEscrow");
    const escrow = await Escrow.attach(contractAddress);

    const dynamicId = "PAYMENT_" + Date.now();
    const paymentId = hre.ethers.id(dynamicId);
    const amount = hre.ethers.parseEther("10");

    console.log(`\n🚀 STARTING NEW TRADE: ${dynamicId}`);
    console.log("--------------------------------------------");

    console.log("Step 1: Creating Escrow on Blockchain...");
    const tx1 = await escrow.createEscrow(paymentId, amount);
    await tx1.wait();
    console.log("✅ Success: Escrow Initialized!");

    console.log("\nStep 2: Releasing 'Vessel Departed' (30%)...");
    const tx2 = await escrow.releaseMilestone(paymentId, 0);
    await tx2.wait();

    let state = await escrow.escrows(paymentId);
    console.log(`✅ Success: ${hre.ethers.formatEther(state.releasedAmount)} ETH sent to Provider.`);

    console.log("\nStep 3: Security Check (Double Release)...");
    try {
        await escrow.releaseMilestone(paymentId, 0);
    } catch (e) {
        console.log("🔒 Security block works: Cannot release same milestone twice!");
    }

    console.log("\n--------------------------------------------");
    console.log("✨ HACKATHON DEMO READY");
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
