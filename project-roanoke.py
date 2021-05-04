import os, socket, webbrowser
from requests import get
from pyco import *

titleDir = os.path.join(workingDir, 'titles')
Logger.ClearLog()
Color.INFO = Fore.BRIGHT_CYAN

# Functions
# Main startup screen
def MainDashboard():
    ClearScreenCommand()
    titles = ListFiles(titleDir, 'title-project-roanoke')
    titleColors = [Fore.BRIGHT_CYAN, Fore.BRIGHT_YELLOW, Fore.BRIGHT_GREEN, Fore.BRIGHT_YELLOW, Fore.BRIGHT_GREEN]
    titleNumber = 0
    for title in titles:
        content = open(title, 'r')
        PrintMessage(content.read(), messageColor=titleColors[titleNumber])
        titleNumber += 1

    GetInput()

# Searches for files in a directory matching the filter
def ListFiles(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().startswith(filetype.lower()):
            paths.append(os.path.join(root, file))

   return paths

# Checks that the users input is a valid number between 1-18
def GetInput():
    userInput = UserInput("Please select a program 1-18: ")
    try:
        value = int(userInput)
        if value > 18:
            PrintMessage("Number is greater than 18.", "Error")
            GetInput()

        elif value < 0:
            PrintMessage("Why would you think to use negative numbers? How would that even work?", "Error")
            GetInput()

        elif value == 0:
            PrintMessage("Please enter a number greater than 0.", "Error")
            GetInput()

        # Start of selection elif statments
        # Selection: 1 - Opens web rickroll - Temporary
        elif value == 1:
            PrintMessage("Booting selected program. This may take a second...", "Info")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'))
            webbrowser.get('chrome').open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

        # Selection: 2 - Opens Fern Wifi Cracker - Placeholder
        elif value == 2:
            ClearScreenCommand()
            PrintMessage("Fern Wifi Cracker placeholder")
            UserInput("\nPress enter to continue.")

        # Selection: 10 - Opens the IP Info applet
        elif value == 10:
            IPInfo()

        # Selection: 13 - Opens OSINT Framework - Placeholder
        elif value == 13:
            ClearScreenCommand()
            PrintMessage("OSINT Framework placeholder")
            UserInput("\nPress enter to continue.")

    # If the user enters something they're not supposed to
    except ValueError:
        try:
            value = float(userInput)
            PrintMessage("You're really trying to break my program. Please stop.", "Error")
            GetInput()

        except ValueError:
            PrintMessage("Please enter a number, not a string.", "Error")
            GetInput()

# Network information applet
def IPInfo():
    netInfo = []
    # Returns a list of network names and IP addresses
    # List indexes:
    # 0 = host name
    # 1 = private IP address
    # 2 = public IP address
    def GetIP():
        # Get the hostname of the computer
        PrintMessage("Getting hostname...", "Info")
        hostname = socket.gethostname()
        # Get the private IP address starting with '192.168.'
        PrintMessage("Getting private IP address...", "Info")
        privateIP = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if ip.startswith('192.168.')][:1]
        # Get the public IP address
        PrintMessage("Getting public IP address...", "Info")
        publicIP = get('https://api.ipify.org').text
        netInfo.insert(0, hostname)
        netInfo.insert(1, privateIP[0])
        netInfo.insert(2, publicIP)

    ClearScreenCommand()
    GetIP()
    ClearScreenCommand()
    title = open(os.path.join(titleDir, 'title-ipinfo.txt'))
    PrintMessage(title.read(), messageColor=Fore.BRIGHT_CYAN)
    PrintMessage(f"Your computer name is: {netInfo[0]}")
    PrintMessage(f"Private IP address is: {netInfo[1]}")
    PrintMessage(f"Public IP address is: {netInfo[2]}")
    UserInput("\nPress enter to continue.")
    
if __name__ == '__main__':
    while True:
        MainDashboard()