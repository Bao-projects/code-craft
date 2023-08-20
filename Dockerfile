FROM python:3.9

WORKDIR /app

COPY requirements.txt .

# Install required python libraries
RUN pip install -r requirements.txt

RUN apt-get update -y
# Install programming langauges compilers/interpreters needed
RUN apt-get install -y g++
RUN apt-get install -y nodejs
RUN apt-get install -y python3
RUN apt-get install -y ruby-full

COPY ./ .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
