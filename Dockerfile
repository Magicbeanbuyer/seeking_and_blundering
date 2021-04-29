FROM python:3.8-slim-buster

ENV GO_VERSION=go1.16.3
ENV GO_BINARY=$GO_VERSION.linux-amd64.tar.gz

# assume yes for apt install
RUN echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/installAssumeYes

# intall git, ssh, ca-certificates to work with circleci
# https://circleci.com/docs/2.0/custom-images/?section=executors-and-images#creating-a-custom-image-manually
RUN apt update && apt install sudo \
    && sudo apt install curl \
    git \
    ssh \
    ca-certificates

# install go for tflint
RUN curl -O "https://dl.google.com/go/$GO_BINARY" \
    && tar xvf $GO_BINARY \
    && sudo mv go /usr/local \
    && rm $GO_BINARY
# add go the PATH
ENV PATH=$PATH:/usr/local/go/bin

RUN pip install pre-commit commitizen --quiet

# set /home/circleci as home dir
RUN mkdir /home/circleci
ENV HOME=/home/circleci
