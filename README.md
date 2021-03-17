# Insurance Blockchain Application

This repository is forked from sijo0703/PythonEthereumSmartContracts as linked and modified for the project's purpose

In case the setup instructions don't work, please refer to this link: 
https://medium.com/swlh/develop-test-and-deploy-your-first-ethereum-smart-contract-with-truffle-14e8956d69fc

Setup instructions:
1. Install NodeJS (https://nodejs.org/en/) used for compilation
2. Install Truffle
npm install -g truffle
3. Install Ganache
4. Setup the necessary flask modules
5. Every other modules should be in requirements.txt

<h2> Setup environment </h2>

Create your python environment
Then run pip install -r requirements.txt

Three main parts to modify this project:
Create solidity project file, put in the folder ./contracts (make sure it's tested on remix)
If it's the first time you are using truffle, run truffle init
Subsequently, simply run truffle compile > which will create a JS deployment file which you do not need to edit

Now, run flask by issuing the command python3 insurance.py

Take note:

To find an address or key for use, you need to replace the address with your own live address from Ganache.
Open up Ganache > for each ADDRESS you can find a corresponding key icon on the right. Click on it and you will find a private key. Replace the key where appropriate in the code



