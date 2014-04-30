import os
import requests

from test_runner import BaseComponentTestCase
from qubell.api.private.testing import instance, environment, workflow, values

@environment({
    "default": {},
    "AmazonEC2_CentOS_63": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-eb6b0182"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "root"
        }]
    },
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
    },
    "AmazonEC2_Ubuntu_1004": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-0fac7566"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "ubuntu"
        }]
    }
})
class TomcatDevComponentTestCase(BaseComponentTestCase):
    name = "component-tomcat-dev"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
    }]

     @instance(byApplication=name)
     def test_zookeeper_ui(self, instance):
        urls = instance.returnValues['output.zoo-ui']
        for url in urls:
        resp = requests.get(url, verify=False)

        assert resp.status_code == 200    

