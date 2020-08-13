
# Should I use umbrella?  
  
Consulta o tempo na cidade para ver se sevo usar meu guarda chuva!  
  
O Sistema consulta uma API de previsão do tempo [**Weather AP**I](https://openweathermap.org/api)  para os próximos 5 dias e verifica a umidade do ar para cada dia.
Caso a umidade do ar seja maior do que **70%** é recomendado que o guarda chuva seja usado.
 
Demonstração: [https://weather-challenge.herokuapp.com/](https://weather-challenge.herokuapp.com/)

## Como desenvolver?  
  
1. clone o respositório.  
2. crie um virtualenv com Python 3.7.  
3. Ative o virtualenv.  
4. Instale as dependências.  
5. Configure a instância .env  
  
```console  
git clone git@github.com:lffsantos/weather_challenge.git weather_challenge  
cd weather_challenge  
virtualenv -p python3 .venv  
source .venv/bin/activate  
pip install -r requirements-dev.txt  
cp contrib/env-sample .env  
python manage.py migrate
python mangae.py load_cities
python mangae.py load_countries
```  

### Rodar Testes:

>pytest


### Rodar Aplicação

> python manage.py runserver

  
## Configurações  
  
Para o sistema funcionar corretamente é preciso realizar o cadastro na [Weather API](https://openweathermap.org/api).
- [https://home.openweathermap.org/users/sign_up](https://home.openweathermap.org/users/sign_up)

Fazer a inscrição no serviço :
- [https://openweathermap.org/api/one-call-api](https://openweathermap.org/api/one-call-api)

Após a inscrição pegar a `key` gerada em API keys e adicionar ao arquivo `.env `
APPID=


## REST API

#### [GET] - /api/v1/cities
Listagem de cidades possíveis para buscar a previsão.
#### [GET] - /api/v1/countries
 Listagem de Países

####  [GET] -  /api/v1/weather/<CODE_CITY> 
Faz a consulta na API do Tempo para saber se devemos utilizar o guarda chuva nos próximos 5 dias.
*CODE_CITY = Código da cidade. 
**Returns**:
- _You should take an umbrella in these days: ...._  
**or**
- _You won't need an umbrella for the next few days_

Exemplo:
, Se a umidade do ar for superior a 70% na segunda e quarta-feira , vai exibir a seguinte mensagem:
-	_You should take an umbrella in these days: Monday and Wednesday._

Caso em nenhum dos dias a umidade seja superior:
- _You won't need an umbrella for the next few days_