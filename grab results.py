from bs4 import BeautifulSoup
import pandas as pd 
import requests


url = "https://mychiptime.com/searchResultGen.php?eID=14863&showExtra=1&showall=1&export="
x = requests.get(url)
df=pd.read_html(x.text,attrs = {'id': 'myTable'})[0]
df.columns = [x.lower().replace(" ","_") for x in df.columns]
print(df)
#df.to_csv("race.csv",index=False)