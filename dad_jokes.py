# Started from https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard

# import board
# import json
import time
import random
import alarm
import terminalio
from adafruit_magtag.magtag import MagTag


DATA_SOURCE = "https://icanhazdadjoke.com/"

MAGTAG = MagTag(status_neopixel=None)
MAGTAG.peripherals.neopixel_disable = False

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
        215,
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
sleep_level = 1

while True:
    if (loops % 600) == 0:
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
        MAGTAG.set_text(f'', 3)

    time.sleep(0.1)

    # check for buttons during 1st minute
    if MAGTAG.peripherals.button_a_pressed:
        MAGTAG.set_text(f'next...', 3)
        loops = -1

    if MAGTAG.peripherals.button_b_pressed:
        sleep_level = sleep_level + 1
        if sleep_level > 2:
            sleep_level = 0
        if sleep_level == 0:
            MAGTAG.set_text(f'sleep: none', 3)
        if sleep_level == 1:
            MAGTAG.set_text(f'sleep: 1min', 3)
        if sleep_level == 2:
            MAGTAG.set_text(f'sleep: 10min', 3)

    # if MAGTAG.peripherals.button_c_pressed:
    #     MAGTAG.set_text(f'button C', 3)
    #     print("C")

    # if MAGTAG.peripherals.button_d_pressed:
    #     MAGTAG.set_text(f'button D', 3)
    #     print("D")

    if loops > 0 and (loops % 600) == 0:
        try:
            print("trying: ", DATA_SOURCE)
            MAGTAG.network.connect()
            RESPONSE = MAGTAG.network.requests.get(DATA_SOURCE, headers={"accept": "application/json"})
            VALUE = RESPONSE.json()
            print(VALUE["joke"])
            MAGTAG.set_text(VALUE["joke"], 2, False)
            count = count + 1
            MAGTAG.set_text(f'online: {count}', 3)

        except Exception as e:
            print("Some error occured, retrying! -", e)

        # put the board to sleep
        if sleep_level == 1:
            loops = 0
            print("Sleeping 1 minute")
            PAUSE = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60)
            MAGTAG.peripherals.neopixel_disable = True
            alarm.light_sleep_until_alarms(PAUSE)
            MAGTAG.peripherals.neopixel_disable = False
            # BUTTONA = alarm.touch.TouchAlarm(pin=board.BUTTON_A)
            # BUTTONB = alarm.touch.TouchAlarm(pin=board.BUTTON_B)
            # BUTTONC = alarm.touch.TouchAlarm(pin=board.BUTTON_C)
            # BUTTOND = alarm.touch.TouchAlarm(pin=board.BUTTON_D)
            # alarm.light_sleep_until_alarms(PAUSE, BUTTONA, BUTTONB, BUTTONC, BUTTOND)
        if sleep_level == 2:
            print("Sleeping 10 minutes")
            PAUSE = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60 * 10)
            MAGTAG.peripherals.neopixel_disable = True
            alarm.exit_and_deep_sleep_until_alarms(PAUSE)

    loops = loops + 1
