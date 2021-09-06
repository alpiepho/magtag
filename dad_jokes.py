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
MAGTAG.peripherals.neopixel_disable = False

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
        205,
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
    text_scale=1.0,
    line_spacing=1.0,
    is_data=False,
)

# MAGTAG.preload_font()  # preload characters

MAGTAG.set_text("Bad-Dad-Joke Machine", 0, False)
MAGTAG.set_text("battery: ---%", 1, False)
try:
    batt = MAGTAG.peripherals.battery
    print(batt)
    temp = f"battery: {batt:.2f}V"
    if batt > 4.0:
        temp = f"battery: usb"
    else:
        if batt > 3.7:
            batt = 3.7
        batt = 100 * batt / 3.7
        temp = f"battery: {batt:.2f}%"
    MAGTAG.set_text(temp, 1, False)
except:
    pass

# HACK: mark offline jokes with leading .
joke = "." + jokes[random.randint(0, len(jokes) - 1)]
MAGTAG.set_text(joke, 2)

loops = 0
while True:
    try:
        print("trying: ", DATA_SOURCE)
        MAGTAG.network.connect()
        RESPONSE = MAGTAG.network.requests.get(DATA_SOURCE, headers={"accept": "application/json"})
        VALUE = RESPONSE.json()
        print(VALUE["joke"])

        # leave the backup joke for a minimum time
        time.sleep(60)

        # display the latest joke
        MAGTAG.set_text(VALUE["joke"], 2)

    # except (ValueError, RuntimeError) as e:
    #     print("Some error occured, retrying! -", e)
    except:
        pass

    # put the board to sleep
    print("Sleeping 1 hour")
    PAUSE = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60 * 60)
    alarm.exit_and_deep_sleep_until_alarms(PAUSE)
