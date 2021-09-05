
# Started from https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard

import json
import time
import random
import alarm
import terminalio
from adafruit_magtag.magtag import MagTag

# Set up where we'll be fetching data from
# DATA_SOURCE = (
#     "https://icanhazdadjoke.com/"
# )
DATA_SOURCE = (
    "https://raw.githubusercontent.com/codyogden/killedbygoogle/main/graveyard.json"
)

# Get the MagTag ready
MAGTAG = MagTag()
MAGTAG.peripherals.neopixel_disable = True
# MAGTAG.set_background("/bmps/background.bmp")
## MAGTAG.network.connect()

# google graveyard for positions below
# Prepare the three text fields
#
#  name         description
#  ...          ...
#  ...          ...
#  date         ...
#               ...
#

MAGTAG.add_text(
  # name
    # text_font="/fonts/Deutsch-Gothic-14.bdf",
    text_position=(7, 2,),
    text_wrap=30,
    text_anchor_point=(0, 0),
    text_scale=1,
    line_spacing=0.9,
    is_data=False,
)

MAGTAG.add_text(
    # text_font="/fonts/Deutsch-Gothic-14.bdf",
    text_position=(215, 2,),
    text_anchor_point=(0, 0),
    text_scale=1,
    is_data=False,
)

MAGTAG.add_text(
  # description
    text_font=terminalio.FONT,
    text_position=(20, 30,),
    text_wrap=40,
    text_anchor_point=(0, 0),
    text_scale=1,
    line_spacing=1.0,
    is_data=False,
)

MAGTAG.add_text(
  # description
    text_font=terminalio.FONT,
    text_position=(20, 70,),
    text_wrap=40,
    text_anchor_point=(0, 0),
    text_scale=1,
    line_spacing=1.0,
    is_data=False,
)

MAGTAG.preload_font()  # preload characters

# SONG = (
#     (330, 1),
#     (370, 1),
#     (392, 2),
#     (370, 2),
#     (330, 2),
#     (330, 1),
#     (370, 1),
#     (392, 1),
#     (494, 1),
#     (370, 1),
#     (392, 1),
#     (330, 2),
# )

MAGTAG.set_text("Bad-Dad-Joke Machine", 0, False)

MAGTAG.set_text("battery: ---%", 1, False)

while True:
    try:
        print("trying: ", DATA_SOURCE)
        # Get the response and turn it into json
        # RESPONSE = MAGTAG.network.requests.get(DATA_SOURCE)
        # VALUE = RESPONSE.json()

        VALUE = {}
        VALUE["id"] = "R7UfaahVfFd"
        VALUE["joke"] = "My dog used to chase people on a bike a lot. It got so bad I had to take his bike away."
        VALUE["status"] = 200
        # print(VALUE)

        # # Choose a random project to display
        # PROJECT = VALUE[random.randint(0, len(VALUE) - 1)]

        # # Prepare the text to be displayed
        # CLOSED = PROJECT["dateClose"].split("-")
        # CLOSED.reverse()
        # CLOSED = "/".join(CLOSED)

        # print(PROJECT["name"])

        # Display the text
        # MAGTAG.set_text(PROJECT["name"], 0, False)
        # MAGTAG.set_text(CLOSED, 1, False)
        # MAGTAG.set_text(PROJECT["description"], 2)
        parts = VALUE["joke"].split(".")

        MAGTAG.set_text(parts[0], 2, False)
        MAGTAG.set_text(parts[1], 3)

        # # Play a song
        # for notepair in SONG:
        #     MAGTAG.peripherals.play_tone(notepair[0], notepair[1] * 0.2)

        # Put the board to sleep for an hour
        time.sleep(2)
        print("Sleeping")
        PAUSE = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60 * 60)
        alarm.exit_and_deep_sleep_until_alarms(PAUSE)

    except (ValueError, RuntimeError) as e:
        print("Some error occured, retrying! -", e)
