# import libraries
import hashlib
import random
import string
import json
import binascii
import logging
import datetime
import collections

import string
import binascii
import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

class User:
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
        
    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
    transactions = []

    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time' : self.time})

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    def display_transaction(self):
        dict = self.to_dict()
        print("SENDER: " + dict['sender'])
        print('-----')
        print("RECIPIENT: " + dict['recipient'])
        print('-----')
        print("VALUE: " + str(dict['value']))
        print('-----')
        print("TIME: " + str(dict['time']))

    @staticmethod
    def display_all_transaction():
        count = 1
        for transaction in Transaction.transactions:
            print ('============================================')
            print('TRANSACTION #', count);
            print('============================================')
            count = count + 1
            transaction.display_transaction()

# Create Users
pawan = User()
shashwat = User()
puneet = User()
nitesh = User()

# Transactions
t1 = Transaction(pawan, shashwat.identity, 5.0)
t1.sign_transaction()
Transaction.transactions.append(t1)
t2 = Transaction(puneet, nitesh.identity, 10.0)
t2.sign_transaction()
Transaction.transactions.append(t2)
t3 = Transaction(puneet, nitesh.identity, 8.0)
t3.sign_transaction()
Transaction.transactions.append(t3)

# Display All Transactions
Transaction.display_all_transaction()
