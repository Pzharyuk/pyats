import json
from rich import print as rprint
from genie.testbed import load

testbed = load("nb_testbed.yaml")

dev = testbed.devices['RT1']
dev.connect(log_stdout=False)
ip_route = dev.parse("show ip route")
print(ip_route)

for name in testbed.devices.keys():
    dev = testbed.devices[name]
    dev.connect(log_stdout=False)
    interfaces = dev.parse("show interfaces")
    print(interfaces)