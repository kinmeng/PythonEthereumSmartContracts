import json
import sys
from web3 import Web3, HTTPProvider
from flask import Flask, render_template, request, redirect, url_for

# create a web3.py instance w3 by connecting to the local Ethereum node
w3 = Web3(HTTPProvider("http://localhost:7545"))

print(w3.isConnected())

app = Flask(__name__)

# Initialize a local account object from the private key of a valid Ethereum node address
local_acct = w3.eth.account.from_key("82eb6a7339201ab17ddaef24236613c19a1d92f357342bdb9acc477d2350a8eb")

# compile your smart contract with truffle first
truffleFile = json.load(open('./build/contracts/InsuranceContract.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']
# Initialize a contract object with the smart contract compiled artifacts
contract = w3.eth.contract(bytecode=bytecode, abi=abi)

@app.route("/create", methods=['POST','GET'])
def highestbidder():
    if request.method == "GET":
        print(w3.isConnected())
        return render_template('insurance.html')
    
    if request.method == "POST":
        txn_constructor= contract.constructor(str(request.form.get("insurerValue")),
        str(request.form.get("insuredValue")),
        str(request.form.get("insurername")),
        str(request.form.get("insuredname"))).buildTransaction(
    {
    'nonce': w3.eth.getTransactionCount(local_acct.address),
    'gas': 1728712,
    'gasPrice': w3.toWei('21', 'gwei')}
    )
        txn_constructor["to"] = ""
        txn_constructor = str(txn_constructor).replace("\'", "\"")
        
        print(txn_constructor)
        #return render_template('success.html')
        return redirect(url_for('claims', messages=txn_constructor))



@app.route("/getinfo", methods=['POST','GET']) 
def claims():
    if request.method == "GET":
        
        signed = w3.eth.account.sign_transaction(json.loads(request.args["messages"]), local_acct.key)
        tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        contract_address = tx_receipt['contractAddress']
        
        print(tx_hash.hex())
        
        # Initialize a contract instance object using the contract address which can be used to invoke contract functions
        contract_instance = w3.eth.contract(abi=abi, address=contract_address)

        info=contract_instance.functions.getInfo().call()
        print(info)
        return render_template("getinfo.html", info=info)

if __name__ == '__main__':
    app.run(debug=True)