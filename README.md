
This repo contains a number of the simple examples that are provided by the
Magtag Overview:
- https://learn.adafruit.com/adafruit-magtag/overview


The shipping demo code is in preloaded.ino and described here:
- https://learn.adafruit.com/adafruit-magtag/shipping-demo


Using CP bootloader:
- adafruit-circuitpython-adafruit_magtag_2.9_grayscale-en_US-6.3.0.uf2

Using bundle:
- https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210903/adafruit-circuitpython-bundle-6.x-mpy-20210903.zip

## Files

The following is a list of the source files here.

- cpcode.py - default circuitpython from bundle (with stdout going to screen)
- get_date_time.py - example from adafruit, <b>WARNING<b> This requires creating an account on https://accounts.adafruit.com/
- interent_test.py - example from adafruit, see below
- shipping_demo.ino - the pre loaded code on the hardware, see below
- magtaglog.h - c array of logo bitmask
- coin.h - c array of sound for shipping demo
- shipping_demo.py - my port of preloaded to circuitpython (not complete)
- sample_secret.py - example of secrets file that goes at root
- MagTag_Killed_By_Google - Google Graveyard example

Below are some more details about some of these files.
## Internet test

At minumum, need the following from bundle:

- adafruit_requests.mpy
- neopixel.mpy

This helps determine if you have the internet configured correctly on your board.

## Sample secrets

secrets.py saved in CIRCUITPY root along side code.py.  <b>WARNING<b> Be careful not to commit secret.py file.

secrets = {
    'ssid' : 'home_wifi_network',
    'password' : 'wifi_password',
    'aio_username' : 'my_adafruit_io_username',
    'aio_key' : 'my_adafruit_io_key',
    'timezone' : "America/New_York", # http://worldtimeapi.org/timezones
    }

## Learnings

- learned how to set up secrets and wifi access
- attempting to code the shipping ino sketch to circuitpython is informative
- but they diverge
- the encapsulation if the MAGTAG class can hinder the coding
- still informative, even if the port is not completed
- bugs me, but this may not be completed


## References

https://learn.adafruit.com/adafruit-magtag/overview<br>
https://learn.adafruit.com/adafruit-magtag/shipping-demo<br>
https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210903/adafruit-circuitpython-bundle-6.x-mpy-20210903.zip<br>
https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard<br>
https://icanhazdadjoke.com/api<br>

## TODO List

- [done] Turn on internet_test.py
- [done] clean up README.md
- (optional) Signup for account and test time
- code shipping_demo.py from shipping_demo.ino
- convert c style bitmask to python
- convert c style audio to python
- turn on shipping_demo.py from shipping_demo.ino





