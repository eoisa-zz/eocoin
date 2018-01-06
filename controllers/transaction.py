from flask_restplus import fields, Resource, Namespace

import controllers
from block import blockchain
from block.b_core import Block

ns = Namespace(name='transaction', description='how to register a transaction for eocoin')

post_transaction = ns.model('transaction', {
    'from': fields.String(description='Who sent it', example='Billy', required=True),
    'to': fields.String(description='Who received it', example='Greg', required=True),
    'amount': fields.Integer(description='How much eo was given', example=200, required=True)
})

post_transaction_success_response = ns.model('Success', {
    'message': fields.String(description='transaction successful', example='transaction successful')
})

my_transactions = []


@ns.route('')
class Transaction(Resource):
    @ns.expect(post_transaction, validation=True)
    @ns.response(200, 'transaction successful', post_transaction_success_response)
    def post(self):
        global my_transactions

        transaction = controllers.api.payload

        if len(blockchain) == 1:
            old_block = blockchain[0]
        else:
            old_block = blockchain[len(blockchain)-1]

        my_transactions.append(transaction)

        new_block = Block.new_block(old_block, my_transactions)
        blockchain.append(new_block)

        return {'message': 'transaction successful'}

