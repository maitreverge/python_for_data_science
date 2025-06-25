FROM python:3.10-alpine

RUN apk add zsh

RUN mkdir -p module_xx

COPY . ./module_xx

WORKDIR /module_xx

RUN pip install -r ./requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]