FROM ubuntu

RUN apt-get update
RUN apt-get install -y openssh-server
RUN apt-get -y install sudo
RUN apt-get -y install cron
RUN apt-get -y install vim

RUN mkdir /var/run/sshd

RUN useradd -rm -d /home/user -s /bin/bash -u 1000 user

RUN echo 'user:superpassword' | chpasswd

RUN setcap cap_setuid+ep /usr/bin/python3

RUN echo "flag{46722dd32216ea2ec74abdf98e6cf1b4}" > /passwd

RUN chown root:root /passwd

RUN chmod 400 /passwd

ENV PORT=1405

RUN echo "Port $PORT" >> /etc/ssh/sshd_config

RUN service ssh start

EXPOSE 1405

CMD ["/usr/sbin/sshd","-D"]
