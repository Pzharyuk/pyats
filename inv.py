from genie.testbed import load

testbed = load("nb_testbed.yaml")

dir = dir(testbed)

devices = testbed.devices

for k, v in devices.items():
    print(k)
    print(v)
    print("\n\n")