[![GitHub Issues](https://img.shields.io/github/issues/xinabox/Python-SL19.svg)](https://github.com/xinabox/Python-SL19/issues)
![GitHub Commit](https://img.shields.io/github/last-commit/xinabox/Python-SL19)
![Maintained](https://img.shields.io/maintenance/yes/2020)
![Build status badge](https://github.com/xinabox/Python-SL19/workflows/Python/badge.svg)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

# Python-SL19

The SL19 xChip is equipped to measure temperature as a function of infrared light/radiation (IR) radiating from objects in its field of view. Is is based on the [MLX90614](https://www.melexis.com/en/product/MLX90614/Digital-Plug-Play-Infrared-Thermometer-TO-Can) in which a IR sensitive thermopile detector chip and signal conditioning ASIC are integrated.

The MLX90614 is factory calibrated in wide temperature ranges: -40-125˚C for the ambient temperature and -70-380˚C for the object temperature. The measured value is the average temperature of all objects in the Field Of View of the sensor. The MLX90614 offers a standard accuracy of ±0.5˚C around room temperatures.

# Usage

## Mu-editor
Download [Mu-editor](https://github.com/xinabox/mu-editor/releases/tag/v1.1.0a2)

### CW01 and CW02
- Use [XinaBoxUploader](https://github.com/xinabox/XinaBoxUploader/releases/latest) and flash MicroPython to the CW01/CW02.
- Download Python packages from the REPL with the following code:
    ```python
    import network
    import upip
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("ssid", "password")
    upip.install("xinabox-SL19")
    ```

### CC03, CS11 and CW03
- Download the .UF2 file for CC03/CS11/CW03 [CircuitPython](https://circuitpython.org/board/xinabox_cs11/) and flash it to the board.
- TO DO

### MicroBit
- TO DO

## Raspberry Pi

Requires Python 3
```
pip3 install xinabox-SL19
```

# Example
```python
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
```
