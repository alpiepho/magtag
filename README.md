
This repo contains a number fo the simple examples that are provided by the
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
- dad_jokes.py - see below
- get_date_time.py - example from adafruit, <b>WARNING<b> This requires creating an account on https://accounts.adafruit.com/
- interent_test.py - example from adafruit, see below
- preloaded.ino - the pre loaded code on the hardware, see below
- preloaded.py - my port of preloaded to circuitpython
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


## dad_jokes.py - Started Dad Joke

Mashup of Google Graveyard this Dad Joke api:

https://icanhazdadjoke.com/api

Rough outline:
- load random from offline jokes list
- display
- get battery
- wait 5 seconds
- attempt to get new joke from site
- display
- wait 5 seconds and go to deep sleep
- button press should start from top of file?

Offline or backup_jokes are created using the python script get_jokes.py.  These are useful to allow the 
app to seem like it's working while any online data is gathered.


## Learnings

TBD


## References

https://learn.adafruit.com/adafruit-magtag/overview<br>
https://learn.adafruit.com/adafruit-magtag/shipping-demo<br>
https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210903/adafruit-circuitpython-bundle-6.x-mpy-20210903.zip<br>
https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard<br>
https://icanhazdadjoke.com/api<br>

## TODO List

- [done] Turn on internet_test.py
- [done] clean up README.md
- [done] code dad joke from offline
- (optional) Signup for account and test time
- turn on dad joke
- add next button to dad joke, enabled while awake
- add light button to dad joke, how to wake?
- code preloaded.py from preloaded.ino
- turn on preloaded.py from preloaded.ino
- idea: split lines with extra \r\n
- battery as a percent
- convert dad joke to a coffee pot watcher?


## Motes for magtag-dadjokes

This project was inspired by the following examples:

https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard<br>

https://icanhazdadjoke.com/api<br>

Everyone needs a good bad-dad-joke, and what better way than a gadget like the Magtag on 
the referidgerator to allow "sharing" them daily?

Rough outline:
- load random from offline jokes list
- display
- get battery
- wait 5 seconds
- attempt to get new joke from site
- display
- wait 5 seconds and go to deep sleep
- button press should start from top of file?
