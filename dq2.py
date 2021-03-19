import json
from rich import print as rprint
from genie.testbed import load
from genie.utils import Dq
from pyats.async_ import pcall


def get_ospf_route(hostname, dev):
    parsed = dev.parse("show interfaces")
    oper_up = parsed.q.contains_key_value("oper_status", "up").get_values('[0]')
    rprint(json.dumps(f"{hostname} interfaces in up status {oper_up}", indent=2))



testbed = load("nb_testbed.yaml")
testbed.connect(log_stdout=False)
result = pcall(get_ospf_route, hostname=testbed.devices.keys(), dev=testbed.devices.values())