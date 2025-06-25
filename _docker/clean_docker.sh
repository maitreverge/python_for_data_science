#! /bin/sh

CONTAINER_NAME="my_python"

CONTAINER_ID=$(docker ps --all | grep "$CONTAINER_NAME" | awk '{print $1}')

IMAGE_ID=$(docker images | grep "my_python" | awk '{print $3}')

echo "⌛ CLEANING PYTHON DATA SCIENCE CONTAINER ⌛"

# Stop container
docker stop $CONTAINER_ID

# Delete container
docker container rm $CONTAINER_ID

# Remove image
docker rmi $IMAGE_ID

echo "✅ CONTAINER PYTHON DATA SCIENCE CLEANED ✅"