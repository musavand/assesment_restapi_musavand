## Logic Of Project
```fetch & save data
call http://localhost:8000/get_data  or prese on get data link on home
```
```show data
call http://localhost:8000  i set page size= 5
```
```search data
call http://localhost:8000  and then any text  for serch after first serch consider yuor search creteria 
```
## Setup the project
```xamp
database:
 i used mysql as database if you dont change default db in settings.py
```
api:
i use todo free api  and could not test move api

## Install requirements

Create a new virtual environment
```shell
1-  python -m venv myenv-env
2-  run activate in myenv-env\scripts
```

Install packages

```shell
pip install -r requiremnts.txt
```

## Test the application

Open your browser and go to [localhost:8000](http://localhost:800/)