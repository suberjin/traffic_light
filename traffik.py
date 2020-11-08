from termcolor import colored
from time import sleep
import subprocess

red_counter = 3
green_counter = 3
blinking_green = 2
yellow_counter = 2

def set_color(color,mode):
  if mode == "on":
    print(colored(f'I am {color} light', color))
  if mode == "off":
    print("\r", end='', sep='')


while True:
  subprocess.call("clear")
  set_color("red","on")
  sleep(red_counter)
  set_color("yellow","on")
  sleep (1)
  set_color("red","off")
  subprocess.call("clear")
  set_color("green","on")
  sleep(green_counter)
  set_color("green","off")
  subprocess.call("clear")
  for i in range(blinking_green):
    sleep(0.5)
    set_color("green","on")
    sleep(0.5)
    set_color("green","off")
    subprocess.call("clear")
  set_color("yellow","on")
  sleep(yellow_counter)
  set_color("yellow","off")
