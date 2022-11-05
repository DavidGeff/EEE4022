#!/usr/bin/env python
#  Adapted by David Sephton-Poultney

import time
import csv
from bh1745 import BH1745

csv0 = open('160bh.csv', 'w+');
csv1 = open('320bh.csv', 'w+');
csv2 = open('640bh.csv', 'w+');
csv3 = open('1280bh.csv', 'w+');
csv4 = open('2560bh.csv', 'w+');
csv5 = open('5120bh.csv', 'w+');
bh1745 = BH1745()

bh1745.setup()
bh1745.set_adc_gain_x(1)
bh1745.set_measurement_time_ms(160)
bh1745.set_channel_compensation(1, 1, 1, 1)
bh1745.enable_white_balance(1)

i = 0
time.sleep(1.0)  # Skip the reading that happened before the LEDs were enabled

while i < 20:
    r, g, b, c = bh1745.get_rgbc_raw()
    print('RGBC: {:10.1f} {:10.1f} {:10.1f} {:10.1f}'.format(r, g, b, c))
    csv0.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
    csv0.write('\n')
    i += 1
    time.sleep(0.2)

print('\n')
i = 0
bh1745.set_measurement_time_ms(320)
time.sleep(1.0)
    
while i < 20:
    r, g, b, c = bh1745.get_rgbc_raw()
    print('RGBC: {:10.1f} {:10.1f} {:10.1f} {:10.1f}'.format(r, g, b, c))
    csv1.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
    csv1.write('\n')
    i += 1
    time.sleep(0.2)
    

print('\n')    
i = 0
bh1745.set_measurement_time_ms(640)
time.sleep(1.0)
    
while i < 20:
    r, g, b, c = bh1745.get_rgbc_raw()
    print('RGBC: {:10.1f} {:10.1f} {:10.1f} {:10.1f}'.format(r, g, b, c))
    csv2.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
    csv2.write('\n')
    i += 1
    time.sleep(0.3)

print('\n')
i = 0
bh1745.set_measurement_time_ms(1280)
time.sleep(1.5)
    
while i < 20:
    r, g, b, c = bh1745.get_rgbc_raw()
    print('RGBC: {:10.1f} {:10.1f} {:10.1f} {:10.1f}'.format(r, g, b, c))
    csv3.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
    csv3.write('\n')
    i += 1
    time.sleep(0.3)

print('\n')
i = 0
bh1745.set_measurement_time_ms(2560)
time.sleep(2.5)
    
while i < 20:
    r, g, b, c = bh1745.get_rgbc_raw()
    print('RGBC: {:10.1f} {:10.1f} {:10.1f} {:10.1f}'.format(r, g, b, c))
    csv4.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
    csv4.write('\n')
    i += 1
    time.sleep(0.5)

print('\n')
i = 0
bh1745.set_measurement_time_ms(5120)
time.sleep(5.0)
    
while i < 20:
    r, g, b, c = bh1745.get_rgbc_raw()
    print('RGBC: {:10.1f} {:10.1f} {:10.1f} {:10.1f}'.format(r, g, b, c))
    csv5.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
    csv5.write('\n')
    i += 1
    time.sleep(1.0)