import pytest

from specmatic.core.decorators import specmatic_stub, specmatic_contract_test, start_asgi_app
from definitions import ROOT_DIR

host = "127.0.0.1"
port = 8000
stub_host = "127.0.0.1"
stub_port = 9090
specmatic_json_file = ROOT_DIR + '/specmatic.json'
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'


@specmatic_contract_test(host, port, ROOT_DIR)
@start_asgi_app('sanic app:app', host, port)
@specmatic_stub(stub_host, stub_port, ROOT_DIR, [expectation_json_file])
class TestApiContract:
    pass


if __name__ == '__main__':
    pytest.main()
