import requests  
import datetime

r = requests.get('[githuburl]')

from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')

#Search for matched attributes
results = soup.find_all("h3",class_='wb-break-all')

#Search for date data
dateClass = soup.find_all("relative-time")

#Github URL
githubURL = 'https://github.com'
URL = ''
ProjectName = ''
dates = ''
records = []  
for result in results:

	#URL of project
	parsedURL = result.find('a')['href']
	URL = githubURL+parsedURL+' '

	#Name of project
	hovercard = result.find('a')['data-hovercard-url']
	tempStr= hovercard.replace('/f5devcentral/','')
	ProjectName= tempStr.replace('/hovercard','')

	#append soup information to Record Python List
	records.append((URL,ProjectName,dates))

for dates in dateClass:

	dates.find('datetime')	
	#print(dates)
	records.append((dates))

#Transfer information onto Excel file 
import pandas as pd  
df = pd.DataFrame(records, columns=['Github Location', 'ProjectName', 'Last Updated'])  
df.to_csv('ScrapTesting.csv', index=False, encoding='utf-8') 