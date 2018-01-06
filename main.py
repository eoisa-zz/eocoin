from block import Block


def main(block_num):
    blockchain = [Block.create_genesis()]
    print("\nGenesis block has been created!\n".format(blockchain[0].index))
    old_block = blockchain[0]

    for i in range(0, block_num):
        new_block = Block.new_block(old_block)
        blockchain.append(new_block)
        print("Block [{}] has been added to the blockchain!".format(new_block.index))
        print("Hash: {}".format(new_block.hash))
        print("Data: {}\n".format(new_block.data))
        old_block = new_block


if __name__ == '__main__':
    number_of_blocks = input('Number of blocks to add to chain: ')
    main(int(number_of_blocks))