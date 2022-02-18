#! /usr/bin/env python3

import subprocess
import os
import re
def Checkroot():
    who = subprocess.check_output('whoami')
    chuser = re.search(r"root", str(who))
    if chuser:
        verifywus = input("\n [Verifying] --> The XEye-tp tool needs to run with root user not only running with \"sudo\". Are you running your shell as root? [yes / no] " )
        if verifywus.lower() == 'y' or verifywus.lower() == 'yes':
            Start()
        elif verifywus.lower() == 'n' or verifywus.lower() == 'no':
            print(" [Instruction] --> Please run \"sudo su\" command, enter the password for the current user to change to root with the pwd, then run the tool again :) \n")
        else:
            print(" [warning] --> Invalid entry, please use a yes or no answer, Exiting .....")
            exit()
    else:
        print("\n\n [Warning] --> You are not root - Please read and follow the instructions below: \n ")
        print("\n [Instruction] --> 1- Please run the XEye-tp tool with root user not only with \"sudo\" to configure your adapter with no issues. ")
        print(" [Instruction] --> 2- Run \"sudo su\" command then enter the password for the current user to change to root with the pwd, then run the tool again :) \n")
def Start():
    print("\n **********************************************************************************************************************************************************")
    print("\n [Welcoming] --> Welcome to XEye-tp tool :):):) \n\n")
    print(" [Info] --> With XEye-tp tool, you can do the following: \n")
    print(" \t[*] --> 1) Change your Wifi USB adapter TP-Link model WN722N v2 and v3 to Monitor and Injection mode easily and in few minutes or even seconds :) ")
    print(" \t[*] --> 2) You can easily change the Mac address after your TP-Link Wifi USB is set to monitor mode :) ")
    print(" \t[*] --> 3) Make sure to clone the tool again once each week as we are updating the tool and adding more features regularly :):)\n")
    
    ifconfig_outp = subprocess.check_output('iwconfig')
    chwlan = re.search(r"WIFI@REALTEK", str(ifconfig_outp))
    chwlann = re.search(r"Mode:Auto", str(ifconfig_outp))
    chwlannn = re.search(r"Mode:Monitor", str(ifconfig_outp))
    if chwlannn:
        lines()
        print("\n [Info] --> Your Wifi USB adapter is already set to Monitor mode ")
        Asking = input("\n [Asking] --> Would like to change your adapter Mac address? [yes / no] ")
        lines()
        if Asking.lower() == 'y' or Asking.lower() == 'yes':
            Usermd()
        elif Asking.lower() == 'n' or Asking.lower() == 'no':
            lines()
            print("\n [*] --> Thanks for using XEye-tp tool, Your Adapter is just set to Monitor mode - Bye bye .....\n")
            lines()
        else:
            lines()
            print(" [warning] --> Invalid entry, please use a yes or no answer, Exiting .....")
            lines()
            exit()
    elif chwlann:
        lines()
        print("\n [Info] --> Your Wifi USB adapter is already set to Auto mode ")
        asking = input(" [Permission] --> Would you like to set your Wifi USB adapter to \"Monitor mode now\" or \"reconfigure\"?  [set / reconf] ")
        lines()
        if asking.lower() == 'set':
           tp_set()
        elif asking.lower() == 'reconf':
           tp_conf()
        else:
           lines()
           print(" [Warning] --> Invalid Entry. [Your interface is just set to Auto mode]   Exiting .....")
           lines()
           exit()
    elif chwlan:
        usermd()
    else:
        lines()
        print("\n [Warning] --> Please make sure that the Wifi USB is plugged in, Bye bye ...... ")
        exit()
    TheEnd()
def usermd():
    lines()
    sque= input("\n [Permission] --> Would you like to proceed? [yes / no] ")
    lines()
    if sque.lower() == 'y' or sque.lower() == 'yes':
        tp_conf()
    elif sque.lower() == 'n' or sque.lower() == 'no':
        lines()
        print("\n [*] --> Thanks for using XEye-tp tool, Exiting .....\n")
        lines()
    else:
        lines()
        print(" [warning] --> Invalid entry, please use a yes or no answer, Exiting .....")
        lines()
        exit()

def tp_conf():
    lines()
    print("\n [*] --> Updating your system, please wait ....  \n")
    lines()
    subprocess.call(['apt', 'update', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing build-essentials, Please wait ....  \n")
    lines()
    subprocess.call(['apt', 'install', 'build-essential', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing bc, Won't take too long :) ....  \n")
    lines()
    subprocess.call(['apt', 'install', 'bc', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing libelf-dev, Please wait ....  \n")
    lines()
    subprocess.call(['apt', 'install', 'libelf-dev', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing the required linux-headers, Please wait .....  \n")
    lines()
    subprocess.call("apt install linux-headers-$(uname -r)", shell=True)
    lines()
    print("\n [*] --> Removing \"r8188eu.ko module\"  \n")
    subprocess.call(['rmmod', 'r8188eu.ko'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Git cloning \"rtl8188eus\"  \n")
    lines()
    unamer = subprocess.check_output(['uname','-r'])
    unamerr = re.search(r"5.1", str(unamer))
    if unamerr is not None:
        subprocess.call(['git', 'clone', 'https://github.com/drygdryg/rtl8188eus.git'], stdout=subprocess.DEVNULL)
    else:
        subprocess.call(['git', 'clone', 'https://github.com/aircrack-ng/rtl8188eus'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing dkms  \n")
    subprocess.call(['apt', 'install', 'dkms'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Done installing dkms. proceeding further ....  \n")
    os.chdir("rtl8188eus")
    lines()
    print("\n [*] --> Echoing \"blacklist r8188eu.ko\" to \"realtek.conf\"  \n")
    subprocess.call("echo \"blacklist r8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)
    lines()
    print("\n [*] --> Running Make command, Will take few minutes, please wait and ignore the upcoming errors and warnings ......  \n")
    lines()
    subprocess.call(['sudo', 'make'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Running Make Install command  \n")
    lines()
    subprocess.call(['sudo', 'make', 'install'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Running \"modprobe 8188eu\"  \n")
    lines()
    subprocess.call("sudo modprobe 8188eu", shell=True)
    iwco = subprocess.check_output(['iwconfig'])
    Auto_check = re.search(r"Mode:Auto", str(iwco))
    if not Auto_check:
        lines()
        print("\n [Warning] --> The Wifi adapter mode is not Auto or it is just missing. ")
        print(" [Instruction] --> UnPlug and plug in your Wifi USB adapter, wait for few seconds then run the tool again with root - Bye bye :)   \n")
        lines()
        exit()
    if Auto_check.group(0) == 'Mode:Auto':
        lines()
        print("\n [Congrats] --> The Wifi USB adapter is successfully configured \n")
        asking = input("\n [Permission] --> Would you like to set your Wifi USB adapter to Monitor mode now?  [yes / no] ")
        lines()
        if asking.lower() == 'y' or asking.lower() == 'yes':
            tp_set()
        elif asking.lower() == 'n' or asking.lower() == 'no':
            lines()
            print("\n [Info] --> Now your adapter is just set to Auto mode - Bye Bye :) \n")
            TheEnd()
        else:
            lines()
            print("\n [Warning] --> Invalid Entry. [Your interface is just set to Auto mode] - Exiting .....\n")
            exit()
def tp_set():
    interf = getinterf()
    subprocess.call(['ifconfig', interf, 'down'])
    subprocess.call("airmon-ng check kill", shell=True)
    subprocess.call(['iwconfig', interf, 'mode', 'monitor'])
    subprocess.call(['ifconfig', interf, 'up'])
    tp_check()
def tp_check():
    iwcon = subprocess.check_output(['iwconfig'])
    iwcon_Mcheck = re.search(r"Monitor",str(iwcon))
    if iwcon_Mcheck.group(0) == "Monitor":
        lines()
        print("\n [Congrats] --> You wireless USB has been set to monitor mode :) :) \n")
        Asking = input("\n [Asking] --> Would like to change your adapter Mac address? [yes / no] ")
        if Asking.lower() == 'y' or Asking.lower() == 'yes':
            Usermd()
        elif Asking.lower() == 'n' or Asking.lower() == 'no':
            lines()
            print("\n [*] --> Thanks for using XEye-tp tool, Your Adapter is just set to Monitor mode - Bye bye :) .....\n")
        else:
            lines()
            print(" [warning] --> Invalid entry, please use a yes or no answer, Exiting .....")
            exit()
    else:
        lines()
        print("\n [Failure] --> Sorry :( , your Wifi USB could not be changed to monitor mode ")
        print("\n [Instruction] --> Upgrade and Restart your system then run the tool again ")
        exit()
def Usermd():
    Interface = getinterf()
    lines()
    Mac = input("\n        [Required] --> Enter the required Mac address: ")
    if not Mac:
        print(" \n [Warning] --> No Mac address specified. ")
        print(" \n [Info] Now your adapter is just set to monitor mode - Bye bye .....")
        TheEnd()
    Macc1 = getmac(Interface)
    if Macc1 == Mac:
        print(" \n [Info] --> You just entered the same Mac address for " + Interface + ", please enter a different Mac address - Exiting ...... ")
        exit()
    ChMac(Interface, Mac)
    Macc2 = getmac(Interface)
    if (Macc2 == Mac) or (Macc1 != Macc2):
        print(" [Done] --> The Mac address is changed successfully to " + Mac)
        TheEnd()
    else:
        print(" [Warning] --> Something Went wrong, The Mac address couldn't change to "+Mac)
        print("\n [Instruction] --> Enter a valid Mac address, or unplug then plug in you adapter, wait for few seconds then run the tool again - Bye bye :) ")
        exit()

def ChMac(Interface,Mac):
    lines()
    print("\n [Info] --> XEye-tp is setting your " + Interface + " Mac address to " + Mac)
    lines()
    subprocess.call(["ifconfig", Interface, "down"])
    subprocess.call(["iwconfig", Interface, "mode", "Auto"])
    subprocess.call(["ifconfig", Interface, "hw", "ether", Mac])
    subprocess.call(["iwconfig", Interface, "mode", "Monitor"])
    subprocess.call(["ifconfig", Interface, "up"])

def getinterf():
    interfs = subprocess.check_output('iwconfig')
    interf = re.search(r"\w\w\w\w\d", str(interfs))
    interff = re.search(r"\w\w\w\d", str(interfs))
    Interff = re.search(r"WIFI@REALTEK", str(interfs))
    if interf and Interff:
        return interf.group(0)
    elif interff and Interff:
        return interff.group(0)
    else:
        lines()
        print(" [Warning] --> Couldn't read your adapter, please make sure that your adapter is plugged in or simply replug it then run the tool again - Exiting .......")
        exit()
def getmac(interface):
    ifconfgi_re = subprocess.check_output(["ifconfig", interface])
    testing1 = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfgi_re))
    testing2 = re.search(r"\w\w-\w\w-\w\w-\w\w-\w\w-\w\w", str(ifconfgi_re))
    if testing1:
        return testing1.group(0)
    elif testing2:
        mvalue = testing2.group(0)
        Mvalue = re.sub('-',':',mvalue)
        return Mvalue
    else:
        lines()
        print("\n [Warning] --> Please make sure that your adapter is plugged in, then run the tool again and use the set option. - Exiting ..... ")
        exit()
def lines():
    print("-------------------------------------------------------------------------------------------------------")
def TheEnd():
    lines()
    print("\n [Recommendation] --> Run the \"exit\" command to exit the root shell, and stay secure :) ")
    print(" [Recommendation] --> The Facebook OSINT Hacking course: https://www.udemy.com/course/facebook-osint-hacking/?referralCode=1FEF1A87D703B6DAE484")
    print(" [Recommendation] --> The Linux cmd course: https://www.udemy.com/course/linux-command-lines-from-a-hackers-perspective/?referralCode=62A07A01780C21117592")
    print(" [Recommendation] --> Make sure to clone the tool once a week as we are updating the tool and adding more features regularly ")
    lines()
    print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert and \"XEye\" founder.")
    exit()
Checkroot()
