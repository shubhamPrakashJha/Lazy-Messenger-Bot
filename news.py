import requests
from bs4 import BeautifulSoup
import subprocess
import time
 
url = "http://timesofindia.indiatimes.com/"
 
def open_url(url):
    return requests.get(url).text  
 
def get_bsoup_object(html):
    return BeautifulSoup(html, "lxml")
 
def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return
 
def main():
    myhtml = open_url(url)
    soup = get_bsoup_object(myhtml)
    j = 1
   
    for i in soup.find('ul',attrs={'class':'list9'}).findAll('li'):
        #print(str(j) + " " + i.text)
        sendmessage(str(j) + " " + i.text)
        time.sleep(10)
        j += 1
       
while True:
    main()
    print "News update started"
    time.sleep(3600)
