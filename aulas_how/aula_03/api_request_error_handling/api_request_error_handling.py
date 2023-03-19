#%%
import requests
import json

#%%

# APIs
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
ret = requests.get(url)

#%%

# API requisition status code
    # 1XX - info
    # 2XX - sucess (this is what we want!)
    # 3XX - redirect
    # 4xx - client error (you made a mistake)
    # 5xx - server error (they made a mistake)
if ret:
	print(ret)
else:
	print("Failed.")

# %%
dolar = json.loads(ret.text)['USDBRL']
# %%
print(f"20 dólares hoje custam R$ {float(dolar['bid']) * 20}.")

# %%
def cotacao(valor, moeda):
	url = "https://economia.awesomeapi.com.br/json/last/{}".format(moeda)
	ret = requests.get(url)
	dolar = json.loads(ret.text)[moeda.replace('-','')]
	cotacao = f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * 20} {moeda[-3:]}."
	print(cotacao)
# %%
cotacao(20, "USD-BRL")
# %%
cotacao(20, "JPY-BRL")
# %%
cotacao(20, "EDUARDO")
# %%


try:
	cotacao(20, "EDUARDO")
except:
	pass
# %%


try:
	cotacao(20, "JPY-BRL")
except:
	pass
else:
	print("Cotação funcionou.")
# %%


try:
	cotacao(20, "EDUARDO")
except Exception as e:
	print(f"Erro no parâmetro: {e}")
else:
	print("Cotação funcionou.")
# %%


try:
	10/0
except Exception as e:
	print(e)
else:
	print("ok")


# %%

def error_check(func):
	def inner_func(*args, **kargs):
		try:
			func(*args, **kargs)
		except:
			print(f"Função {func.__name__} falhou.")
	return inner_func

			
@error_check			
def multi_moedas(valor, moeda):
		url = "https://economia.awesomeapi.com.br/json/last/{}".format(moeda)
		ret = requests.get(url)
		dolar = json.loads(ret.text)[moeda.replace('-','')]
		cotacao = f"{valor} {moeda[:3]} hoje custam {round(float(dolar['bid']) * 20, 2)} {moeda[-3:]}."
		print(cotacao)
			
# %%


multi_moedas(valor=20, moeda="USD-BRL")
multi_moedas(valor=20, moeda="EUR-BRL")
multi_moedas(valor=20, moeda="BTC-BRL")
multi_moedas(valor=20, moeda="JPY-BRL")
multi_moedas(valor=20, moeda="RPL-BRL")
# %%


import backoff
import random

# Exposing errors and applying retries
@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError),
                    max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
            RND: {rnd}
            args: {args if args else 'no args'}
            kargs: {kargs if kargs else 'no kargs'}
    """)
    if rnd < .2:
        raise ConnectionAbortedError("Conexão abortada.")
    elif rnd < .4:
        raise ConnectionRefusedError("Conexão recusada.")
    elif rnd < .6:
        raise TimeoutError("Tempo de espera excedido.")
    else:
        return "OK! Número randômico (RND) aceito."
# %%

# no args / no kargs
test_func()

# %%

# args / no kargs
test_func(1)
# %%

# no args / kargs
test_func(name = "EDUARDO")
# %%

# args / kargs
test_func(1, name = "EDUARDO")

# %%


# Logs
import logging


log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
	'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)


# %%

# Exposing errors and applying retries
@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError),
                    max_tries=10)
def test_func(*args, **kargs):
    random_float = round(random.random(), 2)
    log.debug(f"RND: {random_float}")
    log.info(f"args: {args if args else 'no args'}")
    log.info(f"kargs: {kargs if kargs else 'no kargs'}")
    if random_float < .2:
        log.error("Conexão abortada.")
        raise ConnectionAbortedError("Conexão abortada.")
    elif random_float < .4:
        log.error("Conexão recusada.")
        raise ConnectionRefusedError("Conexão recusada.")
    elif random_float < .6:
        log.error("Tempo de espera excedido.")
        raise TimeoutError("Tempo de espera excedido.")
    else:
        return f"OK! Número randômico (RND) aceito: {random_float}"
# %%
test_func()