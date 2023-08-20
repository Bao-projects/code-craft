# Build the docker image
docker build -t code-craft .

# Run the image
docker run -p 5000:5000 code-craft
