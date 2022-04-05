from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from plyer import notification
import time


quotes_page ='https://www.mohfw.gov.in/'
uClient = uReq(quotes_page)
page_html = uClient.read()
uClient.close()

page_soup =soup(page_html,"html.parser")
active_data = page_soup.findAll("div",{"class":"col-xs-8 site-stats-count"})




def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon ='C:\\Users\\thaku\PycharmProjects\\big projects\\real time corona outbreak notification sysetm\\icon.ico',

        timeout = 10,
    )

while (True):
    for data in active_data:
        active_cases = data.findAll("strong")
        Active = active_cases[0].text.strip()

        no_of_cases = data.findAll("strong")
        Cases = no_of_cases[1].text.strip()

        Discharged = data.findAll("strong")
        Dis = Discharged[3].text.strip()

        no_of_discharged = data.findAll("strong")
        no_of_dis = no_of_discharged[4].text.strip()

        Deaths = data.findAll("strong")
        dea = Deaths[6].text.strip()

        no_of_deaths = data.findAll("strong")
        no_of_dea = no_of_deaths[7].text.strip()

        notify_title = "covid-19 Status"
        notify_text = f"ActiveCases: {Cases}\nCured\Discharged: {no_of_dis}\nDeaths: {no_of_dea}"
        notifyMe(notify_title, notify_text)
    time.sleep(86400)