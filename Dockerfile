FROM python:3.8-slim-buster
WORKDIR /isp
COPY . .
CMD ["python","main.py"]
