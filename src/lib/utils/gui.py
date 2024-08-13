import pyautogui
import numpy
import cv2
import time
import subprocess

GAME_LEFT_W = 500
GAME_RIGHT_W = 0
GAME_WIDTH = GAME_LEFT_W + GAME_RIGHT_W
GAME_HEIGHT = 500
app_path = '/Users/peterchau/Desktop/Botomy.app'
play_location = (965, 502)
chat_location = (343, 662)
api_location = (936, 264)
menu_location = (828, 263)

def close_app():
    with pyautogui.hold('command'):
        pyautogui.press('q')
    time.sleep(4)

def open_app():
    subprocess.run(['open', app_path])
    time.sleep(4)

def play_game():
    pyautogui.click(play_location)
    time.sleep(1)

def close_chat():
    pyautogui.click(chat_location)
    time.sleep(.5)

def click_api():
    pyautogui.click(api_location)
    time.sleep(.5)

def start_connection():
    with pyautogui.hold('command'):
        pyautogui.press('r')
    time.sleep(.5)

def close_menu():
    pyautogui.click(menu_location)
    time.sleep(.5)

def get_region():
    res = pyautogui.size()
    x_start = (res[0] // 2) - (GAME_LEFT_W) - 13
    y_start = (res[1] // 2) - (GAME_HEIGHT // 2) - 20
    return (x_start, y_start, GAME_LEFT_W + GAME_RIGHT_W, GAME_HEIGHT)


def get_obs(region):
    im1 = pyautogui.screenshot(region=region)
    frames = numpy.array(im1)
    frames_RGB = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
    im = numpy.moveaxis(frames_RGB, -1, 0)
    return im
