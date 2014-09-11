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
            "value": "us-east-1/ami-bf5021d6"
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
            "value": "us-east-1/ami-967edcff"
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
            "value": "us-east-1/ami-9f3906f6"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "ubuntu"
        }]
    }
})
class ZookeeperDevTestCase(BaseComponentTestCase):
    name = "Zookeeper"
    meta = "https://raw.githubusercontent.com/qubell-bazaar/component-zookeeper-dev/master/meta.yml"
    apps = [{
        "name": name,
   }]
    @classmethod
    def timeout(cls):
        return 20    
    @instance(byApplication=name)
    def test_zoo_ui(self, instance):
        hosts = instance.returnValues['zoo.zoo-ui']
        for host in hosts:
           resp = requests.get(host, verify=False)
           assert resp.status_code == 200

