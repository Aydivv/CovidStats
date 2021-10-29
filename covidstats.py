from bs4 import BeautifulSoup
import requests
print("===============================================================")
country = input("Enter country:")
site = requests.get(f"https://www.worldometers.info/coronavirus/country/{country}/")
soup = BeautifulSoup(site.content,'lxml')
print("===============================================================")
#total data
totaldata = soup.find_all(class_="maincounter-number")
try:
    tcases,tdeaths,trecovs=totaldata[0].text.replace("\n",""),totaldata[1].text.replace("\n",""),totaldata[2].text.replace("\n","")
except:
    print("Country does not exist in our database.")
    print("===============================================================")
    quit()
print(f"Total cases in {country} is {tcases}.")
print(f"Total deaths in {country} is {tdeaths}.")
print(f"Total recoveries in {country} is {trecovs}.")
#daily data
print("===============================================================")
dailydate = soup.find(class_="news_date").text
dailydata = soup.find("div",class_="news_body").find_all("strong")
dcases,ddeaths=dailydata[0].text,dailydata[1].text
print(f"On {dailydate} in {country} there have been:")
print(dcases)
print(ddeaths)
print("===============================================================")
