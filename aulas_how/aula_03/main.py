#%%
import requests
import json

#%%
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
ret = requests.get(url)

#%%
if ret:
  print(ret)
else:
  print("Failed.")

# %%
dolar = json.loads(ret.text)['USDBRL']
# %%
print(f"20 dólares hoje custam R$ {float(dolar['bid']) * 20}.")

# %%
