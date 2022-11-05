#!/usr/bin/python
# Adapted by David Sephton-Poultney

import time
import csv
import RPi.GPIO as GPIO
from TCS34725 import TCS34725
csv0 = open('2_4tcs5i.csv', 'w+');
csv1 = open('24tcs5i.csv', 'w+');
csv2 = open('50tcs5i.csv', 'w+');
csv3 = open('101tcs5i.csv', 'w+');
csv4 = open('154tcs5i.csv', 'w+');
csv5 = open('700tcs5i.csv', 'w+');

#try:
Light=TCS34725(0X29, debug=False);
if(Light.TCS34725_init() == 1):
    print("TCS34725 initialization error!!")
else:
    print("TCS34725 initialization success!!")
time.sleep(1)

i = 0;
Light.Set_Integration_Time(Light.TCS34725_INTEGRATIONTIME_2_4MS)
Light.IntegrationTime_t = Light.TCS34725_INTEGRATIONTIME_2_4MS

    
    #while True:
while i < 20: 
    Light.Get_RGBData()
    Light.GetRGB888()
    Light.GetRGB565()
    Light.GetXYZ()
    print("R: %d "%Light.R), 
    print("G: %d "%Light.G), 
    print("B: %d "%Light.B),     
    #print("R: %d "%Light.RGB888_R), 
    #print("G: %d "%Light.RGB888_G), 
    #print("B: %d "%Light.RGB888_B), 
    print("C: %#x "%Light.C),
    #print("RGB565: %#x "%Light.RG565),
    #print("RGB888: %#x "%Light.RGB888), 
    #print("X: %d "%Light.X),
    #print("Y: %d "%Light.Y),
    #print("Z: %d "%Light.Z),
    #print("LUX: %d "%Light.Get_Lux()),
    #print("CT: %dK "%Light.Get_ColorTemp())
        
    csv0.write(str(Light.R) + ',' + str(Light.G) + ',' + str(Light.B) + ',' + str(Light.C))
    csv0.write('\n')
       
    i += 1

Light.Set_Integration_Time(Light.TCS34725_INTEGRATIONTIME_24MS)
Light.IntegrationTime_t = Light.TCS34725_INTEGRATIONTIME_24MS
print('\n')
i = 0;
time.sleep(0.2)



while i < 20: 
    Light.Get_RGBData()
    Light.GetRGB888()
    Light.GetRGB565()
    Light.GetXYZ()
    print("R: %d "%Light.R), 
    print("G: %d "%Light.G), 
    print("B: %d "%Light.B),     
    #print("R: %d "%Light.RGB888_R), 
    #print("G: %d "%Light.RGB888_G), 
    #print("B: %d "%Light.RGB888_B), 
    print("C: %#x "%Light.C),
    #print("RGB565: %#x "%Light.RG565),
    #print("RGB888: %#x "%Light.RGB888), 
    #print("X: %d "%Light.X),
    #print("Y: %d "%Light.Y),
    #print("Z: %d "%Light.Z),
    #print("LUX: %d "%Light.Get_Lux()),
    #print("CT: %dK "%Light.Get_ColorTemp())
    
    csv1.write(str(Light.R) + ',' + str(Light.G) + ',' + str(Light.B) + ',' + str(Light.C))
    csv1.write('\n')
    
    i += 1
    
Light.Set_Integration_Time(Light.TCS34725_INTEGRATIONTIME_50MS)
Light.IntegrationTime_t = Light.TCS34725_INTEGRATIONTIME_50MS
print('\n')
i = 0;
time.sleep(0.2)

while i < 20: 
    Light.Get_RGBData()
    Light.GetRGB888()
    Light.GetRGB565()
    Light.GetXYZ()
    print("R: %d "%Light.R), 
    print("G: %d "%Light.G), 
    print("B: %d "%Light.B),     
    #print("R: %d "%Light.RGB888_R), 
    #print("G: %d "%Light.RGB888_G), 
    #print("B: %d "%Light.RGB888_B), 
    print("C: %#x "%Light.C),
    #print("RGB565: %#x "%Light.RG565),
    #print("RGB888: %#x "%Light.RGB888), 
    #print("X: %d "%Light.X),
    #print("Y: %d "%Light.Y),
    #print("Z: %d "%Light.Z),
    #print("LUX: %d "%Light.Get_Lux()),
    #print("CT: %dK "%Light.Get_ColorTemp())
    
    csv2.write(str(Light.R) + ',' + str(Light.G) + ',' + str(Light.B) + ',' + str(Light.C))
    csv2.write('\n')
    
    i += 1    

Light.Set_Integration_Time(Light.TCS34725_INTEGRATIONTIME_101MS)
Light.IntegrationTime_t = Light.TCS34725_INTEGRATIONTIME_101MS
print('\n')
i = 0;
time.sleep(0.2)

while i < 20: 
    Light.Get_RGBData()
    Light.GetRGB888()
    Light.GetRGB565()
    Light.GetXYZ()
    print("R: %d "%Light.R), 
    print("G: %d "%Light.G), 
    print("B: %d "%Light.B),     
    #print("R: %d "%Light.RGB888_R), 
    #print("G: %d "%Light.RGB888_G), 
    #print("B: %d "%Light.RGB888_B), 
    print("C: %#x "%Light.C),
    #print("RGB565: %#x "%Light.RG565),
    #print("RGB888: %#x "%Light.RGB888), 
    #print("X: %d "%Light.X),
    #print("Y: %d "%Light.Y),
    #print("Z: %d "%Light.Z),
    #print("LUX: %d "%Light.Get_Lux()),
    #print("CT: %dK "%Light.Get_ColorTemp())
    
    csv3.write(str(Light.R) + ',' + str(Light.G) + ',' + str(Light.B) + ',' + str(Light.C))
    csv3.write('\n')
    
    i += 1

Light.Set_Integration_Time(Light.TCS34725_INTEGRATIONTIME_154MS)
Light.IntegrationTime_t = Light.TCS34725_INTEGRATIONTIME_154MS
print('\n')
i = 0;
time.sleep(0.2)

while i < 20: 
    Light.Get_RGBData()
    Light.GetRGB888()
    Light.GetRGB565()
    Light.GetXYZ()
    print("R: %d "%Light.R), 
    print("G: %d "%Light.G), 
    print("B: %d "%Light.B),     
    #print("R: %d "%Light.RGB888_R), 
    #print("G: %d "%Light.RGB888_G), 
    #print("B: %d "%Light.RGB888_B), 
    print("C: %#x "%Light.C),
    #print("RGB565: %#x "%Light.RG565),
    #print("RGB888: %#x "%Light.RGB888), 
    #print("X: %d "%Light.X),
    #print("Y: %d "%Light.Y),
    #print("Z: %d "%Light.Z),
    #print("LUX: %d "%Light.Get_Lux()),
    #print("CT: %dK "%Light.Get_ColorTemp())
    
    csv4.write(str(Light.R) + ',' + str(Light.G) + ',' + str(Light.B) + ',' + str(Light.C))
    csv4.write('\n')
    
    i += 1

Light.Set_Integration_Time(Light.TCS34725_INTEGRATIONTIME_700MS)
Light.IntegrationTime_t = Light.TCS34725_INTEGRATIONTIME_700MS
print('\n')
i = 0;
time.sleep(0.2)

while i < 20: 
    Light.Get_RGBData()
    Light.GetRGB888()
    Light.GetRGB565()
    Light.GetXYZ()
    print("R: %d "%Light.R), 
    print("G: %d "%Light.G), 
    print("B: %d "%Light.B),     
    #print("R: %d "%Light.RGB888_R), 
    #print("G: %d "%Light.RGB888_G), 
    #print("B: %d "%Light.RGB888_B), 
    print("C: %#x "%Light.C),
    #print("RGB565: %#x "%Light.RG565),
    #print("RGB888: %#x "%Light.RGB888), 
    #print("X: %d "%Light.X),
    #print("Y: %d "%Light.Y),
    #print("Z: %d "%Light.Z),
    #print("LUX: %d "%Light.Get_Lux()),
    #print("CT: %dK "%Light.Get_ColorTemp())
    
    csv5.write(str(Light.R) + ',' + str(Light.G) + ',' + str(Light.B) + ',' + str(Light.C))
    csv5.write('\n')
    
    i += 1

Light.Disable()

#except:
#    GPIO.cleanup()
#    print ("\nProgram end")
#    exit()