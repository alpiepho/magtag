# Started from https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard

import json
import time
import random
import alarm
import terminalio
from adafruit_magtag.magtag import MagTag


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

MAGTAG.add_text(
    text_font=terminalio.FONT,
    text_position=(
        20,
        90,
    ),
    text_wrap=40,
    text_anchor_point=(0, 0),
    text_scale=1.0,
    line_spacing=1.0,
    is_data=False,
)
MAGTAG.preload_font()  # preload characters

MAGTAG.set_text("Bad-Dad-Joke Machine", 0, False)
MAGTAG.set_text("battery: ---%", 1, False)

loops = 0
count = 0
while True:
    if count == 0:
        try:
            batt = MAGTAG.peripherals.battery
            print(batt)
            batt = min(batt, 4.2)
            batt = 100 * batt / 4.2
            MAGTAG.set_text(f"battery: {batt:.2f}%", 1, False)
        except:
            pass
        jokes = ["We only tell these to our kids to help them learn...really!"]
        try:
            from backup_jokes import backup_jokes
            jokes = backup_jokes
        except ImportError:
            print("Default backup_jokes.py not found on CIRCUITPY")
            pass
        joke = jokes[random.randint(0, len(jokes) - 1)]
        MAGTAG.set_text(joke, 2, False)
        MAGTAG.set_text(f'(offline)', 3)

    # leave the backup joke for a minimum time
    time.sleep(1)

    # check for buttons during 1st minute
    if MAGTAG.peripherals.button_a_pressed:
        pass
    # A - next
    # B - dont sleep
    # C - lights on/off
    # D - ???

    if loops >= 60:
        try:
            print("trying: ", DATA_SOURCE)
            MAGTAG.network.connect()
            RESPONSE = MAGTAG.network.requests.get(DATA_SOURCE, headers={"accept": "application/json"})
            VALUE = RESPONSE.json()
            print(VALUE["joke"])
            MAGTAG.set_text(VALUE["joke"], 2, False)
            count = count + 1
            MAGTAG.set_text(f'(online: {count})', 3)

        # except (ValueError, RuntimeError) as e:
        #     print("Some error occured, retrying! -", e)
        except:
            pass

        # put the board to sleep
        print("Sleeping 10 minutes")
        PAUSE = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60 * 10)
        alarm.exit_and_deep_sleep_until_alarms(PAUSE)
    loops = loops + 1
