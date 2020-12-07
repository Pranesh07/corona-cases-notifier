from plyer import notification
import requests
from bs4 import BeautifulSoup



def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="icon.ico",
        timeout=10,
    )
def getData(url):
    r=requests.get(url)
    return r.text 
if __name__=="__main__":
    # notifyMe("Welcome","Pranesh")
    myHtmlData=getData("https://www.worldometers.info/coronavirus/country/india/")
    # print(myHtmlData)
    soup=BeautifulSoup(myHtmlData,'html.parser')
    # print(soup.prettify())
     
    
    cases=soup.find_all(class_="maincounter-number")
    p=[]
    for i in cases:
         p.append(i.text.strip())
    totat_cases="Total Cases: "+p[0]
    deaths=p[1]
    recovered=p[2]
    s=" Deaths:"+p[1]
    s+="\nRecovered :"+p[2]
    s+='\n----Stay Home Stay Safe----'
    notifyMe(totat_cases,s) 
        
     
     
        
         