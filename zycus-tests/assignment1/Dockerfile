# Centos 6.8 Base
FROM centos:6.8

# Installing Python 2.7 Dependendencies
RUN yum -y update \
    && yum groupinstall -y 'development tools' \
    && yum install -y zlib-dev openssl-devel sqlite-devel bzip2-devel xz-libs wget tar

# Installing Python 2.7
RUN cd /usr/local \
    && wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tar.xz \
    && xz -d Python-2.7.13.tar.xz \
    && tar -xvf Python-2.7.13.tar \
    && cd Python-2.7.13 \
    && ./configure --prefix=/usr/local \
    && make \
    && make altinstall

# Exporting Python2.7 path
ENV PATH "/usr/local/bin:$PATH"

# Installing Java 8 and exporting JAVA HOME
RUN yum install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.121-1.b13.el6.x86_64/

# Download & Installing Apache Tomcat 7
RUN cd /tmp;wget http://mirror.fibergrid.in/apache/tomcat/tomcat-7/v7.0.77/bin/apache-tomcat-7.0.77.tar.gz \
    && tar xvf apache-tomcat-7.0.77.tar.gz  \
    && mv apache-tomcat-7.0.77 /opt/tomcat7 \
    && chmod -R 755 /opt/tomcat7

# Installing EPEL Repository RPM
RUN rpm -Uhv http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

# Installing MongoDB and Starting MongoDB
RUN yum update -y \
    && yum install mongodb* -y \
    && yum clean all \
    && service mongod start \
    && chkconfig mongod on

# Exposing port to external systems
EXPOSE 8080

# Starting Tomcat in foreground mode
CMD ["/opt/tomcat7/bin/catalina.sh", "run"]
