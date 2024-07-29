import pickle
import hashlib
import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.chain.append(Block(0, "0", "2024-01-01 00:00:00", "Genesis Block", "0"))

    def add_new_transaction(self, data):
        # Simplified example
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1
        new_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_hash = self.calculate_hash(new_index, previous_block.hash, new_timestamp, data)
        new_block = Block(new_index, previous_block.hash, new_timestamp, data, new_hash)
        self.chain.append(new_block)

    def mine(self):
        # Simplified example
        last_block = self.chain[-1]
        new_block = Block(
            index=last_block.index + 1,
            previous_hash=last_block.hash,
            timestamp=str(datetime.datetime.now()),
            data="New Block Data",
            hash=self.calculate_hash(last_block.index + 1, last_block.hash, str(datetime.datetime.now()), "New Block Data")
        )
        self.chain.append(new_block)
        return new_block.hash

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = str(index) + previous_hash + timestamp + data
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def save_object(self, blockchain, filename):
        with open(filename, 'wb') as file:
            pickle.dump(blockchain, file)
