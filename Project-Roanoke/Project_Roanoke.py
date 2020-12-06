import webbrowser
import os
import requests
from requests import get
import socket

#Fixes weird bug in windows command line to allow printing of colors. 
os.system('cls')


 #Functions 
#Checks thats the users input is a valid number between 1 - 10
def userinput():
    user_input = input("Please select a program 1- 10: ")
   

    try:
        val = int(user_input)
        if val > 10:
            print("\u001b[31mNumber is greater then 10.\u001b[0m")
            userinput()
        elif val < 0:  
            print("\u001b[31mWhy would you think to use negative numbers? How would that even work.\u001b[0m")
        elif val == 0:
            print("\u001b[31mPlease use a number greator then 1.\u001b[0m")
            userinput()

        #Start of selection elif statments. This 

        #Selection: 1 - Opens web rickroll - TEMP 
        elif val == 1:
            print("\u001b[32mBooting selected program this may take a second...\u001b[0m")
            webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        #Selection: 2 - Opens Fern Wifi Cracker - Placeholder 
        elif val == 2:
            print("Fern Wifi Cracker PlaceHolder")
        #Selection: 10 - Opens the IP info applet 
        elif val == 10: 
            ipinfo()
    #If a user enters somthing there not supposed to this runs. 
    except ValueError:
        try:
            val = float(user_input)
            print("\u001b[31mYour really trying to break my program please stop.\u001b[0m")
            userinput()
        except ValueError:
            print("\u001b[31mPlease enter a number, not a string.\u001b[0m")
            userinput()

#Gets information about public ip adress and private IPv4 adress. 
def ipinfo():
    os.system('cls')
    publicip = get('https://api.ipify.org').text
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("""\u001b[36;1m
  _____ _____ _____        __      
 |_   _|  __ \_   _|      / _|     
   | | | |__) || |  _ __ | |_ ___  
   | | |  ___/ | | | '_ \|  _/ _ \ 
  _| |_| |    _| |_| | | | || (_) |
 |_____|_|   |_____|_| |_|_| \___/ 
                                   
                                   
    \u001b[33m""")
    print("Your computer name is: " + hostname)
    print('Public IPv4 address is: {}'.format(publicip))
    print("Local IPv4 address is: " + local_ip)
    input("Press enter to contiune.")
    



def maindashboard():
    if os.name =='posix':
        os.system('clear')
    else:
       os.system('cls')
    print("""\u001b[36;1m
      _____           _           _      _____                         _         
     |  __ \         (_)         | |    |  __ \                       | |        
     | |__) | __ ___  _  ___  ___| |_   | |__) |___   __ _ _ __   ___ | | _____  
     |  ___/ '__/ _ \| |/ _ \/ __| __|  |  _  // _ \ / _` | '_ \ / _ \| |/ / _ \ 
     | |   | | | (_) | |  __/ (__| |_   | | \ \ (_) | (_| | | | | (_) |   <  __/ 
     |_|   |_|  \___/| |\___|\___|\__|  |_|  \_\___/ \__,_|_| |_|\___/|_|\_\___| 
                    _/ |                                                         
                   |__/                                                                        
    """)







    print("""
    \u001b[33mWireless Atacks           Password Attacks          Database Attacks\u001b[32m
    (1)Airgeddon              (4)                       (7)
    (2)Fern Wifi Cracker      (5)                       (8)
    (3)                       (6)                       (9)
    \u001b[33mNetworking Tools          OSINT Tools               Exploitation Tools\u001b[32m
    (10)Ip Info Applet        (13)OSINT Framework       (16)
    (11)                      (14)                      (17)
    (12)                      (15)                      (18)
    """)
    userinput()
while(1):
    maindashboard()
    
