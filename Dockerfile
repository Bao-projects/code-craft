FROM python:3.9

WORKDIR /app

COPY requirements.txt .

# Install required python libraries
RUN pip install -r requirements.txt

RUN apt-get update -y
RUN apt update -y

#==============================================================================
# Install programming languages compilers/interpreters needed
#==============================================================================
# C
RUN apt-get install -y gcc
# C++
RUN apt-get install -y g++
# C#
RUN apt install -y mono-complete
# Java
RUN apt install -y default-jre
# Javascript
RUN apt-get install -y nodejs
# Python3
RUN apt-get install -y python3
# Ruby
RUN apt-get install -y ruby-full

COPY ./ .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
