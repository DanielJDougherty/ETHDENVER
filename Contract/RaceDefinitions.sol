pragma solidity ^0.4.5;

contract RaceDefinitions {
    event UserRegistrationEvent(address adr);
    event RaceEnd(address winner);
    event UserPutEntryFee(address user, uint currentPot);

    event WinnerTookItAll(string message);
    event WinnerFailedToTakeWin(string message);
    event RaceFailed(string message);
}
