pragma solidity >=0.5.0;

contract InsuranceContract {
        address private insurer;
        address private insured;
        string insurerName;
        string insuredName;
      
        
    constructor (
        address insurerValue,
        address insuredValue,
        string memory insurername,
        string memory insuredname,
        uint value
        
    ) public {
        
        insurer= insurerValue;
        insured= insuredValue;
        insurerName = insurername;
        insuredName = insuredname;
        value = value;
        
    }


function getInfo() public view returns(
        address insurerValue,
        address insuredValue,
        string memory insurername,
        string memory insuredname,
        uint value)
          {
        return (insurer,insured,insurerName,insuredName,value);
    }


    
    
}