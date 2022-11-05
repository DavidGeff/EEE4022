#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  VEML3328.py
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


csv0 = open('50ve33.csv', 'w+');
csv1 = open('100ve33.csv', 'w+');
csv2 = open('200ve33.csv', 'w+');
csv3 = open('400ve33.csv', 'w+');
bus = smbus.SMBus(1)    # /dev/i2c-1, in my case

VEML3328_ADDR = 0x10   
VEML3328_CONF = 0x00

# -------------------------   
def VEML3328_init(): 
    VEML3328_enableSensor()
    
# -------------------------   
def VEML3328_write(cmd,val): #//Write 0x00 register 
    bus.write_word_data(VEML3328_ADDR,cmd,val)
    
# -------------------------   
def VEML3328_read(cmd): 
 return bus.read_word_data(VEML3328_ADDR,cmd)

# -------------------------   
def getRed(): #//Get red light measurement
    return VEML3328_read(0x05);
# -------------------------   
def getGreen():#//Get green light measurement
    return VEML3328_read(0x06);
# -------------------------   
def getBlue(): #//Get blue light measurement  
    return VEML3328_read(0x07);
# -------------------------   
def getWhite(): #//Get white light measurement
    return VEML3328_read(0x04)  
    
# -------------------------   
def VEML3328_enableSensor(): #//Enable light sensor in VEML3328
    conf = VEML3328_read(VEML3328_CONF)
    conf = conf & 0x00FE
    VEML3328_write(VEML3328_CONF, conf)
    time.sleep(.001)
      
# -------------------------   
def VEML3328_disableSensor(): #//Disable light sensor
	conf = VEML3328_read(VEML3328_CONF)
	conf = conf & 0x00FE
	conf = conf | 0x000
	VEML3328_write(VEML3328_CONF, conf)
	time.sleep(.001)
    
 # -------------------------   
def VEML3328_setIT(it): #integration time  0=50ms,1=100,2=200,3=400
	conf = VEML3328_read(VEML3328_CONF)
	conf = conf & 0x0003
	it = it << 4
	VEML3328_write(VEML3328_CONF, (conf | it))

# -------------------------   
def VEML3328_forceMode(): #forced measurement mode.(Trigger to start)
	conf = VEML3328_read(VEML3328_CONF)
	conf = conf & 0x0072
	conf = conf | 0x0002
	VEML3328_write(VEML3328_CONF, conf)
        
# -------------------------   
def VEML3328_autoMode(): #auto measurement mode
    conf = VEML3328_read(VEML3328_CONF)
    conf = conf & 0x0070
    VEML3328_write(VEML3328_CONF, conf)
    
# -------------------------   
def VEML3328__trigger(): #Trigger a measurement (forced mode)
	conf = VEML3328_read(VEML3328_CONF)
	conf = conf & 0x0072
	VEML3328_write(VEML3328_CONF, (conf | 0x0004))
	time.sleep(.001)
	VEML3328_write(VEML3328_CONF, (conf & 0x0070))    

def readAllLoop():
    r=getRed()
    g=getGreen()
    b=getBlue()
    c=getWhite()
        
    print( "red=",r," : ","grn=",g ," : ","blu=", b," : ","wht=",c)   
    loopTimer = threading.Timer(2, readAllLoop)
    loopTimer.start()

#######################################################################

def main(args):
    VEML3328_init()
    VEML3328_setIT(0)
    VEML3328_autoMode()
    
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
    VEML3328_setIT(1)
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
    VEML3328_setIT(2)
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
        time.sleep(0.3)
        
    print('\n')
    VEML3328_setIT(3)
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
        time.sleep(0.5)
        
    VEML3328_disableSensor()
    
    return 0
    
###########################

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
