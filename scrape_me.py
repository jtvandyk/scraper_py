## Prints table to JSON in browser
#import pandas as pd
#import requests
#from bs4 import BeautifulSoup
 
#res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
#soup = BeautifulSoup(res.content,'lxml')
#table = soup.find_all('table')[0] 
#df = pd.read_html(str(table))
#print(df[0].to_json(orient='records'))

## Converts table to dataframe in Pandas
#import pandas as pd
#import requests
#from bs4 import BeautifulSoup
 
#res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
#soup = BeautifulSoup(res.content,'lxml')
#table = soup.find_all('table')[0] 
#df = pd.read_html(str(table))[0]
#countries = df["COUNTRY"].tolist()
#users = df["AMOUNT"].tolist()

## Converts table to dataframe in pgsql format
#import pandas as pd
#import requests
#from bs4 import BeautifulSoup
#from tabulate import tabulate
 
#res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
#soup = BeautifulSoup(res.content,'lxml')
#table = soup.find_all('table')[0] 
#df = pd.read_html(str(table))
#print( tabulate(df[0], headers='keys', tablefmt='psql') )
