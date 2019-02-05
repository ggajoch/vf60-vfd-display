#!/usr/bin/env python3
import argparse
import time
from vf60.VFD import VFD

parser = argparse.ArgumentParser(description='VF60 clock demo app')
parser.add_argument('port', type=str, help='Serial port to use')
args = parser.parse_args()

vfd = VFD(args.port, rtscts=True)

vfd.clear_display()

last_timestr = ''
while True:
    time.sleep(0.1)
    now = time.localtime(time.time())
    timestr = time.strftime("%H:%M:%S", now).center(20)
    if timestr == last_timestr:
        continue

    last_timestr = timestr
    vfd.set_cursor(1, 1)
    vfd.write(timestr)

    date = time.strftime("%A", now).ljust(10) + time.strftime("%d.%m.%Y", now).rjust(10)

    vfd.set_cursor(1, 2)
    vfd.write(date)
