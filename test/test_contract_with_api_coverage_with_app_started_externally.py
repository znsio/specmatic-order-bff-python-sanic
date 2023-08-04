import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.servers.asgi_app_server import ASGIAppServer

from definitions import ROOT_DIR
from api import app

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 9090
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'

app_server = ASGIAppServer('app:app', app_host, app_port)
app_server.start()


class TestContract:
    pass


Specmatic() \
    .with_project_root(ROOT_DIR) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .test_with_api_coverage_for_sanic_app(TestContract, app, app_host, app_port) \
    .run()

app_server.stop()

if __name__ == '__main__':
    pytest.main()
