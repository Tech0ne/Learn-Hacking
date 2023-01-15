FROM ubuntu

# flag will be in /passwd or in /root/*.txt

RUN apt-get update && apt-get install -y openssh-server && apt-get -y install sudo

RUN mkdir /var/run/sshd

RUN useradd -rm -d /home/user -s /bin/bash -u 1000 user

RUN echo 'user:hellossh' | chpasswd

RUN echo "user ALL = (root) ALL" > /etc/sudoers.d/user

RUN echo "flag{e97454f3336c2cbab7eba9e66f4ae24a}" > /passwd

RUN chown root:root /passwd

RUN chmod 400 /passwd

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]