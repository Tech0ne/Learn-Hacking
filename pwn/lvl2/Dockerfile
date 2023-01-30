FROM ubuntu

RUN apt-get update
RUN apt-get install -y openssh-server
RUN apt-get -y install sudo
RUN apt-get -y install cron
RUN apt-get -y install vim

RUN mkdir /var/run/sshd

RUN useradd -rm -d /home/user -s /bin/bash -u 1000 user

RUN echo 'user:superpassword' | chpasswd

RUN chmod +s /usr/bin/tail

RUN echo "flag{5f65074b48ad8eed5645b376f2c483e0}" > /passwd

RUN chown root:root /passwd

RUN chmod 400 /passwd

ENV PORT=1402

RUN echo "Port $PORT" >> /etc/ssh/sshd_config

EXPOSE 1402

CMD ["/usr/sbin/sshd","-D"]
