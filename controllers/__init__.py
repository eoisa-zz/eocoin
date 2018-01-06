from flask_restplus import Api

from .blocks import ns as blocks
from .mine import ns as mine
from .transaction import ns as transaction

api = Api(title='eoCoin',
          prefix='/api/eocoin')

api.add_namespace(transaction)
api.add_namespace(blocks)
api.add_namespace(mine)
