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
    if userInput == "1":
        STEAM_MENU()
    elif userInput == "2":
        WINGE_MENU()
    else:
        print("error")

def STEAM_MENU():
    global GE_PATH
    print("1.Package Manager 2. Flatpak")
    userInput = input("Select your type of steam install: ")
    if userInput == "1":
        temp1 = "/home/" # set the home part of location for concat later
        temp2 = getpass.getuser() # set to the login name of current user
        home_dir = temp1 + temp2 + "/.steam/steam"
        GE_PATH = home_dir + "/compatibilitytools.d/"
        subprocess.call(["mkdir", GE_PATH])
        PROTONGE_MENU()
    elif userInput == "2":
        temp1 = "/home/" # set the home part of location for concat later
        temp2 = getpass.getuser() # set to the login name of current user
        home_dir = temp1 + temp2 + "/.var/app/com.valvesoftware.Steam/data/Steam"
        GE_PATH = home_dir + "/compatibilitytools.d/"
        subprocess.call(["mkdir", GE_PATH])
        PROTONGE_MENU()
    elif userInput == "3":
        test_menu2()
    else:
        print("error")

def WINGE_MENU():
    global GELINK
    global GETARBALL
    global GE_TYPE
    global GE_PATH
    GE_TYPE="wine-lutris"
    with open("menus/winege_menu.txt", "r") as file:
        filedata = file.read()
    print(filedata)

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
    elif userInput == "722":
        from winege import winege722
        GELINK = winege722()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "721":
        from winege import winege721
        GELINK = winege721()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "711":
        from winege import winege711
        GELINK = winege711()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "2":
        print(userInput)
        print("Placeholder")
    else:
        print("error")

def PROTONGE_MENU():
    global GELINK
    global GETARBALL
    global GE_TYPE
    GE_TYPE="Proton"
    with open("menus/protonge_menu.txt", "r") as file:
        filedata = file.read()
    print(filedata)

    userInput = input("Enter an option: ")
    if userInput == "74":
        GE_TYPE = "GE-Proton"
        from protonge import proton74
        GELINK = proton74()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "73":
        GE_TYPE = "GE-Proton"
        from protonge import proton73
        GELINK = proton73()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "731":
        from protonge import protonge731
        GELINK = protonge731()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "722":
        from protonge import protonge722
        GELINK = protonge722()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "721":
        from protonge import protonge721
        GELINK = protonge721()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "712":
        from protonge import protonge712
        GELINK = protonge712()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "711":
        from protonge import protonge711
        GELINK = protonge711()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "7061":
        from protonge import protonge70rc61
        GELINK = protonge70rc61()
        PROCESS_LINK()
        SETUP_GE()
    elif userInput == "0":
        quit()
    else:
        print(error)
        quit()
MENU()
