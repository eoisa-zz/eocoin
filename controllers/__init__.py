from flask_restplus import Api

from .mine import ns as mine
from .transaction import ns as transaction

api = Api(title='eoCoin',
          prefix='/api/eocoin')

api.add_namespace(transaction)
api.add_namespace(mine)
