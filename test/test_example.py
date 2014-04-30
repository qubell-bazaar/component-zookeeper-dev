import os

from test_runner import BaseComponentTestCase
from qubell.api.private.testing import instance, environment, workflow, values


@environment({
    "default": {}
})
class ComponentTestCase(BaseComponentTestCase):
    name = "name-component"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
    }]

    def test_fail(self):
        assert Fail, "Test is not implemented, start to write your tests here"

    def test_pass(self):
        assert True, "Just another test, that passes"
