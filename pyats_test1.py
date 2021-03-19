import json
from rich import print as rprint
from genie.testbed import load
from pyats.async import pcall

testbed = load("nb_testbed.yaml")

dev = testbed.devices['RT1']
dev.connect(log_stdout=False)
ip_route = dev.parse("show ip route")


for name in testbed.devices.keys():
    dev = testbed.devices[name]
    dev.connect(log_stdout=False)
    interfaces = dev.parse("show interfaces")
    pretty_interfaces = json.dumps(interfaces, indent=2)
    rprint(f"{name}\n{pretty_interfaces}\n")