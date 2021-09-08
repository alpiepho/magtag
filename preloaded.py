# my attempted at reproducing preloaded.ino in circuitpython


import board
import time
from adafruit_magtag.magtag import MagTag
from rainbowio import colorwheel  # TODO install to lib

MAGTAG = MagTag(status_neopixel=None)
MAGTAG.peripherals.neopixel_disable = False

print("Adafruit EPD Portal demo, in CircuitPython")

MAGTAG.peripherals.neopixels.setBrightness(0.5)
MAGTAG.peripherals.neopixel_disable = True  # Initialize all pixels to 'off'
MAGTAG.peripherals.speaker_disable = True

#   // Red LED
#   pinMode(13, OUTPUT);
# board.NEOPIXEL

#   // Neopixel power
#   pinMode(NEOPIXEL_POWER, OUTPUT);
#   digitalWrite(NEOPIXEL_POWER, LOW); // on

#   display.begin(THINKINK_MONO);
  
#   if (! lis.begin(0x19)) {
#     Serial.println("Couldnt start LIS3DH");
#     display.clearBuffer();
#     display.setTextSize(3);
#     display.setTextColor(EPD_BLACK);
#     display.setCursor(20, 40);
#     display.print("No LIS3DH?");
#     display.display();
#     while (1) delay(100);
#   }

#   analogReadResolution(12); //12 bits
#   analogSetAttenuation(ADC_11db);  //For all pins
#   display.clearBuffer();
#   display.drawBitmap(0, 38, magtaglogo_mono, MAGTAGLOGO_WIDTH, MAGTAGLOGO_HEIGHT, EPD_BLACK);
#   display.display();



loops = 0
rotation = 0

while True:
    loops = loops + 1

    if loops == 0:
        print(f'Rotation: {rotation}')
        if rotation == 0 or rotation == 2:
            MAGTAG.display.setRotation(rotation*90) # TODO: will this work?
             MAGTAG.display.clearBuffer()
             MAGTAG.display.drawBitmap()
            # display.drawBitmap(0, 38, magtaglogo_mono, MAGTAGLOGO_WIDTH, MAGTAGLOGO_HEIGHT, EPD_BLACK);
            # display.display();

#   // Red LED On
#   digitalWrite(13, HIGH);

    print(".")
    if loops % 10 == 0:
        pass
#    if (j % 10 == 0) {
#       sensors_event_t event;
#       lis.getEvent(&event);
    
#       /* Display the results (acceleration is measured in m/s^2) */
#       Serial.print("X: "); Serial.print(event.acceleration.x);
#       Serial.print(" \tY: "); Serial.print(event.acceleration.y);
#       Serial.print(" \tZ: "); Serial.print(event.acceleration.z);
#       Serial.println(" m/s^2 ");
#       if ((event.acceleration.x < -5) && (abs(event.acceleration.y) < 5)) {
#         rotation = 1;
#       }
#       if ((abs(event.acceleration.x) < 5) && (event.acceleration.y > 5)) {
#         rotation = 0;
#       }
#       if ((event.acceleration.x > 5) && (abs(event.acceleration.y) < 5)) {
#         rotation = 3;
#       }
#       if ((abs(event.acceleration.x) < 5) && (event.acceleration.y < -5)) {
#         rotation = 2;
#       }
      
#       int light = analogRead(LIGHT_SENSOR);
#       Serial.print("Light sensor: ");
#       Serial.println(light);
  
#       Serial.print("I2C scanner: ");
#       for (int i = 0x07; i <= 0x77; i++) {
#         Wire.beginTransmission(i);
#         bool found (Wire.endTransmission() == 0);
#         if (found) {
#           Serial.printf("0x%02x, ", i);
#         }
#       }
#       Serial.println();
#   }

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

#   // Red LED off
#   digitalWrite(13, LOW);

    time.sleep(0.01)
