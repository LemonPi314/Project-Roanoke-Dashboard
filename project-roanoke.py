# Imports needed to use this code
import os, requests, socket, webbrowser
from requests import get
from PythonTools import *

# Attempt at making the PythonTools library be downloaded from GitHub
#from httpimport import github_repo
#with github_repo("Duplexes", "PythonTools"):
#    from PythonTools import PythonTools

titleDir = os.path.join(projectDir, "titles")

# Functions
# Main startup screen
def MainDashboard():
    ClearScreen()
    titles = ListFiles(titleDir, "title-project-roanoke")
    titleColors = [BrightCyan, BrightYellow, BrightGreen, BrightYellow, BrightGreen]
    titleNumber = 0
    for title in titles:
        content = open(title)
        PrintMessage(content.read(), "none", titleColors[titleNumber])
        titleNumber += 1

    UserInput()

# Clears the console screen
def ClearScreen():
    if os.name == "posix":
        os.system("clear")
    else:
       os.system("cls")

# Searches for files in a directory matching the filter
def ListFiles(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().startswith(filetype.lower()):
            paths.append(os.path.join(root, file))
   return(paths)

# Checks that the users input is a valid number between 1-18
def UserInput():
    user_input = input("Please select a program 1-18: ")
    try:
        value = int(user_input)
        if value > 18:
            PrintMessage("Number is greater than 18.", "error")
            UserInput()
        elif value < 0:
            PrintMessage("Why would you think to use negative numbers? How would that even work?", "error")
            UserInput()
        elif value == 0:
            PrintMessage("Please enter a number greater than 0.", "error")
            UserInput()

        # Start of selection elif statments
        # Selection: 1 - Opens web rickroll - TEMPORARY
        elif value == 1:
            PrintMessage("Booting selected program. This may take a second...")
            webbrowser.register("chrome",
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get("chrome").open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        # Selection: 2 - Opens Fern Wifi Cracker - Placeholder 
        elif value == 2:
            ClearScreen()
            PrintMessage("Fern Wifi Cracker Placeholder")
            input("Press ENTER to continue.")

        # Selection: 10 - Opens the IP Info applet 
        elif value == 10:
            IPInfo()

    # If the user enters something they"re not supposed to
    except ValueError:
        try:
            value = float(user_input)
            PrintMessage("You're really trying to break my program. Please stop.", "error")
            UserInput()

        except ValueError:
            PrintMessage("Please enter a number, not a string.", "error")
            UserInput()

# Network information applet
def IPInfo():
    netInfo = []

    # Returns a list of network names and IP addresses
    # List indexes:
    # 0 = hostname
    # 1 = private IP address
    # 2 = public IP address
    def GetIP():
        # Get the hostname of the computer
        hostname = socket.gethostname()
        # Get the private IP address starting with "192.168."
        privateIP = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if ip.startswith("192.168.")][:1]
        # Get the public IP address
        publicIP = get("https://api.ipify.org").text
        netInfo.insert(0, hostname)
        netInfo.insert(1, privateIP[0])
        netInfo.insert(2, publicIP)

    ClearScreen()
    GetIP()
    title = open(os.path.join(titleDir, "title-ipinfo.txt"))
    PrintMessage(title.read(), "none", BrightCyan)
    PrintMessage("Your computer name is: " + netInfo[0])
    PrintMessage("Private IP address is: " + netInfo[1])
    PrintMessage("Public IP address is: " + netInfo[2])
    input("Press ENTER to continue.")
    
# Fixes a weird bug in Windows command line to allow printing of colors. 
ClearScreen()
PrintMessage("hello World", "customprefix", BrightBlue)

while(1):
    MainDashboard()