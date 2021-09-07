# Started from https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard

import json
import time
import random
import alarm
import terminalio
from adafruit_magtag.magtag import MagTag


DATA_SOURCE = "https://icanhazdadjoke.com/"

MAGTAG = MagTag()
MAGTAG.peripherals.neopixel_disable = True

# title
MAGTAG.add_text(
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

# battery
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

# joke
MAGTAG.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(
        5,
        20,
    ),
    text_wrap=34,
    text_anchor_point=(0, 0),
    text_scale=1.0,
    line_spacing=1.0,
    is_data=False,
)

# offline/online
MAGTAG.add_text(
    text_font=terminalio.FONT,
    text_position=(
        205,
        110,
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
deep_sleep = True
while True:
    if loops == 0:
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
        deep_sleep = False
    if MAGTAG.peripherals.button_b_pressed:
        deep_sleep = False
        # MAGTAG.peripherals.neopixel_disable = False
    if MAGTAG.peripherals.button_c_pressed:
        deep_sleep = False
    if MAGTAG.peripherals.button_d_pressed:
        deep_sleep = False

    # A - next
    # B - dont sleep
    # C - lights on/off
    # D - change rate

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
        if deep_sleep:
            alarm.exit_and_deep_sleep_until_alarms(PAUSE)
        else:
            loops = 0
            alarm.light_sleep_until_alarms(PAUSE)

    loops = loops + 1
