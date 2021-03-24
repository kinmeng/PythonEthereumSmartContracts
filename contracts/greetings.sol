
pragma solidity ^0.5.7;
pragma experimental ABIEncoderV2;

contract greeter{
    string[] private my_array;
    uint claim_amount=0;
    
    function greet(string memory new_greeting, uint256 new_claim)public {
       my_array.push(new_greeting);
       claim_amount= claim_amount+new_claim;
    }
    function getGreeting() public view returns(string [] memory, uint) {
        return (my_array, claim_amount);
    }
}