import bs4
import urllib.request

race_site=urllib.request.urlopen("http://paizo.com/pathfinderRPG/prd/races.html#chapter-2").read()
race_soup=bs4.BeautifulSoup(race_site,"html.parser")
r=race_soup.encode('utf8')
f=open('C:\\Users\\t161249\\Desktop\\Overflow\\race_info.txt','a')
for x in race_soup.find_all('p'):
	try:
		f.write(str(x))
	except:
		pass
f.close()
