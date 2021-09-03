import datetime
import hashlib
import json
from flask import Flask, jsonify
from add_new_owner import OwnerChain, app

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': OwnerChain.chain,
                'length': len(OwnerChain.chain)}
    return jsonify(response), 200