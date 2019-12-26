docker-compose -f docker-compose_test.yml up --build
docker run kannan1985/netapp_docker_demo coverage report -m flask_rest/tests/*
docker run kannan1985/netapp_docker_demo python flask_rest/tests/test.py
