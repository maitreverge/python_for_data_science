#! /bin/sh

CONTAINER_NAME="my_python"

CONTAINER_ID=$(docker container ls | grep "$CONTAINER_NAME" | awk '{print $1}')

echo "⌛ CLEANING DOCKER PYTHON DATA SCIENCE ⌛"

docker stop $CONTAINER_ID

docker rmi $CONTAINER_ID

echo "✅ DOCKER PYTHON DATA SCIENCE CLEANED ✅"