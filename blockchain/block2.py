#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"https://medium.com/@felipemfp/entendendo-como-funciona-uma-blockchain-com-python-4e5a66f09e16"

from hashlib import sha256
from datetime import datetime


class Blockchain:

    def __init__(self):
        self.blocks = []
        self.set_genesis_block()

    def set_genesis_block(self):
        data = 'Hello, World!' 
        timestamp = datetime.utcnow().timestamp()
        prev_hash = 0
        index = 0
        self.hash_block(
            data, timestamp, prev_hash, index
        )
    
    def hash_block(self, data, timestamp, prev_hash, index):
        hash = ''
        nonce = 1
        while not self.is_hash_valid(hash):
            block = '{}:{}:{}:{}:{}'.format(
                data, timestamp, prev_hash, index, nonce
            )
            hash = sha256(block.encode()).hexdigest()
            nonce += 1
        print('[nonce]', nonce)
        self.blocks.append(hash)
    
    def get_last_hash(self):
        return self.blocks[-1]
    
    def is_hash_valid(self, hash):
        return hash.startswith('0000')

    def add_new_block(self, data):
        index = len(self.blocks)
        prev_hash = self.get_last_hash()
        timestamp = datetime.utcnow().timestamp()
        self.hash_block(
            data, timestamp, prev_hash, index
        )
    
    def get_all(self):
        return self.blocks[:]

if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.add_new_block('Primeiro bloco!')
    blockchain.add_new_block('Blockchain é top!')
    blockchain.add_new_block('Mais uma vez!')

    print(blockchain.get_all())
