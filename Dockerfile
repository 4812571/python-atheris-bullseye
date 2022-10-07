FROM python:3.8-bullseye
RUN python3 -m pip install atheris
COPY . /thefuzz
WORKDIR /thefuzz

RUN python3 -m pip install .
RUN chmod +x fuzz/fuzzme.py