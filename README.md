1- activate venv: source .venv/bin/activate
2-run database: make silentup
3-run migrations: make makemigrations
4-apply migrations: make migrate
5-run server: make runserver
5- go this url : http://localhost:8000/swagger/
6- create user and then login and get token fro api-token-auth endpoint and authorise with = Token whatever_token_you_get
7- you can access shared urls the tennant urls will give error for their tables are not created
8-create tenant for example with buinsess name bigco and add to url http://bigco.localhost:8000/swagger/
9-Now you can access tenants urls and check database where tenant schema should be created.
