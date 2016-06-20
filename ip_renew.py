import time

import socket
import socks

import requests
from bs4 import BeautifulSoup

from stem import Signal
from stem.control import Controller


controller = Controller.from_port(port=9051)

def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

def renew_tor():
    controller.authenticate("Ayush22x")
    controller.signal(Signal.NEWNYM)

def showmyip():
    url = "http://www.showmyip.gr/"
    r = requests.Session()
    page = r.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    ip_address = soup.find("span",{"class":"ip_address"}).text.strip()
    print(ip_address)


for i in range(10):
    renew_tor()
    connectTor()
    showmyip()
    time.sleep(1)
