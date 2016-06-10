FROM centos
MAINTAINER Han Gu 
# This docker file creates a image with ansible installed.
# The purpose is to use this ansible to handle maintenance work for MAP, which is within another container
# - restart MAP in case of coreOS reboots

ENV HTTP_PROXY http://proxy2.inf.ise.com:3128
ENV HTTPS_PROXY http://proxy2.inf.ise.com:3128
ENV http_proxy http://proxy2.inf.ise.com:3128
ENV https_proxy http://proxy2.inf.ise.com:3128
ENV proxy http://proxy2.inf.ise.com:3128
ENV DOCKER_HOST tcp://172.17.0.1:2375

ADD docker.repo /etc/yum.repos.d
RUN yum clean all && \
    yum -y install epel-release ansible docker-engine

# pip installation
#wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \
RUN curl -L -O  https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py


# Need to add git clone here to clone the repo where ansible playbooks resides


CMD ["/sbin/init"]