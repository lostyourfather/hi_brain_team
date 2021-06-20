build_api:
	docker build -t apiserver .

up_api:
	docker run -it -p 8000:8000 --network hib_as_api_docker --env-file deployment/loc.env apiserver