#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:39:04 2018

@author: jeanfernandes
criptomoeda
"""

import hashlib
import time

class Block:

    def __init__(self, index, previousHash, timestamp, data, hash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash



def calculateHash(index, previousHash, timestamp, data):
    return hashlib.sha256(index + previousHash + timestamp + data).hexdigest

ts = int(round(time.time() * 1000))
genesis = Block(0, "", ts, "vazio", calculateHash(
    0, "", ts, "vazio"
))