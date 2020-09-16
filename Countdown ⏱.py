#!/usr/bin/env python3
"""
Created on Wed Sep 16 17:39:11 2020

@author: Phoenix
"""


import time, sys, random

TIME = "\r{:02d}:{:02d}"
ENTER = "Enter time in seconds:\n"
WRONG = "\nWrong input."
TIMEOUT = "TIMEOUT!"
AGAIN = "Start time again? yes/no \n"
NEGATIVE = "\nTime cannot be negative."
WELCOME = "Welcome to Countdown Timer!"
DECORATION = "\n" + "*  " * 25 + "\n"

yes = 'yes y ok continue'
YES = set((yes + yes.upper()).split())
no = 'no n nope exit quit'
NO = set((no + no.upper()).split())
EXIT = ['Thank you!', 'Goodbye!', 'Bye!']

def decorate(x):
    print("\n" + DECORATION)
    print(x)
    print(DECORATION)
def countdown():
    """
    Main function. 
    Ask user input and check it's a positive number.
    Ask user input again if an error occurs eg. cannot be converted to integer.
    Converts to integer (12.1 --> 12, 30.7 --> 30)
    INPUT --> SECONDS to countdown
    ex t = 60 --> 01:00 --> 00:59 --> (...) --> 00:02 --> 00:01 --> 00:00 --> TIMEOUT
    
    """
    try:
         t = int(input(ENTER))
    except:
        print(WRONG)
        countdown()
    if t < 0:
        print(NEGATIVE)
        countdown()
    while t >= 0:
        minute, sec = divmod(t, 60) #seconds to minutes and seconds ex. 90 --> minute = 1, sec = 30
        print(TIME.format(minute, sec), end = '\r') #print time format ex. 04:10. Overwite each line ('\r')
        t -= 1
        time.sleep(1)
    print(TIME.format(minute, sec), end = '\r') 
    decorate(TIMEOUT)
    again()
def again():

    """
    Repeat countdown if input in yes, exit or ask user input again otherwise
    """
    comand = input(AGAIN)
    if comand in YES:
        countdown()
    elif comand in NO:
        sys.exit(random.choice(EXIT)) #exit politely the program :)
    else:
        print(WRONG)
        again()
        
decorate(WELCOME)
countdown()
	
