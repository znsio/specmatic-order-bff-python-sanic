import os
import pytest
from specmatic.core.specmatic import Specmatic
from api import app
from definitions import ROOT_DIR
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'


class TestContract:
    pass


stub = None
app_server = None
try:
    stub = Specmatic.start_stub(project_root=ROOT_DIR)
    stub.set_expectations([expectation_json_file])

    app.config['ORDER_API_HOST'] = stub.host
    app.config['ORDER_API_PORT'] = stub.port
    app_server = Specmatic.start_asgi_app(app)

    Specmatic.test(TestContract, app_server.host, app_server.port, ROOT_DIR)
except Exception as e:
    print(f"Error: {e}")
    raise e
finally:
    app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_HOST")
    app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_PORT")
    if app_server is not None:
        app_server.stop()
    if stub is not None:
        stub.stop()

if __name__ == '__main__':
    pytest.main()
