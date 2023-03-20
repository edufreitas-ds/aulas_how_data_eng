# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
# %%

url = 'https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'
# %%

i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)
# %%

houses = soup.find_all('a',
                      {'class':'property-card__content-link js-card-title'})
sell = float(soup.find('strong', {'class': 'results-summary__count js-total-records'}).text.replace('.', ''))
# %%
len(houses)
# %%

house = houses[0]
# %%

house
# %%

# descricao
descricao = house.find('span', {'class' : 'property-card__title'}).text.strip()
# endereco
endereco = house.find('span', {'class' : 'property-card__address'}).text.strip()
# area
area = house.find('span', {'class' : 'property-card__detail-area'}).text.strip()
# quartos
quartos = house.find('li', {'class' : 'property-card__detail-room'}).span.text.strip()
# wc (banheiro)
wc = house.find('li', {'class' : 'property-card__detail-bathroom'}).span.text.strip()
# vagas (garagem)
vagas = house.find('li', {'class' : 'property-card__detail-garage'}).span.text.strip()
# valor
valor = house.find('div', {'class' : 'property-card__price'}).p.text.strip()
# condominio
condominio = house.find('div', {'class' : 'property-card__price-details--condo'}).strong.text.strip()
# wlink (link do imovel)
wlink = 'https://www.vivareal.com.br' + house['href']

print(descricao)
print(endereco)
print(area)
print(quartos)
print(wc)
print(vagas)
print(valor)
print(condominio)
print(wlink)
# %%


# continue no link: https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/