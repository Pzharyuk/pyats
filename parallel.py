import json
from rich import print
from genie.testbed import load
from pyats.async_ import pcall
from genie.utils import Dq

def get_opsf(dev_name, testbed_value):
    routing_table = testbed_value.parse("show ip route")
    pretty_routing_table = json.dumps(routing_table, indent=2)
    return routing_table

testbed = load("nb_testbed.yaml")
testbed.connect(log_stdout=False)
result = pcall(get_opsf, dev_name=testbed.devices.keys(), testbed_value=testbed.devices.values())