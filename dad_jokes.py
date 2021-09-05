# Started from https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard

import json
import time
import random
import alarm
import terminalio
from adafruit_magtag.magtag import MagTag

jokes = ["We only tell these to our kids to help them learn...really!"]

try:
    from backup_jokes import backup_jokes

    jokes = backup_jokes
except ImportError:
    print("Default backup_jokes.py not found on CIRCUITPY")
    pass


DATA_SOURCE = "https://icanhazdadjoke.com/"

MAGTAG = MagTag()
MAGTAG.peripherals.neopixel_disable = True

MAGTAG.add_text(
    # name
    text_font=terminalio.FONT,
    text_position=(
        7,
        2,
    ),
    text_wrap=30,
    text_anchor_point=(0, 0),
    text_scale=1,
    line_spacing=0.9,
    is_data=False,
)

MAGTAG.add_text(
    text_font=terminalio.FONT,
    text_position=(
        215,
        2,
    ),
    text_anchor_point=(0, 0),
    text_scale=1,
    is_data=False,
)

MAGTAG.add_text(
    text_font=terminalio.FONT,
    text_position=(
        20,
        30,
    ),
    text_wrap=40,
    text_anchor_point=(0, 0),
    text_scale=1,
    line_spacing=1.0,
    is_data=False,
)

MAGTAG.preload_font()  # preload characters

# load random from offline jokes list
# display
# get battery
# wait 5 seconds
# attempt to get new joke from site
# display
# wait 5 seconds and go to deep sleep
# button press should start from top of file?

# press A - wake, press D - lights?

MAGTAG.set_text("Bad-Dad-Joke Machine", 0, False)
MAGTAG.set_text("battery: ---%", 1, False)
try:
    temp = f"battery: {MAGTAG.battery()} V"
    MAGTAG.set_text(temp, 1, False)
except:
    pass

# HACK: mark offline jokes with leading -
joke = "- " + jokes[random.randint(0, len(jokes) - 1)]
MAGTAG.set_text(joke, 2)

# start network after
MAGTAG.network.connect()

while True:
    try:
        print("trying: ", DATA_SOURCE)
        # Get the response and turn it into json
        RESPONSE = MAGTAG.network.requests.get(DATA_SOURCE)
        VALUE = RESPONSE.json()

        # Display the text
        time.sleep(2)
        MAGTAG.set_text(VALUE["joke"], 2)

        # Put the board to sleep for a day
        time.sleep(2)
        # print("Sleeping 1 hour")
        # PAUSE = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60 * 60)
        print("Sleeping 1 minute")
        PAUSE = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60)
        alarm.exit_and_deep_sleep_until_alarms(PAUSE)

    except (ValueError, RuntimeError) as e:
        print("Some error occured, retrying! -", e)
