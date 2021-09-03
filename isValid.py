import datetime
import hashlib
import json
from flask import Flask, jsonify
from add_new_owner import OwnerChain, app
#Checking if all the blocks in the chain are valid, by validating the 
#previousHash of every block
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = OwnerChain.is_chain_valid(OwnerChain.chain)
    if is_valid:
        response = {'message': 'No Breach, everything\'s fine '}
    else:
        response = {'message': 'Emergency, system breach!! system breach!!'}
    return jsonify(response), 200