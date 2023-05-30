import configparser

from sanic import Sanic
from definitions import ROOT_DIR

config = configparser.ConfigParser()
config.read(ROOT_DIR + '/cfg.ini')

app = Sanic("OrderBFF")
app.config["ORDER_API_HOST"] = config.get('dev', 'ORDER_API_HOST')
app.config["ORDER_API_PORT"] = config.get('dev', 'ORDER_API_PORT')


from api.routes import *
