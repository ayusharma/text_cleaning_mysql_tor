import peewee
from peewee import *
import urllib2
import json

# import time

# import socket
# import socks

# import requests
# from bs4 import BeautifulSoup

# from stem import Signal
# from stem.control import Controller

db = MySQLDatabase('country', user='root',passwd='Ayush22x')
# controller = Controller.from_port(port=9051)

class Story_TweetLocation(peewee.Model):
	country_code = peewee.CharField()
	city_name = peewee.CharField()

	class Meta:
		database = db

class Repeating_Val(peewee.Model):
	id = peewee.IntegerField()

	class Meta:
		database = db

rv = Repeating_Val
st = Story_TweetLocation


# def connectTor():
#     socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
#     socket.socket = socks.socksocket

# def renew_tor():
#     controller.authenticate("Ayush22x")
#     controller.signal(Signal.NEWNYM)

# def showmyip():
#     url = "http://www.showmyip.gr/"
#     r = requests.Session()
#     page = r.get(url)
#     soup = BeautifulSoup(page.content, "lxml")
#     ip_address = soup.find("span",{"class":"ip_address"}).text.strip()
#     print(ip_address)


def values():
	for k in rv.select():
		print k.id
		# renew_tor()
		# connectTor()
		#showmyip()
		# time.sleep(1)
		db_obj = st.get(st.id == k.id)
		print db_obj.city_name
		url = "http://api.geonames.org/searchJSON?q="+db_obj.city_name.strip().replace(' ','%20')+"&maxRows=1&fuzzy=0.8&username=ayushpix"
		print url
		data =  json.loads(urllib2.urlopen(url).read())
		print data
		if data["geonames"][0]["countryCode"] != db_obj.country_code:
			st.delete().where(st.id == k.id).execute()
			rv.delete().where(rv.id <= k.id).execute()
			print "Deleted"
		else:
			pass

if __name__ == "__main__":
	values()
