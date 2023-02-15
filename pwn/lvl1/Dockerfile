FROM ubuntu

RUN apt-get update
RUN apt-get install -y openssh-server
RUN apt-get -y install sudo
RUN apt-get -y install cron
RUN apt-get -y install vim

RUN mkdir /var/run/sshd

RUN useradd -rm -d /home/user -s /bin/bash -u 1000 user

RUN echo 'user:superpassword' | chpasswd

RUN echo "user ALL = (root) ALL" > /etc/sudoers.d/user

RUN echo "flag{e97454f3336c2cbab7eba9e66f4ae24a}" > /passwd

RUN chown root:root /passwd

RUN chmod 400 /passwd

ENV PORT=1401

RUN echo "Port $PORT" >> /etc/ssh/sshd_config

RUN service ssh start

EXPOSE 1401

CMD ["/usr/sbin/sshd","-D"]
