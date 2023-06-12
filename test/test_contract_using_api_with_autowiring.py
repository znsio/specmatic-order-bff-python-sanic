import pytest
import configparser
from definitions import ROOT_DIR
from specmatic.core.specmatic import Specmatic
from specmatic.servers.asgi_app_server import ASGIAppServer

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 9090
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'


class TestContract:
    pass


def set_app_config(host: str, port: int):
    config = configparser.ConfigParser()
    config.read(ROOT_DIR + '/cfg.ini')
    config['dev']['ORDER_API_HOST'] = host
    config['dev']['ORDER_API_PORT'] = str(port)
    with open(ROOT_DIR + '/cfg.ini', 'w') as configfile:
        config.write(configfile)


def reset_app_config():
    config = configparser.ConfigParser()
    config.read(ROOT_DIR + '/cfg.ini')
    config['dev']['ORDER_API_HOST'] = '127.0.0.1'
    config['dev']['ORDER_API_PORT'] = '9090'
    with open(ROOT_DIR + '/cfg.ini', 'w') as configfile:
        config.write(configfile)


Specmatic() \
    .with_project_root(ROOT_DIR) \
    .with_stub(expectations=[expectation_json_file]) \
    .with_asgi_app('app:app', set_app_config_func=set_app_config, reset_app_config_func=reset_app_config) \
    .test(TestContract) \
    .run()

if __name__ == '__main__':
    pytest.main()
