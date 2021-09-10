# my attempted at reproducing preloaded.ino in circuitpython


import board
import time
from adafruit_magtag.magtag import MagTag
from rainbowio import colorwheel  # TODO install to lib
from analogio import AnalogIn

MAGTAG = MagTag(status_neopixel=None)

print("Adafruit EPD Portal demo, in CircuitPython")

MAGTAG.peripherals.neopixel_disable = False
MAGTAG.peripherals.neopixels.setBrightness(0.5)
MAGTAG.peripherals.speaker_disable = True
MAGTAG.peripherals.neopixel_disable = True  # Initialize all pixels to 'off'

MAGTAG.graphics.display.clearBuffer()
MAGTAG.graphics.display.drawBitmap(0, 38, magtaglogo_mono, MAGTAGLOGO_WIDTH, MAGTAGLOGO_HEIGHT, EPD_BLACK)
MAGTAG.graphics.display.display()

#   analogReadResolution(12); //12 bits
#   analogSetAttenuation(ADC_11db);  //For all pins
accX = AnalogIn(board.acceleration.X)
accY = AnalogIn(board.acceleration.Y)
accZ = AnalogIn(board.acceleration.Z)


loops = 0
rotation = 0
while True:
    loops = loops + 1

    if loops == 0:
        print(f'Rotation: {rotation}')
        if rotation == 0 or rotation == 2:
            MAGTAG.display.setRotation(rotation*90) # TODO: will this work?
            MAGTAG.graphics.display.clearBuffer()
            MAGTAG.graphics.display.drawBitmap(0, 38, magtaglogo_mono, MAGTAGLOGO_WIDTH, MAGTAGLOGO_HEIGHT, EPD_BLACK)
            MAGTAG.graphics.display.display()

    # Red LED
    MAGTAG.peripherals.neopixels[3] = 0xFF0000

    print(".")
    if loops % 10 == 0:    
        # Display the results (acceleration is measured in m/s^2)
        print(f'X: {accX.value} \tY: {accY.value} \tZ: {accZ.value} m/s^2')
        if accX.value < -5 and abs(accY.value < 5):
            rotation = 1
        if accX.value < 5 and abs(accY.value > 5):
            rotation = 0
        if accX.value > 5 and abs(accY.value < 5):
            rotation = 3
        if accX.value < 5 and abs(accY.value < -5):
            rotation = 2
      
        print(f'Light sensor: {MAGTAG.peripherals.light}')

        # scan i2c
        print("I2C scanner: ")
        i2c.try_lock()
        i2c_list = i2c.scan()
        i2c.unlock()
        print(i2c_list)

    if MAGTAG.peripherals.button_a_pressed:
        print("Button A pressed")
        MAGTAG.peripherals.neopixels.fill(0xFF0000)
    elif MAGTAG.peripherals.button_b_pressed:
        print("Button B pressed")
        MAGTAG.peripherals.neopixels.fill(0x00FF00)
    elif MAGTAG.peripherals.button_c_pressed:
        print("Button C pressed")
        MAGTAG.peripherals.neopixels.fill(0x0000FF)
    elif MAGTAG.peripherals.button_d_pressed:
        print("Button D pressed")
        MAGTAG.peripherals.speaker_disable = False
        MAGTAG.play_tone(1319, 0.1)
        MAGTAG.play_tone(988, 0.1)
        MAGTAG.peripherals.speaker_disable = True
    else:
        # neopixelate
        for i in range(len(MAGTAG.peripherals.neopixels)):
        color_value = ((i * 256 / len(MAGTAG.peripherals.neopixels)) + loops) % 255
        MAGTAG.peripherals.neopixels[i] = colorwheel(color_value)

    # Red LED
    MAGTAG.peripherals.neopixels[3] = 0x000000

    time.sleep(0.01)
