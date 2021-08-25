import time
import pyautogui as pg
import random

time.sleep(5)
print("running...")
wait = 5
def press_space():
    pg.press('space')
    print("pressed space")
    time.sleep(wait)

def press_a():
    pg.write('a')
    print("pressed a")
    time.sleep(wait)

def type_virus():
    pg.write("Virus!! Virus!!" , 0.0005)
    print("said virus!! virus!!")
    time.sleep(wait)



def close():
    pg.hotkey("alt", 'f4')
    print("pressed alt+f4")
    time.sleep(wait)

def run():
    pg.hotkey("win" , 'r')
    print("opend run")
    time.sleep(wait)

def sleeping():
    waiting_time = random.randint(5,20)
    print('sleeping for '+ str(waiting_time) + ' seconds')
    time.sleep(waiting_time)

func_list = [press_space , press_a , close, run, sleeping,type_virus]



while True:
    mouse_x = pg.position()[0]
    if mouse_x != 0:
        random.choice(func_list)()
        
    if mouse_x == 0:
        print("paused")
 
