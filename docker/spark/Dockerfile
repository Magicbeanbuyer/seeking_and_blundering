# base images
ARG IMAGE_VARIANT=slim-buster
ARG OPENJDK_VERSION=8
#ARG PYTHON_VERSION=3.8
#FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT} AS py3
FROM openjdk:${OPENJDK_VERSION}-${IMAGE_VARIANT}
#COPY --from=py3 / /

RUN apt-get update && apt-get install -y wget \
    gpg \
    procps

# install spark
ENV SPARK_HOME=/usr/lib/spark
ARG SPARK_VERSION=3.1.1
ARG HADOOP_VERSION=3.2
ARG SPARK_DIST=spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}
RUN wget --progress=dot:giga \
    https://ftp-stud.hs-esslingen.de/pub/Mirrors/ftp.apache.org/dist/spark/spark-${SPARK_VERSION}/${SPARK_DIST}.tgz \
    && wget https://downloads.apache.org/spark/spark-${SPARK_VERSION}/${SPARK_DIST}.tgz.asc \
    && wget https://downloads.apache.org/spark/KEYS \
    && gpg --import KEYS \
    && gpg --verify ${SPARK_DIST}.tgz.asc ${SPARK_DIST}.tgz \
    && tar -xzf ${SPARK_DIST}.tgz \
    && mv ${SPARK_DIST} ${SPARK_HOME} \
    && rm ${SPARK_DIST}.tgz ${SPARK_DIST}.tgz.asc

# python packages
#RUN pip install pytest \
#    numpy \
#    pandas \
#    boto3

ENV PATH $SPARK_HOME/bin:$PATH
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9-src.zip
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
#ENV PYSPARK_PYTHON python3

WORKDIR ${SPARK_HOME}

CMD ["bash"]

# docker run -ti --rm --name pyspark_container -v $PWD/src:/root/src  spark_sandbox
#/usr/lib/spark