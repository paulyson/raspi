import time
#from rpi_ws281x import *
from neopixel import *


def get_strip():
    # LED strip configuration:
    LED_COUNT      = 300      # Number of LED pixels.
    LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transi$
    LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INV$
    return strip

def LED_on(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


if __name__ == '__main__':
    strip = get_strip()
    strip.begin()
    LED_on(Color(0,0,0))
    time.sleep(2)
    #LED_on(Color(100,100,200))
    #time.sleep(5)
    #LED_on(Color(0,0,0))
    #time.sleep(2)
    while time.localtime().tm_hour < 18:
        for i in range(255):
            LED_on(Color(i,0,0))
            time.sleep(1/2)
        for j in range(255):
            LED_on(Color(i,j,0))
            time.sleep(1/2)
        for k in range(255):
            LED_on(Color(i,j,k))
            time.sleep(1/2)
        for x in range(255,0,-1):
            LED_on(Color(x,j,k))
            time.sleep(1/2)
        for y in range(255,0,-1):
            LED_on(Color(x,y,k))
            time.sleep(1/2)
        for z in range(255,0,-1):
            LED_on(Color(x,y,z))
            time.sleep(1/2)

    #exit()
    #time.sleep(2)
    #print("Local hour is {}".format(time.localtime().tm_hour))
    while True:
        if time.localtime().tm_hour >= 18:
            LED_on(Color(30,190,0))
        elif time.localtime().tm_hour == 8:
            LED_on(Color(120,120,170))
        else:
            LED_on(Color(0,0,0))