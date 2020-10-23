test:
	pytest

run:
	uvicorn app.server:APP --host 127.0.0.1

build-docker:
	docker build -t movies-server .

run-docker:
	docker run -t -i --network host movies-server


