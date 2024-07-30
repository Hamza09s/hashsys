makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

migrate_schemas_shared:
	python manage.py migrate_schemas --shared
silentup:
	sudo docker compose up -d
runserver:
	python manage.py runserver

db_shell:
	python manage.py shell
