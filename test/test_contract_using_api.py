import pytest
from specmatic.core.specmatic import Specmatic

from definitions import ROOT_DIR

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 9090
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'


class TestContract:
    pass


Specmatic() \
    .with_project_root(ROOT_DIR) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_app_module('app:app') \
    .with_app_host(app_host) \
    .with_app_port(app_port) \
    .test(TestContract) \
    .run()

if __name__ == '__main__':
    pytest.main()
