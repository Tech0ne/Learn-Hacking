FROM ubuntu

RUN apt-get update
RUN apt-get install -y openssh-server
RUN apt-get -y install sudo
RUN apt-get -y install cron
RUN apt-get -y install vim

RUN mkdir /var/run/sshd

RUN useradd -rm -d /home/user -s /bin/bash -u 1000 user

RUN echo 'user:superpassword' | chpasswd

RUN mkdir /opt/scripts/

RUN chmod 777 /opt/scripts/

RUN echo "sample file" > /opt/scripts/sample_file.txt

RUN chmod 744 /opt/scripts/sample_file.txt

COPY exploit.sh /opt/main.sh

RUN chmod +x /opt/main.sh

COPY crontab /etc/crontab

RUN chmod 644 /etc/crontab

COPY run_me.sh /etc/run_me.sh

RUN chmod +x /etc/run_me.sh

RUN echo "flag{978544600ee6246c1002c3eb5fc6976e}" > /passwd

RUN chown root:root /passwd

RUN chmod 400 /passwd

ENV PORT=1403

RUN echo "Port $PORT" >> /etc/ssh/sshd_config

RUN service ssh start

EXPOSE 1403

CMD ["/etc/run_me.sh"]
