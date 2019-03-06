 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jeanfernandes
criptomoeda
jeancoin
"""

import hashlib
import binascii

class Transaction:

    def __init__(self):
        self.id = None
        self.inputs = None
        self.outputs = None

class OutPut:

    def __init__(self, address, amount):
        self.address = address
        self.amount = amount

class Input:

    def __init__(self):
        self.outputId = None
        self.outputIndex = None
        self.signature = None

    def idTransaction(self, transaction):
        inputContents = ""
        outputContents = ""
        for input in transaction.inputs:
            inputContents += (input.outputId + input.outputIndex)

        for output in transaction.outputs:
            outputContents += (output.address + output.amount)

        return hashlib.sha256((str(inputContents) + str(outputContents)).encode('utf-8')).hexdigest()

class UnspentOutput:

    def __init__(self, outputId, outputIndex, address, amout):
        self.outputId = outputId
        self.outputIndex = outputIndex
        self.address = address
        self.amount = amout

class UnspentOutputs:

    def __init__(self):
        self.__listUtxo = []

    def updateListUtxo(self, list):
        self.__listUtxo = list

    def newUnspentOutputs(self, transactions):
        list = []
        for transaction in transactions:
            for inpt in transaction.input:
                utxo = UnspentOutput(transaction.id, inpt.outputId, inpt.address, inpt.amout)
                list.append(utxo)

        self.updateListUtxo(list)

def findUnspentOutput(outputId, outputIndex, listUnspentOutputs):
    for utxo in listUnspentOutputs:
        if utxo.outputId == outputId and utxo.outputIndex == outputIndex:
            return True
    
    return False