import os
import requests

from test_runner import BaseComponentTestCase
from qubell.api.private.testing import instance, environment, workflow, values


@environment({
    "default": {},
    "AmazonEC2_Ubuntu_1204": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-d0f89fb9"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "ubuntu"
        }]
  }
})
class ComponentTestCase(BaseComponentTestCase):
    name = "component-zookeeper-dev"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
   }]
    
    @instance(byApplication=name)
    def test_solr_search(self, instance):
        host = instance.returnValues['output.zoo-ui'][0]
        resp = requests.get(host, verify=False)

        assert resp.status_code == 200

