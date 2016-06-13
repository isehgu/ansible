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
ENV DOCKER_HOST tcp://td-tac01.test.ise.com:2375

#ADD docker.repo /etc/yum.repos.d
RUN mkdir /root/.ssh && \
    chmod 700 /root/.ssh

ADD config /root/.ssh/

# RUN mv /opt/ansible/ansible /root/.ssh; \
#     mv /opt/ansible/ansible.pub /root/.ssh

RUN yum clean all && \
    yum -y install epel-release && \
    #yum -y install ansible docker-engine-0:1.10.3-1.el7.centos.x86_64 git
    yum -y install ansible 

# pip installation
#wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \
RUN curl -L -O  https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py


# Need to add git clone here to clone the repo where ansible playbooks resides


CMD ["/sbin/init"]