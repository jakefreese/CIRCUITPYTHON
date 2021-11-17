# save as setup.py
import board
import adafruit_dotstar
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

rgb = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
rgb.brightness = 0.3

a_button = DigitalInOut(board.D4)
a_button.direction = Direction.INPUT
a_button.pull = Pull.UP

b_button = DigitalInOut(board.D3)
b_button.direction = Direction.INPUT
b_button.pull = Pull.UP

def check(token):
    if token == "A":
        return not a_button.value
    if token == "B":
        return not b_button.value
