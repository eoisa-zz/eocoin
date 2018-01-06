from flask_restplus import fields, Resource, Namespace

from block import blockchain

ns = Namespace(name='blocks', description='get current node\'s blockchian')

block_success_response = ns.model('block', {
    'message': fields.String(description='eocoin block count', example='eocoin block count')

})


@ns.route('/')
class Blocks(Resource):
    @ns.response(200, 'eocoin block count', block_success_response)
    def get(self):
        out_chain = blockchain

        blocks = []
        for block in out_chain:
            block_index = str(block.index)
            block_timestamp = str(block.timestamp)
            block_data = str(block.data)
            block_hash = block.hash
            block = {
                "index": block_index,
                "timestamp": block_timestamp,
                "data": block_data,
                "hash": block_hash
            }
            blocks.append(block)

        return blocks
