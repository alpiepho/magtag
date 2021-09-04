
This repo contains a number o the simple examples that are provided by the
Magtag Overview:<br>

https://learn.adafruit.com/adafruit-magtag/overview


The shipping demo code is in preloaded.ino and described here:

https://learn.adafruit.com/adafruit-magtag/shipping-demo



Using bundle:

https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210903/adafruit-circuitpython-bundle-6.x-mpy-20210903.zip


## Internet test

At minumum, need the following from bundle:

- adafruit_requests.mpy
- neopixel.mpy



## Sample secrets

secrets.py saved in CIRCUITPY root along side code.py.  <b>WARNING<b> Be careful not to commit secret.py file.

secrets = {
    'ssid' : 'home_wifi_network',
    'password' : 'wifi_password',
    'aio_username' : 'my_adafruit_io_username',
    'aio_key' : 'my_adafruit_io_key',
    'timezone' : "America/New_York", # http://worldtimeapi.org/timezones
    }


## Access Timer Server

<b>WARNING<b> This requires creating an account on https://accounts.adafruit.com/


## Google Graveyard example

 See MagTag_Killed_By_Google.


## Started Dad Joke

Mashup of Google Graveyard this Dad Joke api:

https://icanhazdadjoke.com/api



## TODO List

- Turn on internet_test.py
- (optional) Signup for account and test time
- credits button
- next button

## Motes for magtag-dadjokes

This project was inspired by the following examples:

https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard<br>

https://icanhazdadjoke.com/api<br>

Everyone needs a good bad-dad-joke, and what better way than a gadget like the Magtag on 
the referidgerator to allow "sharing" them daily?



