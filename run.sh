# Build the docker image
sudo docker build -t code-craft .

# Run the image
sudo docker run -p 5000:5000 code-craft
