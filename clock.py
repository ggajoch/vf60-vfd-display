import time
from vf60.VFD import VFD

vfd = VFD('COM26', rtscts=True)

vfd.clear_display()

last_timestr = ''
while True:
    time.sleep(0.1)
    timestr = time.strftime("      %H:%M:%S", time.localtime(time.time()))
    if timestr == last_timestr:
        continue

    last_timestr = timestr
    vfd.set_cursor(1, 1)
    vfd.write(timestr)

    date = time.strftime("%A    %d.%m.%Y", time.localtime(time.time()))

    vfd.set_cursor(1, 2)
    vfd.write(date)
