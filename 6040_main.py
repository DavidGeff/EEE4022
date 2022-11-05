#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  VEML6040.py
#  
#  Copyright 2020  <pi@kb>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Written by BitHead (Britany Head)
#  Adapted by David Sephton-Poultney
# Step 1) Enable I2C in Raspi-Config (Interfacing Options)
# Step 2) sudo apt-get install i2c-tools python3-smbus
# Step 3) plug it in (don't forget your pull-up resistors) and run this program

import smbus
import time
import threading
import csv

csv0 = open('40ve60i.csv', 'w+');
csv1 = open('80ve60i.csv', 'w+');
csv2 = open('160ve60i.csv', 'w+');
csv3 = open('320ve60i.csv', 'w+');
csv4 = open('640ve60i.csv', 'w+');
csv5 = open('1280ve60i.csv', 'w+');
bus = smbus.SMBus(1)    # /dev/i2c-1, in my case

VEML6040_ADDR = 0x10   
VEML6040_CONF = 0x00

# -------------------------   
def VEML6040_init(): 
    VEML6040_enableSensor()
    
# -------------------------   
def VEML6040_write(cmd,val): #//Write 0x00 register 
    bus.write_word_data(VEML6040_ADDR,cmd,val)
    
# -------------------------   
def VEML6040_read(cmd): 
 return bus.read_word_data(VEML6040_ADDR,cmd)

# -------------------------   
def getRed(): #//Get red light measurement
    return VEML6040_read(0x08);
# -------------------------   
def getGreen():#//Get green light measurement
    return VEML6040_read(0x09);
# -------------------------   
def getBlue(): #//Get blue light measurement  
    return VEML6040_read(0x0A);
# -------------------------   
def getWhite(): #//Get white light measurement
    return VEML6040_read(0x0B)  
    
# -------------------------   
def VEML6040_enableSensor(): #//Enable light sensor in VEML6040
    conf = VEML6040_read(VEML6040_CONF)
    conf = conf & 0x00FE
    VEML6040_write(VEML6040_CONF, conf)
    time.sleep(.001)
      
# -------------------------   
def VEML6040_disableSensor(): #//Disable light sensor
	conf = VEML6040_read(VEML6040_CONF)
	conf = conf & 0x00FE
	conf = conf | 0x000
	VEML6040_write(VEML6040_CONF, conf)
	time.sleep(.001)
    
 # -------------------------   
def VEML6040_setIT(it): #integration time  0=40ms,1=80,2=160,3=320,4=640,5=1280ms
	conf = VEML6040_read(VEML6040_CONF)
	conf = conf & 0x0003
	it = it << 4
	VEML6040_write(VEML6040_CONF, (conf | it))
        
# -------------------------   
def VEML6040_forceMode(): #forced measurement mode.(Trigger to start)
	conf = VEML6040_read(VEML6040_CONF)
	conf = conf & 0x0072
	conf = conf | 0x0002
	VEML6040_write(VEML6040_CONF, conf)
        
# -------------------------   
def VEML6040_autoMode(): #auto measurement mode
    conf = VEML6040_read(VEML6040_CONF)
    conf = conf & 0x0070
    VEML6040_write(VEML6040_CONF, conf)
    
# -------------------------   
def VEML6040__trigger(): #Trigger a measurement (forced mode)
	conf = VEML6040_read(VEML6040_CONF)
	conf = conf & 0x0072
	VEML6040_write(VEML6040_CONF, (conf | 0x0004))
	time.sleep(.001)
	VEML6040_write(VEML6040_CONF, (conf & 0x0070))    

def readAllLoop():
    r=getRed()
    g=getGreen()
    b=getBlue()
    w=getWhite()
        
    print( "red=",r," : ","grn=",g ," : ","blu=", b," : ","wht=",w)   
    loopTimer = threading.Timer(2, readAllLoop)
    loopTimer.start()

#######################################################################

def main(args):
    VEML6040_init()
    VEML6040_setIT(0)  
    VEML6040_autoMode()
    i = 0
    time.sleep(1.0)
    
    while i < 20:
        r=getRed()
        g=getGreen()
        b=getBlue()
        c=getWhite()
        
        print( "red=",r," : ","grn=",g ," : ","blu=", b," : ","wht=",c)
        csv0.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
        csv0.write('\n')
        i += 1
        time.sleep(0.2)
    
    print('\n')
    VEML6040_setIT(1)
    i = 0
    time.sleep(1.0)
    
    while i < 20:
        r=getRed()
        g=getGreen()
        b=getBlue()
        c=getWhite()
        
        print( "red=",r," : ","grn=",g ," : ","blu=", b," : ","wht=",c)
        csv1.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
        csv1.write('\n')
        i += 1
        time.sleep(0.2)
    
    print('\n')
    VEML6040_setIT(2)
    i = 0
    time.sleep(1.0)
    
    while i < 20:
        r=getRed()
        g=getGreen()
        b=getBlue()
        c=getWhite()
        
        print( "red=",r," : ","grn=",g ," : ","blu=", b," : ","wht=",c)
        csv2.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
        csv2.write('\n')
        i += 1
        time.sleep(0.4)
        
    print('\n')
    VEML6040_setIT(3)
    i = 0
    time.sleep(1.0)
    
    while i < 20:
        r=getRed()
        g=getGreen()
        b=getBlue()
        c=getWhite()
        
        print( "red=",r," : ","grn=",g ," : ","blu=", b," : ","wht=",c)
        csv3.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
        csv3.write('\n')
        i += 1
        time.sleep(0.8)
    
    print('\n')
    VEML6040_setIT(4)
    i = 0
    time.sleep(1.0)
    
    while i < 20:
        r=getRed()
        g=getGreen()
        b=getBlue()
        c=getWhite()
        
        print( "red=",r," : ","grn=",g ," : ","blu=", b," : ","wht=",c)
        csv4.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
        csv4.write('\n')
        i += 1
        time.sleep(1.2)
    
    print('\n')
    VEML6040_setIT(5)
    i = 0
    time.sleep(1.5)
    
    while i < 20:
        r=getRed()
        g=getGreen()
        b=getBlue()
        c=getWhite()
        
        print( "red=",r," : ","grn=",g ," : ","blu=", b," : ","wht=",c)
        csv5.write(str(r) + ',' + str(g) + ',' + str(b) + ',' + str(c))
        csv5.write('\n')
        i += 1
        time.sleep(1.5)
        
    VEML6040_disableSensor()
    return 0
    
###########################

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
