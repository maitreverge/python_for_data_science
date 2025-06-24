#! /bin/sh

CONTAINER_NAME="my_python"

echo "⌛ BUILDING DOCKER PYTHON DATA SCIENCE ⌛"

docker build -t $CONTAINER_NAME .

docker run -d $CONTAINER_NAME

CONTAINER_ID=$(docker container ls | grep "$CONTAINER_NAME" | awk '{print $1}')

docker exec -it $CONTAINER_ID /bin/zsh