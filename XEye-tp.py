#! /usr/bin/env python3

import subprocess
import os
import re
def Checkroot():
    who = subprocess.check_output('whoami')
    chuser = re.search(r"root", str(who))
    if chuser:
        verifywus = input("\n [Verifying] --> The tool needs to run with root user not only running with \"sudo\". Are your running your shell as root? [yes / no] " )
        if verifywus.lower() == 'y' or verifywus.lower() == 'yes':
            Checkexis()
        elif verifywus.lower() == 'n' or verifywus.lower() == 'no':
            print(" [Instruction] --> Please run \"sudo su\" command then enter the password for the current user to change to root with the present directory, then run the tool again :) \n")
        else:
            print(" [warning] --> Invalid entry, please use a yes or no answer, Exiting .....")
            exit()
    else:
        print("\n\n [Warning] --> You are not root - Please read and follow the instructions below: \n ")
        print("\n [Instruction] --> 1- Please run the tool with root user not only with \"sudo\" to configure your adapter with no issues ")
        print(" [Instruction] --> 2- Run \"sudo su\" command then enter the password for the current user to change to root with the present directory, then run the tool again :) \n")
def Checkexis():
    print("\n [*] --> Welcome to XEye-tp tool to set your \"tp-link\" model \"TL-WN722N\" Wifi USB adapter to Monitor mode :):):) \n\n")
    ifconfig_outp = subprocess.check_output('iwconfig')
    chwlan = re.search(r"WIFI@REALTEK", str(ifconfig_outp))
    chwlann = re.search(r"Mode:Auto", str(ifconfig_outp))
    chwlannn = re.search(r"Mode:Monitor", str(ifconfig_outp))
    if chwlannn:
        print("\n [Info] --> Your Wifi USB adapter is already set to Monitor mode, Exiting ...... ")
        print("\n [Recommendation] --> Run the \"exit\" command to exit the root shell, and stay secure :) ")
        exit()
    elif chwlann:
       print("\n [Info] --> Your Wifi USB adapter is already set to Auto mode ")
       asking = input(" [Permission] --> Would you like to set your Wifi USB adapter to \"Monitor mode now\" or \"reconfigure\"?  [set / reconf] ")
       if asking.lower() == 'set':
            tp_set()
       elif asking.lower() == 'reconf':
            tp_conf()
       else:
            print(" [Warning] --> Invalid Entry. [Your interface is just set to Auto mode]   Exiting .....")
            print("\n [Recommendation] --> Run the \"exit\" command to exit the root shell, and stay secure ;) ")
            exit()
    elif chwlan:
        usermd()
    else:
        print("\n [Warning] --> Please make sure that the Wifi USB is plugged in, Exiting ...... ")
        exit()

def usermd():
    sque= input("\n [Permission] --> Would you like to proceed? [yes / no] ")
    if sque.lower() == 'y' or sque.lower() == 'yes':
        tp_conf()
    elif sque.lower() == 'n' or sque.lower() == 'no':
        print("\n [*] --> Thanks for using XEye-tp tool, Exiting .....\n")
        print("\n [Recommendation] --> Run the \"exit\" command to exit the root shell, and stay secure ;) \n")
        print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert")
        
        exit()
    else:
        print(" [warning] --> Invalid entry, please use a yes or no answer, Exiting .....")
        exit()

def tp_conf():
 
    print("\n [*] --> Updating your system, please wait ....  \n")
    subprocess.call(['apt', 'update', '-y'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Installing build-essentials, Please wait ....  \n")
    subprocess.call(['apt', 'install', 'build-essential', '-y'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Installing bc, Won't take too long :) ....  \n")
    subprocess.call(['apt', 'install', 'bc', '-y'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Installing libelf-dev, Please wait ....  \n")
    subprocess.call(['apt', 'install', 'libelf-dev', '-y'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Installing the required linux-headers, Please wait .....  \n")
    subprocess.call("apt install linux-headers-$(uname -r)", shell=True)
    print("\n [*] --> Removing \"r8188eu.ko module\"  \n")
    subprocess.call(['rmmod', 'r8188eu.ko'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Git cloning \"rtl8188eus\"  \n")
    subprocess.call(['git', 'clone', 'https://github.com/drygdryg/rtl8188eus.git'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Installing dkms  \n")
    subprocess.call(['apt', 'install', 'dkms'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Done installing dkms. proceeding further ....  \n")
    os.chdir("rtl8188eus")
    print("\n [*] --> Echoing \"blacklist r8188eu.ko\" to \"realtek.conf\"  \n")
    subprocess.call("echo \"blacklist r8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)
    print("\n [*] --> Running Make command, Will take few minutes, please wait and ignore the upcoming errors and warnings ......  \n")
    subprocess.call(['sudo', 'make'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Running Make Install command  \n")
    subprocess.call(['sudo', 'make', 'install'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Running \"modprobe 8188eu\"  \n")
    subprocess.call("sudo modprobe 8188eu", shell=True)
    iwco = subprocess.check_output(['iwconfig'])
    Auto_check = re.search(r"Mode:Auto", str(iwco))
    if not Auto_check:
        print("\n [Warning] --> The Wifi adapter mode is not Auto or it is just missing. ")
        print(" [Instruction] --> UnPlug and plug in your Wifi USB adapter, wait for few seconds then run the tool again with root :)  \n")
        exit()
    if Auto_check.group(0) == 'Mode:Auto':
        print("\n [Congrats] --> The Wifi USB adapter is successfully configured \n")
        asking = input("\n [Permission] --> Would you like to set your Wifi USB adapter to Monitor mode now?  [yes / no] ")
        if asking.lower() == 'y' or asking.lower() == 'yes':
            tp_set()
        elif asking.lower() == 'n' or asking.lower() == 'no':
            print("\n [Info] --> Now your adapter is just set to Auto mode - Bye Bye :) \n")
            print("\n [Recommendation] --> Run the \"exit\" command to exit the root shell, and stay secure ;) ")
            print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert")
            subprocess.call("exit",shell=True)
            exit()
        else:
            print("\n [Warning] --> Invalid Entry. [Your interface is just set to Auto mode]   Exiting .....\n")
            exit()
def tp_set():
        interfs = subprocess.check_output('iwconfig')
        interf = re.search(r"\w\w\w\w\d", str(interfs))
        interff = re.search(r"\w\w\w\d", str(interfs))
        Interff = re.search(r"WIFI@REALTEK", str(interfs))
        if interf:
            interf = interf.group(0)
        elif interff and Interff:
            interf = interff.group(0)
        subprocess.call(['sudo', 'ifconfig', interf, 'down'])
        subprocess.call("sudo airmon-ng check kill", shell=True)
        subprocess.call(['sudo', 'iwconfig', interf, 'mode', 'monitor'])
        subprocess.call(['sudo', 'ifconfig', interf, 'up'])
        tp_check()
def tp_check():
    iwcon = subprocess.check_output(['iwconfig'])
    iwcon_Mcheck = re.search(r"Monitor",str(iwcon))
    if iwcon_Mcheck.group(0) == "Monitor":
        print("\n [Congrats] --> You wireless USB has been set to monitor mode, Bye Bye :) :) \n")
        print("\n [Recommendation] --> 1- Run the \"exit\" command to exit the root shell, and stay secure ;) ")
        print(" [Recommendation] --> 2- If you want to change the MAC address, clone XEye-Machanger tool from this link: \" https://github.com/Engmostafa26/XEye-MacChanger-v3.2\" ")
        print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert")
        exit()
    else:
        print("\n [Failed] --> Sorry :( , your Wifi USB could not be changed to monitor mode ")
        print("\n [Instruction] --> Upgrade and Restart your system then try again ")
        exit()
Checkroot()
