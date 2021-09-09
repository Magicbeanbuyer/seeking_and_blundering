# base images
FROM python:3.7-slim-buster AS py3
FROM openjdk:8-slim-buster
COPY --from=py3 / /

ENV SPARK_HOME=/usr/local/lib/python3.7/site-packages/pyspark
# s3a driver credential
# minioadmin is default credential for minIO server
ENV AWS_ACCESS_KEY_ID=minioadmin
ENV AWS_SECRET_ACCESS_KEY=minioadmin
ENV AWS_REGION=eu-central-1

RUN apt-get update && apt-get install -y curl git

# renovate: datasource=pypi depName=boto3
ARG BOTO3_VERSION=1.18.31
RUN pip install --upgrade boto3==$BOTO3_VERSION

# renovate: datasource=pypi depName=moto
ARG MOTO_VERSION=2.2.6
RUN pip install --upgrade moto==$MOTO_VERSION

# renovate: datasource=pypi depName=pandas
ARG PANDAS_VERSION=1.3.2
RUN pip install --upgrade pandas==$PANDAS_VERSION

# renovate: datasource=pypi depName=pyspark
ARG PYSPARK_VERSION=3.1.1
RUN pip install --upgrade pyspark==$PYSPARK_VERSION

# renovate: datasource=pypi depName=pytest
ARG PYTEST_VERSION=6.2.4
RUN pip install --upgrade pytest==$PYTEST_VERSION

# renovate: datasource=pypi depName=pytest-cov
ARG PYTEST_COV_VERSION=2.12.1
RUN pip install --upgrade pytest-cov==$PYTEST_COV_VERSION

# renovate: datasource=pypi depName=pytest-mock
ARG PYTEST_MOCK_VERSION=3.6.1
RUN pip3 install --upgrade pytest-mock==$PYTEST_MOCK_VERSION

# renovate: datasource=pypi depName=PyYAML
ARG PYYAML_VERSION=5.4.1
RUN pip install --upgrade PyYAML==$PYYAML_VERSION

# Install .jar packages
# hadoop-aws has to be version 3.2.0, do not upgrade!
ARG HADOOP_PKG="org.apache.hadoop:hadoop-aws:3.2.0"
ARG DELTALAKE_PKG="io.delta:delta-core_2.12:1.0.0"
ARG AWS_SDK="com.amazonaws:aws-java-sdk-bundle:1.12.62"
# Spark runs ivy to get all of its dependencies (packages). We are executing an "dummy" run to make spark downloads its
# packages. These .jars are saved in '/root/.ivy2/jars/' which we can move to `/usr/lib/spark/jars/` for further use.
RUN spark-submit --packages $DELTALAKE_PKG,$HADOOP_PKG,$AWS_SDK --deploy-mode=client --master=local[1] \
    ${SPARK_HOME}/examples/src/main/python/pi.py
RUN mv /root/.ivy2/jars/* ${SPARK_HOME}/jars

# install minio and minio CLI to root dir
ADD https://dl.min.io/server/minio/release/linux-amd64/minio /opt
ADD https://dl.min.io/client/mc/release/linux-amd64/mc /opt
RUN chmod +x /opt/minio && \
    chmod +x /opt/mc
