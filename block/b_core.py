import datetime as date
import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha3_256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))

        return sha.hexdigest()

    @staticmethod
    def create_genesis():
        return Block(index=0,
                     timestamp=date.datetime.now(),
                     data='Genesis Block',
                     previous_hash=0)

    @staticmethod
    def new_block(old_block, ledger_data):
        new_index = old_block.index + 1
        new_timestamp = date.datetime.now()
        new_data = ledger_data
        new_hash = old_block.hash
        return Block(new_index, new_timestamp, new_data, new_hash)
