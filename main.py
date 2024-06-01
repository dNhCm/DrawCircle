
import pyautogui as ag
import math as m
from time import sleep

from selenium import webdriver


driver: webdriver.Chrome = None


def open_website():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--kiosk')
    driver = webdriver.Chrome(options)

    url = 'https://neal.fun/perfect-circle/'
    driver.get(url)


def draw_circle():
    circle: list[tuple[float, float]] = []

    center = (958, 574)
    r = 400
    delta = 10

    degree = -delta
    for d in range(int((360 / delta) + 1)):
        degree += delta
        rad = m.radians(degree)
        x = m.sin(rad) * r + center[0]
        y = m.cos(rad) * r + center[1]
        circle.append((x, y))

    ag.leftClick(1070, 790)
    sleep(0.6)
    ag.leftClick(*center)
    sleep(0.6)
    for pos in circle:
        ag.mouseDown(*pos, duration=0)
    ag.mouseUp(*circle[-1])


if __name__ == "__main__":
    open_website()
    sleep(3)
    draw_circle()
    sleep(60)
    driver.close()
