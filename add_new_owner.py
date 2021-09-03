from ownerChain import OwnerChain
import datetime
import hashlib
import json
from flask import Flask, jsonify
from ownerChain import wchain
app = Flask(__name__)


ownerChain = OwnerChain()

@app.route('/add_new_owner', methods = ['GET'])
def add_new_owner():
    previous_OwnerInfo = OwnerChain.get_previous_OwnerInfo()
    previous_proof = previous_OwnerInfo['proof']
    proof = OwnerChain.proof_of_work(previous_proof)
    previousOwnerHash = OwnerChain.hash(previous_OwnerInfo)
    OwnerInfo = OwnerChain.newOwner(proof, previousOwnerHash)
    response = {'message': 'House Alloted to new Owner',
                'ownerNumber': OwnerInfo['ownerNumber'],
                'timeOfPurchase': OwnerInfo['timeOfPurchase'],
                'proof': OwnerInfo['proof'],
                'previousOwnerHash': OwnerInfo['previousOwnerHash']}
    return jsonify(response), 200