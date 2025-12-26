// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract TradeFlowEscrow {

    struct Escrow {
        uint256 totalAmount;
        uint256 releasedAmount;
        bool hold;
        bool delay;
    }

    struct Milestone {
        string name;
        uint256 percentage;
        bool released;
    }

    mapping(bytes32 => Escrow) public escrows;
    mapping(bytes32 => Milestone[]) public milestones;

    function createEscrow(bytes32 paymentId, uint256 amount) external {
        escrows[paymentId] = Escrow(amount, 0, false, false);

        milestones[paymentId].push(Milestone("Vessel Departed", 30, false));
        milestones[paymentId].push(Milestone("Port Arrival", 40, false));
        milestones[paymentId].push(Milestone("Delivered", 30, false));
    }

    function releaseMilestone(bytes32 paymentId, uint index) external {
        require(!escrows[paymentId].hold, "Escrow on hold");
        require(!milestones[paymentId][index].released, "Already released");

        uint amount =
            (escrows[paymentId].totalAmount * milestones[paymentId][index].percentage) / 100;

        escrows[paymentId].releasedAmount += amount;
        milestones[paymentId][index].released = true;
    }

    function setHold(bytes32 paymentId, bool status) external {
        escrows[paymentId].hold = status;
    }

    function setDelay(bytes32 paymentId, bool status) external {
        escrows[paymentId].delay = status;
    }
}
