from evdev import InputDevice, list_devices, ecodes, categorize

devices = map(InputDevice, list_devices())
possible_devs = []

for dev in devices:
    eventry = dev.capabilities(verbose=True).get(('EV_KEY',1), None)
    if eventry is not None and ('BTN_MOUSE', 272) in eventry:
        possible_devs.append(dev)

print ('Choose the device you want to debug : ')
for i, dev in enumerate(possible_devs):
    print( '%i. %-20s %-64s on %s' % (i, dev.fn, dev.name, dev.phys))

dev_index = input('Number: ')
dev = possible_devs[int(dev_index)]

print ('Waiting for the first event on %s' % dev.fn)
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))
