import lib.utils.gui as gui

import cv2
import time
import pyautogui

time.sleep(2)

gui.close_app()
gui.open_app()
gui.play_game()
gui.close_chat()
gui.click_api()
gui.start_connection()
gui.close_menu()

region = gui.get_region()
obs = gui.get_obs(region)
cv2.imshow('image', obs)
cv2.waitKey(0)
