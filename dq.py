import json
from rich import print as rprint
from genie.testbed import load
from genie.utils import Dq
from pyats.async_ import pcall


def get_ospf_route(hostname, dev):
    parsed = dev.parse("show ip route")
    routes = (Dq(parsed).contains('O').get_values('routes'))
    num_routes = len(routes)
    rprint(f'{hostname} has {num_routes} OSPF routes in ints routing table')



testbed = load("nb_testbed.yaml")
testbed.connect(log_stdout=False)
result = pcall(get_ospf_route, hostname=testbed.devices.keys(), dev=testbed.devices.values())