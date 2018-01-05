import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha3_256()
        sha.update(str(self.index)+
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))

        return sha.hexdigest()

    @staticmethod
    def create_genesis():
        return Block(index=0,
                     timestamp=date.datetime.now(),
                     data=None,
                     previous_hash=None)

    @staticmethod
    def new_block(old_block):
        new_index = old_block.index + 1,
        new_timestamp = date.datetime.now()
        new_data = 'New block, who dis {}'.format(str(new_index))
        new_hash = old_block.hash
        return Block(new_index, new_timestamp, new_data, new_hash)

