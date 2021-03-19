from pyats import aetest
from genie.conf import Genie

class DeviceTestCase(aetest. Testcase):
    @aetest.setup
    def setup(self):
        self.parameters['testbed'].connect(log_stdout=False)

    @aetest.test
    def show_version(self):
        for device in self.parameters['testbed'].devices.values():
            show_ver = device.parse('show version')
            assert show_ver['version']['version_short'] == '15.7'

topology = Genie.init('nb_testbed.yaml')
aetest.main(testbed=topology)