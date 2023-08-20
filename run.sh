sudo docker pull ubuntu &&\
    sudo docker build -t code-craft . &&\
    sudo docker run -p 5000:5000 code-craft
