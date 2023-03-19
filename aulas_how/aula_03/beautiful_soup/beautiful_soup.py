#%%
import requests
from bs4 import BeautifulSoup as bs
import logging
import pandas as pd
# %%

url = 'https://portalcafebrasil.com.br/todos/podcasts/'
ret = requests.get(url)
# %%

ret.text
# %%

# Beautiful Soup - Single Page
soup = bs(ret.text)
# %%

soup
# %%

soup.find('h5')
# %%

soup.find('h5').text
# %%


soup.find('h5').a
# %%

soup.find('h5').a['href']
# %%


lst_podcast = soup.find_all('h5')
# %%

for h5 in lst_podcast:
  print(f"EP: {h5.text} - Link: {h5.a['href']}")
# %%


# Beautiful Soup Multi-page (waterfall)

url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'
# %%

url.format(5)
# %%


log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
	'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

#%%


def get_podcast(url):
  ret = requests.get(url)
  soup = bs(ret.text)
  return soup.find_all('h5')
# %%

get_podcast(url.format(5))

#%%



# %%


iter = 1
lst_podcast = []
lst_get = get_podcast(url.format(iter))
log.debug(f"Coletado {len(lst_get)} episódios do link: {url.format(iter)}")

while len(lst_get) > 0:
  lst_podcast = lst_podcast + lst_get
  iter += 1
  lst_get = get_podcast(url.format(iter))
  log.debug(f"Coletado {len(lst_get)} episódios do link: {url.format(iter)}")
# %%
len(lst_podcast)


#%%
lst_podcast


#%%
df = pd.DataFrame(columns=['name', 'link'])

# %%

for item in lst_podcast:
  df.loc[df.shape[0]] = [item.text, item.a['href']]
# %%

df.shape
# %%

df.head()
# %%

df.to_csv('podcast_cafebrasil_db.csv', index=False)
# %%
