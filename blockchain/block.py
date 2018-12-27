#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jeanfernandes
criptomoeda
jeancoin
"""

import hashlib
import time

class JeanCoin:

    def __init__(self):
        self.blocs = []
        self.setGenesisBlock()

    def getAll(self):
        return self.blocs[:]

    def setGenesisBlock(self):    
        self.addNewBlock('Primeiro Bloco')

    def addNewBlock(self, data, previousHash = 0):
        ts = int(round(time.time() * 1000))
        bloco = Block(0, "", ts, data, self.calculateHash(str(0), str(previousHash), str(ts), data))
        self.blocs.append(bloco)

    @staticmethod
    def calculateHash(index, previousHash, timestamp, data):
        return hashlib.sha256((index + previousHash + timestamp + data).encode()).hexdigest

class Block:

    def __init__(self, index, previousHash, timestamp, data, hash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash


if __name__ == '__main__':
    blockchain = JeanCoin()
    blockchain.addNewBlock('vai filhao')
    print(blockchain.getAll())