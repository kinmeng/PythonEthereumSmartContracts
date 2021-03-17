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
        string memory insuredname
        
    ) public {
        
        insurer= insurerValue;
        insured= insuredValue;
        insurerName = insurername;
        insuredName = insuredname;
        
    }


function getInfo() public view returns(
        address insurerValue,
        address insuredValue,
        string memory insurername,
        string memory insuredname)
          {
        return (insurer,insured,insurerName,insuredName);
    }


    
    
}