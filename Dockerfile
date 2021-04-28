FROM python:3.8-buster

# install go
RUN apt update \
    && apt install -y sudo \
    && sudo apt-get install -y software-properties-common \
    && sudo add-apt-repository ppa:longsleep/golang-backports \
    && sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 52B59B1571A79DBC054901C0F6BC817356A3D45E \
    && sudo apt install golang-go -y --no-install-recommends

RUN pip install pre-commit commitizen --quiet \
    pre-commit install-hooks


VOLUME ["/home", "/home/circleci"]