import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.servers.asgi_app_server import ASGIAppServer
from specmatic.coverage.servers.sanic_app_coverage_server import SanicAppCoverageServer

from definitions import ROOT_DIR
from api import app

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 9090
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'

app_server = ASGIAppServer('app:app', app_host, app_port)
coverage_server = SanicAppCoverageServer(app)

app_server.start()
coverage_server.start()


class TestContract:
    pass


Specmatic() \
    .with_project_root(ROOT_DIR) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_endpoints_api(coverage_server.endpoints_api) \
    .test(TestContract, app_host, app_port) \
    .run()

app_server.stop()
coverage_server.stop()

if __name__ == '__main__':
    pytest.main()
