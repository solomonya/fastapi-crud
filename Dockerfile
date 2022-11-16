FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt requirements.txt
RUN python -m pip install -U pip
RUN pip3 install -r requirements.txt
COPY . /src
EXPOSE 8000