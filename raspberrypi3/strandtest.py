# -*- coding: utf-8 -*-
import random
import time
import cv2 as cv
import speech_recognition as sr
from neopixel import *
import transcribe_streaming_mic

# LED strip configuration:
LED_COUNT = 16  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 200  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = 0x00081000  # ws.WS2811_STRIP_GRB   # Strip type and colour ordering


# Define functions which animate LEDs in various ways.

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def helloWorld(strip, wait_ms=20):
    random.seed(time.ctime())
    for i in random.sample(range(64), 64):
        for j in range(8):
            strip.setPixelColor(j * 64 + i, Color(0, 0, 0, 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)


def setAllPixel(c):
    for i in range(512):
        strip.setPixelColor(c)
    strip.show()


def bye_bye(strip, wait_ms=20):
    strip.setAllPixel(0)
    strip.show()
    random.seed(time.ctime())
    for j in random.sample(range(64), 64):
        for k in range(8):
            strip.setPixelColor((7 - k) * 64 + j, Color(0, 0, 0, 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)


def smile(strip, wait_ms=20, iterations=5):
    emo = [18, 21, 25, 27, 28, 30, 32, 39, 45, 42, 51, 52]
    bg = [0, 1, 6, 7, 8, 15, 55, 48, 63, 62, 57, 56]
    for i in range(64):
        strip.setPixelColor(i, 127, 127, 0)  # Yellow
    for i in emo:
        strip.setPixelColor(i, 255, 0, 0)  # red
    for j in range(256 * iterations):
        for i in bg:
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL,
                              LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    language_code = 'ko-KR'  # 한국어로 변경
    while True:
        print('Rainbow animations.')
        rainbow(strip)
        rainbowCycle(strip)
def ij2xy(i,j):
    if i % 2 == 0:
        t = j
    else:
        t = (8 * (i + 1)) - j - 1
    return i,

def ijk2xyz(i,j,k):
    if i % 2 == 0:
        t = j
    else
        t = (8 * (i + 1)) - j - 1
    return i, t, k
'''

ㄹ자 -> 일자 수정식.

if i%2==0
t = k(그대로)
else
t = (8*(i+1))-k-1


k=(0~7)
def func(i,j):
if i%2==0:
t = k
else
t = (8*(i+1))-k-1
return i,t

def func(i,j,k):
if i%2==0:
t = u
else
t = (8*(i+1))-u-1
return i,t,k

func 좌표변환(ijk2xyz)
func(i,j,k) = > x,y,z 사상.
'''