#!/usr/bin/env python

import time
import detective as det
import fantasy as fan
import scifi as sci

player_name = raw_input("Enter your name:")

def begin():
    begin_op = ["1","2","3"]
    user_choice = ""
    print "Hello " + player_name + "!"
    time.sleep(1)
    print "Please select from the following options: \n 1: Fantasy \n 2: Sci-Fi \n 3: Detective"
    user_choice = raw_input()
    if user_choice == begin_op[0]:
        fan.fan_start(player_name)
        return gameover()
    elif user_choice == begin_op[1]:
        sci.sci_start(player_name)
        return gameover()
    elif user_choice == begin_op[2]:
        det.det_start(player_name)
        return gameover()
    else:
        fan.clr()
        print "Try again!"

#fantasy.py created by Kevin Boyle
#scifi.py created by Cian O'Donoghue
#index.py and detective.py created by Ben Strickland

def gameover():
    start_op = ["y","n"]
    print "Game Over. Try Again? \n (Y/N)"
    user_choice = raw_input("Enter Option:").lower().strip()
    if user_choice in start_op:
        if user_choice != start_op[0]:
            print "Thanks for playing!"
            return "done"

attempt = "start"
while attempt != "done":
    attempt = begin()
