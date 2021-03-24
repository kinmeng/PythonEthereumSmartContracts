#@ Salman Dabbakuti
import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from flask import Flask, render_template, request

# web3.py instance
w3 = Web3(HTTPProvider("http://localhost:7545"))
print(w3.isConnected())
key="b4fe7ab84abc5b931f9074bf4deb66ff185678a26938f51894d65e645ec3722b"
acct = w3.eth.account.from_key(key)

# compile your smart contract with truffle first
truffleFile = json.load(open('./build/contracts/greeter.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']
contract= w3.eth.contract(bytecode=bytecode, abi=abi)

#building transaction
construct_txn = contract.constructor().buildTransaction({
    'from': acct.address,
    'nonce': w3.eth.getTransactionCount(acct.address),
    'gas': 1728712,
    'gasPrice': w3.toWei('21', 'gwei')})

signed = acct.signTransaction(construct_txn)

tx_hash=w3.eth.sendRawTransaction(signed.rawTransaction)
print(tx_hash.hex())
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print("Contract Deployed At:", tx_receipt['contractAddress'])
contract_address= tx_receipt['contractAddress']
contract_instance = w3.eth.contract(abi=abi, address=contract_address)
        

app = Flask(__name__)


@app.route("/")
def index():
    print(w3.isConnected())
    greeting = contract_instance.functions.getGreeting().call()
    print(greeting)
    contract_data = {
        'greeting': greeting
    }

    return render_template('index.html',**contract_data)

@app.route("/greet" , methods=['GET','POST'])
def ind():
    greeting = request.form.get("write")
    claim = int(request.form.get("claim")) 
    tx = contract_instance.functions.greet(greeting, claim).buildTransaction({'nonce': w3.eth.getTransactionCount(acct.address)})
    signed_tx = w3.eth.account.signTransaction(tx, key)
    tx_hash= w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    gree = contract_instance.functions.getGreeting().call()
    contract_data = {
        'greeting': gree
        }
    return render_template('index.html', **contract_data)


if __name__ == '__main__':
    app.run(debug = True)