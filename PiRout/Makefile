setup:
	python3 -m venv venv && . venv/bin/activate && pip install -r api/requirements.txt
	cd front-end && npm install && cd ..

run:
	docker-compose up --build

test:
	cd backend/python && PYTHONPATH=../.. pytest && cd ../..

lint:
	flake8 backend/python/pirout api/app.py || true
	gofmt -w backend/go/main.go

build:
	cd front-end && npm run build && cd ..
	go build -o backend/go/pirout backend/go/main.go
