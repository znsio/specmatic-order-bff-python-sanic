import pytest
import configparser
from definitions import ROOT_DIR
from specmatic.core.specmatic import Specmatic

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 9090
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'
app_contract_file = ROOT_DIR + '/test/spec/product-search-bff-api.yaml'
stub_contract_file = ROOT_DIR + '/test/spec/api_order_v1.yaml'


class TestContract:
    pass


def update_app_config_with_stub_info(host: str, port: int):
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


Specmatic.test_asgi_app('app:app',
                        TestContract,
                        project_root=ROOT_DIR,
                        expectation_files=[expectation_json_file],
                        app_config_update_func=update_app_config_with_stub_info)

reset_app_config()

if __name__ == '__main__':
    pytest.main()
