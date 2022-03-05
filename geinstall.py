import subprocess
import os.path
import getpass

GELINK=""
GETARBALL=""
STEAM_INSTALL_TYPE=""
GE_PATH=""
GE_TYPE=""


def PROCESS_LINK():
    global GELINK
    global GETARBALL
    global GE_TYPE
    print(GELINK)
    link = GELINK
    #start_pos = link.index("Proton")
    start_pos = link.index(GE_TYPE)
    end_pos = len(link)
    GETARBALL = link[start_pos:end_pos]

def SETUP_GE():
    global GELINK
    global GETARBALL
    global GE_PATH
    subprocess.call(["wget", GELINK])
    subprocess.call(["tar", "-xvf", GETARBALL, "-C", GE_PATH])
    subprocess.call(["rm", GETARBALL])

def MENU():
    print("1. Steam 2. Lutris")
    userInput = input("Select an option: ")
    if userInput == '1':
        STEAM_MENU()
    elif userInput == '2':
        WINGE_MENU()
    else:
        print("error")

def STEAM_MENU():
    global GE_PATH
    print("1.Package Manager 2. Flatpak")
    userInput = input("Select your type of steam install: ")
    if userInput == '1':
        temp1 = "/home/" # set the home part of location for concat later
        temp2 = getpass.getuser() # set to the login name of current user
        home_dir = temp1 + temp2 + "/.steam/steam"
        GE_PATH = home_dir + "/compatibilitytools.d/"
        subprocess.call(["mkdir", GE_PATH])
        PROTONGE_MENU()
    elif userInput == '2':
        temp1 = "/home/" # set the home part of location for concat later
        temp2 = getpass.getuser() # set to the login name of current user
        home_dir = temp1 + temp2 + "/.var/app/com.valvesoftware.Steam/data/Steam"
        GE_PATH = home_dir + "/compatibilitytools.d/"
        subprocess.call(["mkdir", GE_PATH])
        PROTONGE_MENU()
    else:
        print("error")

def WINGE_MENU():
    global GELINK
    global GETARBALL
    global GE_TYPE
    global GE_PATH
    GE_TYPE="wine-lutris"
    print("Select WineGE Version")
    print("72. Wine-GE-Proton7-2")
    print("71. Wine-GE-Proton7-1")
    print("722. Wine-7.2-GE-2")
    print("721. Wine-7.2-GE-1  711. Wine-7.1-GE-1")
    print("0. Exit")

    temp1 = "/home/" # set the home part of location for concat later
    temp2 = getpass.getuser() # set to the login name of current user
    home_dir = temp1 + temp2 + "/.local/share/lutris/runners/wine/"
    GE_PATH = home_dir
    subprocess.call(["mkdir", GE_PATH])
    
    userInput = input("Enter an option: ")
    if userInput == "72":
        from winege import winege72
        GELINK = winege72()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "71":
        from winege import winege71
        GELINK = winege71()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == '722':
        from winege import winege722
        GELINK = winege722()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == '721':
        from winege import winege721
        GELINK = winege721()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == '711':
        from winege import winege711
        GELINK = winege711()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == '2':
        print(userInput)
        print("Placeholder")
    else:
        print("error")

def PROTONGE_MENU():
    global GELINK
    global GETARBALL
    global GE_TYPE
    GE_TYPE="Proton"
    print("Select Proton Version")
    print("74. GE-Proton7-4")
    print("73 GE-Proton7-3")
    print("731 Proton-7.3-GE-1")
    print("722 Proton-7.2-GE-2") 
    print("721. Proton-7.2-GE-1")
    print("712. Proton-7.1-GE-2") 
    print("711. Proton-7.1-GE-1")
    print ("7061. Proton-7.0rc6-GE-1")
    print("0. Exit")

    userInput = input("Enter an option: ")
    if userInput == "76":
        GELINK = "https://github.com/GloriousEggroll/proton-ge-custom/releases/download/GE-Proton7-6/GE-Proton7-6.tar.gz"
        GETARBALL = "GE-Proton7-6.tar.gz"
        SETUP_GE()
    elif userInput == "74":
        from protonge import proton74
        GELINK = "https://github.com/GloriousEggroll/proton-ge-custom/releases/download/GE-Proton7-4/GE-Proton7-4.tar.gz"
        GETARBALL = "GE-Proton7-4.tar.gz"
        SETUP_GE()
    elif userInput == "73":
        GE_TYPE = "GE-Proton"
        from protonge import proton73
        GELINK = "https://github.com/GloriousEggroll/proton-ge-custom/releases/download/GE-Proton7-3/GE-Proton7-3.tar.gz"
        GETARBALL = "GE-Proton7-3.tar.gz"
        SETUP_GE()
    elif userInput == "731":
        from protonge import protonge731
        GELINK = "https://github.com/GloriousEggroll/proton-ge-custom/releases/download/7.3-GE-1/Proton-7.3-GE-1.tar.gz"
        GETARBALL = "Proton-7.3-GE-1.tar.gz"
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == '722':
        from protonge import protonge722
        GELINK = protonge722()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == '721':
        from protonge import protonge721
        GELINK = protonge721()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == '712':
        from protonge import protonge712
        GELINK = protonge712()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == '711':
        from protonge import protonge711
        GELINK = protonge711()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == '7061':
        from protonge import protonge70rc61
        GELINK = protonge70rc61()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == '0':
        quit()
    else:
        print(error)
        quit()
MENU()
