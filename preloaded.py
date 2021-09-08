# my attempted at reproducing preloaded.ino in circuitpython


# import board
# import json
# import time
# import random
# import alarm
# import terminalio
from adafruit_magtag.magtag import MagTag
from rainbowio import colorwheel  # TODO install to lib

MAGTAG = MagTag()
MAGTAG.peripherals.neopixel_disable = False

# - shows MAGTAG
# - flashes LEDS
# - 4 buttons
# - wakeup
# - flash and invert MAGTAG
# - button 1 - all leds red while held
# - button 2 - all leds green while held
# - button 3 - all leds blue while held
# - button 4 - sound.  and leds?
# rotation?
# may have to reinstall ino (good to learn how)

print("Adafruit EPD Portal demo, in CircuitPython")

MAGTAG.peripherals.neopixels.setBrightness(0.5)
MAGTAG.peripherals.neopixel_disable = True  # Initialize all pixels to 'off'

#   pinMode(SPEAKER_SHUTDOWN, OUTPUT);
#   digitalWrite(SPEAKER_SHUTDOWN, LOW);

#   // Red LED
#   pinMode(13, OUTPUT);

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

# void loop() {
#   j++;
#   if (j == 0) {
#     Serial.print("Rotation: "); Serial.println(rotation);
#     if (rotation == 0 || rotation == 2) {
#       display.setRotation(rotation);
#       display.clearBuffer();
#       display.drawBitmap(0, 38, magtaglogo_mono, MAGTAGLOGO_WIDTH, MAGTAGLOGO_HEIGHT, EPD_BLACK);
#       display.display();
#     }
#   }
#   // Red LED On
#   digitalWrite(13, HIGH);

#   //Serial.print(".");
#   if (j % 10 == 0) {
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

#   if (! digitalRead(BUTTON_A)) {
#     Serial.println("Button A pressed");
#     intneo.fill(0xFF0000);
#     intneo.show();    
#   }
#   else if (! digitalRead(BUTTON_B)) {
#     Serial.println("Button B pressed");
#     intneo.fill(0x00FF00);
#     intneo.show();    
#   }
#   else if (! digitalRead(BUTTON_C)) {
#     Serial.println("Button C pressed");
#     intneo.fill(0x0000FF);
#     intneo.show();
#   }
#   else if (! digitalRead(BUTTON_D)) {
#     intneo.fill(0x0);
#     intneo.show();
#     Serial.println("Button D pressed");
#     digitalWrite(SPEAKER_SHUTDOWN, HIGH);
#     play_tune(audio, sizeof(audio));
#     digitalWrite(SPEAKER_SHUTDOWN, LOW);
#   } else {
#     // neopixelate
#     for (int i = 0; i < intneo.numPixels(); i++) {
#       intneo.setPixelColor(i, Wheel(((i * 256 / intneo.numPixels()) + j) & 255));
#     }
#     intneo.show(); 
#   }

#   // Red LED off
#   digitalWrite(13, LOW);


#   delay(10);
# }

# void play_tune(const uint8_t *audio, uint32_t audio_length) {
#   uint32_t t;
#   uint32_t prior, usec = 1000000L / SAMPLE_RATE;
  
#   for (uint32_t i=0; i<audio_length; i++) {
#     while((t = micros()) - prior < usec);
#     dacWrite(A0, audio[i]);
#     prior = t;
#   }
# }

# // Input a value 0 to 255 to get a color value.
# // The colours are a transition r - g - b - back to r.
# uint32_t Wheel(byte WheelPos) {
#   WheelPos = 255 - WheelPos;
#   if (WheelPos < 85) {
#     return intneo.Color(255 - WheelPos * 3, 0, WheelPos * 3);
#   }
#   if (WheelPos < 170) {
#     WheelPos -= 85;
#     return intneo.Color(0, WheelPos * 3, 255 - WheelPos * 3);
#   }
#   WheelPos -= 170;
#   return intneo.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
# }