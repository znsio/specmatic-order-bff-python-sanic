import pytest
from specmatic.core.specmatic import Specmatic
from api import app
from definitions import ROOT_DIR

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 9090
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'


class TestContract:
    pass


stub = None
app_server = None

try:
    stub = Specmatic.start_stub(stub_host, stub_port, ROOT_DIR)
    stub.set_expectations([expectation_json_file])

    app_server = Specmatic.start_asgi_app(app, app_host, app_port)

    Specmatic.test(TestContract, app_host, app_port, ROOT_DIR)
except Exception as e:
    print(f"Error: {e}")
    raise e
finally:
    if app_server is not None:
        app_server.stop()
    if stub is not None:
        stub.stop()

if __name__ == '__main__':
    pytest.main()
