# RESTful-service for Tardis company

### __How to install:__

##### __1.__ Open your linux console
##### __2.__ git clone https://github.com/FedorNemira/tardis_hometask.git
##### __3.__ cd tardis_hometask
##### __4.__ python3 -m venv env
##### __5.__ source env/bin/activate
##### __6.__ pip install -r requirements.txt
##### __7.__ python manage.py runserver

### __Now can send GET and POST requests to http://127.0.0.1:8000/__

##### __1.__ /login?phone=<phone> GET request, you will receive secret code. For exapmple: http://127.0.0.1:8000/login?phone=79771113311

##### __2.__ /login POST request: {"phone": "+71111111111", "code": "QWDCR4"}

##### __3.__ /structure GET request, you will receive caculation of html tags in json fomat of URL: freestylo.ru

##### __4.__ /structure?link=<link> GET request, you will receive caculation of html tags of URL you entred. For exapmple: http://127.0.0.1:8000/structure?link=www.yandex.ru

##### __5.__ /structure?link=<link>&tags=<tags sepparated by ","> GET request, you will receive caculation of html tags of URL you entred(for expmple http://127.0.0.1:8000/structure?link=www.yandex.ru&tags=li,div)

##### __6.__ /check_structure POST request JSON with "link" and "structure" parameters. For exmaple: {"link": "freestylo.ru", "structure": {"html": 1, "head": 1, "body": 1, "p": 10, "img": 2}}. You will receive {"is_correct": True} if tags are match with your request, and {"is_correct": False, "difference": {"p": 2, "img": 1}} where "difference" is name of unmatched tags. 


#### __You can use my Postman tests. To do this, you need to open file "Tardis_homework.postman_collection.json" in your Postman app.__
  
 Alaso you can try it on http://tardis.fedor-nemira.com/
