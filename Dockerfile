FROM python:3.8-slim-buster
WORKDIR /Desktop/pythondemo
COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt
EXPOSE 5001
COPY . .
CMD [ "python3", "appset.py"]


