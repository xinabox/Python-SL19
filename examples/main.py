from xCore import xCore
from xSL19 import xSL19

# SL19 instance
SL19 = xSL19()

# configure SL19
SL19.init()

while True:
    tempAmbient = SL19.getAmbientTempC()	# returns ambient temp in degree celcius
    tempObject = SL19.getObjectTempC()		# returns object temp in degree celcius

    # prints on console
    print('Ambient: ',tempAmbient,' C')
    print('Object : ',tempObject,' C')

    xCore.sleep(2000)