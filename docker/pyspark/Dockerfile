ARG IMAGE_VARIANT=slim-buster
ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT}

RUN pip install --upgrade pip && \
    pip install pyspark

EXPOSE 8080:8080

CMD ["bash"]
# docker run -ti --rm --name pyspark_container -v $PWD/src:/root/src  pyspark_sandbox
