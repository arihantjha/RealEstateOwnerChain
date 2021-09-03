import datetime
import hashlib
import json
from flask import Flask, jsonify

class OwnerChain:


#the first owner, as there is no previousOwner we just give it a random value of 
#zero for simplicity
    def __init__(self):
        self.chain = []
        self.newOwner(proof = 1, previousOwnerHash = '0')


#when requested adds the new owner of the house into the existing chain
#along with it storing the necessay information:
    def newOwner(self, proof, previousOwnerHash):
        OwnerInfo = {'ownerNumber': len(self.chain) + 1,
                 'timeOfPurchase': str(datetime.datetime.now()),
                 'proof': proof,
                 'previousOwnerHash': previousOwnerHash,
                 }
        self.chain.append(OwnerInfo)
        return OwnerInfo


#brings us the lst created block in the chain, would help while adding a new owner
    def get_previous_OwnerInfo(self):
        return self.chain[-1]


#a necessary algorithm that needs to be soved to transer the house to a new owner
#right now for simplicity the algo is simple but can 
#take as input important information like the amount paid, token for the house
#some id information, etc.
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(abs(new_proof**2 - previous_proof**2)).encode()).hexdigest()
            if hash_operation[:4] == '000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof


#The hash function provides the uniqueness and security to our chain
#we just encode all the information regarding the home owner using the
#sha256 hashing algo which returns a 256 bit hexadecimal no. which is unique 
#for every single block in the chian.
    def hash(self, OwnerInfo):
        encoded_OwnerInfo = json.dumps(OwnerInfo, sort_keys = True).encode()
        return hashlib.sha256(encoded_OwnerInfo).hexdigest()

#Checking if all the blocks in the chain are valid, by validating the 
#previousHash of every block
    def is_chain_valid(self, chain):
        previous_OwnerInfo = chain[0]
        OwnerInfo_ownerNumber = 1
        while OwnerInfo_ownerNumber < len(chain):
            OwnerInfo = chain[OwnerInfo_ownerNumber]
            if OwnerInfo['previousOwnerHash'] != self.hash(previous_OwnerInfo):
                return False
            previous_proof = previous_OwnerInfo['proof']
            proof = OwnerInfo['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_OwnerInfo = OwnerInfo
            OwnerInfo_ownerNumber += 1
        return True

