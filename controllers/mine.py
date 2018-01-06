import datetime as date
import hashlib
from uuid import getnode as get_mac

from flask_restplus import fields, Resource, Namespace

from block import b_mine, b_core
from block import blockchain

ns = Namespace(name='mine', description='mine eocoin')

mine_success_response = ns.model('mine', {
    'message': fields.String(description='eocoin mine successful', example='eocoin mine successful')
})

transaction = []
miner_address = int(hashlib.sha1(str(get_mac()).encode('utf-8')).hexdigest(), 24)


@ns.route('')
class Mine(Resource):
    @ns.response(200, 'eocoin mine successfull', mine_success_response)
    def get(self):
        last_block = blockchain[len(blockchain) - 1]
        if last_block.index == 0:
            last_proof = 1
        else:
            last_proof = last_block.data['proof-of-work']
        proof = b_mine.proof_of_work(last_proof)

        transaction.append({
            "from": "network",
            "to": str(miner_address),
            "amount": 1})

        block_data = {
            "proof-of-work": proof,
            "transactions": list(transaction)
        }

        block_index = last_block.index + 1
        block_timestamp = this_timestamp = date.datetime.now()
        last_block_hash = last_block.hash

        transaction[:] = []

        mined_block = b_core.Block(
            block_index,
            block_timestamp,
            block_data,
            last_block_hash
        )

        blockchain.append(mined_block)

        return {
            "index": block_index,
            "timestamp": str(block_timestamp),
            "data": block_data,
            "hash": last_block_hash
        }
