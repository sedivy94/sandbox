import bibliopixel
#from bibliopixel.layout import *
#from bibliopixel.animation import *
#from bibliopixel.strip import * 
#from bibliopixel.layout.strip
#from bibliopixel.drivers.driverbase import *
#from bibliopixel.drivers.serial import *
from bibliopixel.drivers.WS2812B import *


#An example of building a driver 
# causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

# Load driver for the AllPixel
from bibliopixel.drivers.serial import *
# set number of pixels & LED type here
driver = Serial(num = 10, ledtype = LEDTYPE.WS2812B)

# load the LEDStrip class
from bibliopixel.layout import *
led = Strip(driver)

# load channel test animation
from bibliopixel.animation import StripChannelTest
anim = StripChannelTest(led)

try:
    # run the animation
    anim.run()
except KeyboardInterrupt:
    # Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()

	

