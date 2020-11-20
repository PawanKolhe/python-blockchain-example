# import libraries
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

def pretty_print(st):
    st_length = len(st)
    columns = 60
    new_st = ""
    i = 0
    while i < st_length:
        new_st += st[i:i+columns] + "\n"
        i += columns
    return new_st[0:st_length-2]

class Client:
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
            'recipient': self.recipient.identity,
            'value': self.value,
            'time' : self.time
        })

    def sign_transaction(self):
        signer = PKCS1_v1_5.new(self.sender._private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    def display_transaction(self):
        t = self.to_dict()
        print('\n===============')
        print("| TRANSACTION |")
        print('===============')
        print("SENDER:\n" + pretty_print(t['sender']))
        print('---------------')
        print("RECIPIENT:\n" + pretty_print(t['recipient']))
        print('---------------')
        print("VALUE:\n" + str(t['value']))
        print('---------------')
        print("TIME:\n" + str(t['time']))

    @staticmethod
    def display_all_transaction():
        count = 1
        for transaction in Transaction.transactions:
            print ('============================================') 
            print('TRANSACTION #', count);
            print('============================================')
            count = count + 1
            transaction.display_transaction()

last_block_hash = ""
TPCoins = []

class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

def dump_blockchain (self):
    print ("Number of blocks in the chain: " + str(len(self)))
    for x in range (len(TPCoins)):
        block_temp = TPCoins[x]
        print ("block # " + str(x))
        for transaction in block_temp.verified_transactions:
            transaction.display_transaction()
        print ('=====================================')

# Create Users
pawan = Client()
shashwat = Client()
puneet = Client()
nitesh = Client()

# Transactions
## T1
t1 = Transaction(pawan, shashwat, 5.0)
print("T1 Signature", t1.sign_transaction())
Transaction.transactions.append(t1)

## T2
t2 = Transaction(puneet, nitesh, 10.0)
print("T2 Signature", t2.sign_transaction())
Transaction.transactions.append(t2)

## T3
t3 = Transaction(puneet, nitesh, 8.0)
print("T3 Signature", t3.sign_transaction())
Transaction.transactions.append(t3)

block1 = Block()
block1.previous_block_hash = None
block1.Nonce = None
block1.verified_transactions.append(t1)
block1.verified_transactions.append(t2)
block1.verified_transactions.append(t3)
digest = hash (block1)
last_block_hash = digest
TPCoins.append (block1)
dump_blockchain(TPCoins)

# Display All Transactions
# Transaction.display_all_transaction()
