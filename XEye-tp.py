#! /usr/bin/env python3

import subprocess
import os
import re

def Checkexis():
    ifconfig_outp = subprocess.check_output('iwconfig')
    chwlan = re.search(r"Link Quality", str(ifconfig_outp))
    if chwlan:
        usermd()
    else:
        print("\n [Warning] --> Please make sure that the Wifi USB is plugged in, Exiting ...... ")
        exit()

def usermd():
    print("\n [*] --> Welcome to XEye-tp tool to set the \"tp-link\" usb model \"TL-WN722N\" wireless to monitor mode")
    sque= input("\n [Permission] --> Would you like to proceed? ")
    if sque.lower() == 'y' or sque.lower() == 'yes':
        tp_conf()
    elif sque.lower() == 'n' or sque.lower() == 'no':
        print("\n [*] --> Thanks for using XEye-tp tool, Exiting .....\n")
        print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert")
        exit()
    else:
        print(" [warning] --> Invalid entry, please use yes or no answer, Exiting .....")
        exit()

def tp_conf():
    print("\n [*] --> Updating your system, please wait ....  \n")
    subprocess.call(['sudo', 'apt', 'update', '-y'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Installing build-essentials, Please wait ....  \n")
    subprocess.call(['sudo', 'apt', 'install', 'build-essential', '-y'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Installing bc, Won't take too long :) ....  \n")
    subprocess.call(['sudo', 'apt', 'install', 'bc', '-y'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Installing libelf-dev, Please wait ....  \n")
    subprocess.call(['sudo', 'apt', 'install', 'libelf-dev', '-y'], stdout=subprocess.DEVNULL)
    #print("\n [*] --> Installing the required linux-headers, Please wait .....  \n")
    #subprocess.call(['sudo', 'apt-get', 'install', 'linux-headers-`uname', '-r\''], stdout=subprocess.DEVNULL)
    print("\n [*] --> Removing \"r8188eu.ko module\"  \n")
    subprocess.call(['sudo', 'rmmod', 'r8188eu.ko'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Git cloning \"rtl8188eus\"  \n")
    subprocess.call(['git', 'clone', 'https://github.com/aircrack-ng/rtl8188eus'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Installing dkms  \n")
    subprocess.call(['sudo', 'apt', 'install', 'dkms'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Done installing dkms. proceeding further ....  \n")
    os.chdir("rtl8188eus")
    print("\n [*] --> Echoing \"blacklist r8188eu.ko\" to \"realtek.conf\"  \n")
    subprocess.call("echo \"blacklist r8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)
    print("\n [*] --> Running Make command, Will take few minutes, please wait ......  \n")
    subprocess.call(['sudo', 'make'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Running Make Install command  \n")
    subprocess.call(['sudo', 'make', 'install'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Running \"modprobe 8188eu\"  \n")
    subprocess.call("sudo modprobe 8188eu", shell=True)
    iwco = subprocess.check_output(['iwconfig'])
    Auto_check = re.search(r"Mode:Auto", str(iwco))
    if not Auto_check:
        print("\n [Warning] --> the wlan interface mode is not Auto, ")
        print(" [Instruction] --> UnPlug and plug in your Wireless USB then try again  \n")
        exit()
    if Auto_check.group(0) == 'Mode:Auto':
        print("\n [Congrats] --> The wlan interface mode is currently Auto \n")
        tp_set()
        
def tp_set():
    asking = input(" [Permission] --> Would you like to change your wireless interface to Monitor mode now? [yes / no] ")
    if asking.lower() == 'y' or asking.lower() == 'yes':
        interfs = subprocess.check_output('iwconfig')
        interf = re.search(r"\w\w\w\w\d", str(interfs))
        interf = interf.group(0)
        subprocess.call(['sudo', 'ifconfig', interf, 'down'])
        subprocess.call("sudo airmon-ng check kill", shell=True)
        subprocess.call(['sudo', 'iwconfig', interf, 'mode', 'monitor'])
        subprocess.call(['sudo', 'ifconfig', interf, 'up'])
        tp_check()
    elif asking.lower() == 'n' or asking.lower() == 'no':
        print("\n [Info] --> Now your wireless interface is just set to Auto,  Bye Bye :) \n")
        print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert")
        exit()
    else:
        print(" [Warning] --> Invalid Entry. [Your interface is just set to Auto mode]   Exiting .....")
        exit()
def tp_check():
    iwcon = subprocess.check_output(['iwconfig'])
    iwcon_Mcheck = re.search(r"Monitor",str(iwcon))
    if iwcon_Mcheck.group(0) == "Monitor":
        print("\n [Congrats] --> You wireless USB has been set to monitor mode, Bye Bye :) :) \n")
        print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert")
        exit()
    else:
        print("\n [Failed] --> Sorry :( , your Wirelss USB is not changed to monitor mode ")
        print("\n [Instruction] --> Upgrade and Restart your machine and try again ")
Checkexis()
