APP_NAME:=e-comm-crm

.PHONY: build run

build-dev:
	docker build -t $(APP_NAME) -f Dockerfile.dev .

run-dev:
	docker run -d -p 5000:5000 --name=$(APP_NAME) -v $(PWD):/app $(APP_NAME)

local:
	FLASK_ENV=development python manage.py