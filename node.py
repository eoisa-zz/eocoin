from flask import Flask

from app_config import *
from controllers import api

node = Flask(__name__)
api.init_app(node)


def load_configurations():
    node.config['RESTPLUS_SWAGGER_UI_DOC_EXPANSION'] = RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    node.config['RESTPLUS_VALIDATE'] = RESTPLUS_VALIDATE
    node.config['RESTPLUS_MASK_SWAGGER'] = RESTPLUS_MASK_SWAGGER
    node.config['RESTPLUS_ERROR_404_HELP'] = RESTPLUS_ERROR_404_HELP


def main():
    load_configurations()
    node.run(debug=FLASK_DEBUG, threaded=True)


if __name__ == '__main__':
    main()
