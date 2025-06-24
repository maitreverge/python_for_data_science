FROM python:3.10-alpine

RUN apk add zsh

RUN mkdir -p module_00

COPY . ./module_00

WORKDIR /module_00

RUN pip install -r ./requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]