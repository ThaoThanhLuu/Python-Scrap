import requests  
import datetime

githubURL='https://github.com/f5devcentral'

#Example
#https://github.com/f5devcentral/ansible-role-f5ansible/graphs/contributors

r = requests.get(githubURL)

file = open("F5DevCentralRepos.txt", "r")

for lines in file:

	temp = githubURL +'/' + lines + 'graphs/contributors'
	
#Create functions to call from to scrape each repo URL 
