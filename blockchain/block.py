 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jeanfernandes
criptomoeda
jeancoin
"""

import hashlib
import time
import binascii

class JeanCoin:

    def __init__(self, genesisBlock):
        self.__chain = []
        self.__chain.append(genesisBlock)
        self.DIFFICULTY_ADJUSTMENT = 10
        self.BLOCK_INTERVAL = 120

    def getDifficulty(self):
        latestBlock = self.getLatestBlock()
        if latestBlock.index % self.DIFFICULTY_ADJUSTMENT == 0 and latestBlock.index != 0:
            return self.getAjustedDifficulty()
        else:
            return latestBlock.difficulty

    def getAjustedDifficulty(self):
        latestBlock = self.getLatestBlock()
        previousAdjustmentBlock = self.__chain[len(self.__chain) - self.DIFFICULTY_ADJUSTMENT]
        timeExpected = self.BLOCK_INTERVAL * self.DIFFICULTY_ADJUSTMENT
        timeTaken = latestBlock.timestamp - previousAdjustmentBlock.timestamp
        if timeTaken < timeExpected * 2:
            return previousAdjustmentBlock.difficulty + 1
        elif timeTaken > timeExpected * 2:
            return previousAdjustmentBlock.difficulty - 1
        else:
            return previousAdjustmentBlock.difficulty

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

    def hashMatchesDifficulty(self, hash, diff):
        hashBin = binascii.unhexlify(hash)
        requiredPrefix = '0' * int(diff)
        return hashBin.startswith(requiredPrefix)

    def findBlock(self, index, previousHash, ts, data, diff):
        nonce = 0
        while True: 
            hash = calculateHash(index, previousHash, ts, data, diff, nonce)
            if self.hashMatchesDifficulty(hash, diff):
                block = Block(index, previousHash, ts, data, diff, nonce)
                return block
            nonce = nonce + 1

    @staticmethod
    def calculateHash(index, previousHash, timestamp, data):
        return hashlib.sha256((index + previousHash + timestamp + data).encode()).hexdigest

class Block:

    def __init__(self, index, previousHash, timestamp, data, hash, difficulty, nonce):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce

def calculateHash(index, previousHash, timestamp, data, difficulty, nonce):
    return hashlib.sha256(
        (str(index) + previousHash + str(timestamp) + data + str(difficulty) + str(nonce)).encode()).hexdigest()

if __name__ == '__main__':
    ts = int(round(time.time() * 1000))
    #genesisBlock = Block(0, "", ts, "genesis",
    #calculateHash(0, "", ts, "genesis"))
    