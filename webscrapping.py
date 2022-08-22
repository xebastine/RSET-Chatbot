import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.rajagiritech.ac.in/Home/Placement/Pdrive.asp")
soup = BeautifulSoup(page.content,'html.parser')

drivename1 = soup.find('body')
drivename2 = drivename1.find_all(class_="title")
drivename = drivename2[0]
tags = drivename1.select(".title")
drivenames = [pt.get_text() for pt in tags]
#for x in drivenames[0:5]:
#	print(x)

dates = []
lastdate1 = soup.find_all('div',class_="details")
for detailsyo in lastdate1:
    detailsyoyo = detailsyo.find('p')
    if (detailsyoyo is not None):
	    dates.append(detailsyoyo.text)

answer = ""
drives5 = drivenames[0:5]
dates5 = dates[0:5]
for i in range(5):
    answer = answer + drives5[i] + '\n' + dates5[i] + '\n\n'

answer+="For more information please visit https://www.rajagiritech.ac.in/Home/Placement/Pdrive.asp"
print(answer)
