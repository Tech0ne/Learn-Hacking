FROM ubuntu

RUN apt-get update
RUN apt-get install -y openssh-server
RUN apt-get -y install sudo
RUN apt-get -y install cron
RUN apt-get -y install gcc

RUN mkdir /var/run/sshd

RUN useradd -rm -d /home/user -s /bin/bash -u 1000 user

RUN echo 'user:superpassword' | chpasswd

COPY suid.c /tmp/suid.c

RUN gcc -o /opt/script /tmp/suid.c

RUN rm /tmp/suid.c

RUN chmod u+s /opt/script

RUN echo "flag{88779f61f6b33963d0430bdf69c1622d}" > /passwd

RUN chown root:root /passwd

RUN chmod 400 /passwd

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]