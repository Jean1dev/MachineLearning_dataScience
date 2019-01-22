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

    def __init__(self, genesisBlock):
        self.__chain = []
        self.__chain.append(genesisBlock)

    def getLatestBlock(self):
        return self.__chain[len(self.__chain) - 1]

    def generateNextBlock(self, data):
        previous = self.getLatestBlock()
        nextIndex = previous.index + 1
        nextTs = int(round(time.time() * 1000))
        nextPreviousHash = previous.hash
        newBlock = Block(nextIndex, nextPreviousHash, nextTs, data,
            calculateHash(nextIndex, nextPreviousHash, nextTs, data))
        
        if self.validatingBlock(newBlock) == True:
            self.__chain.append(newBlock)

    def validatingBlock(self, newBlock):
        previousBlock = self.getLatestBlock()
        if previousBlock.index + 1 != newBlock.index:
            return False
        elif previousBlock.hash != newBlock.previousHash:
            return False
        return True

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

def calculateHash(index, previousHash, timestamp, data):
    return hashlib.sha256(str(index) + previousHash + str(timestamp) + data).hexdigest()

if __name__ == '__main__':
    ts = int(round(time.time() * 1000))
    genesisBlock = Block(0, "", ts, "genesis",
    calculateHash(0, "", ts, "genesis"))
    