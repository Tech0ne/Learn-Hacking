FROM ubuntu:22.04

WORKDIR /app/

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y gcc socat

COPY exploit.c /app/exploit.c

RUN gcc -w -O0 -g3 -o /app/main /app/exploit.c

ENV PORT=1401

EXPOSE 1401

CMD [ "socat", "TCP-LISTEN:$PORT,reuseaddr,fork", "EXEC:/app/main,pty,stderr" ]
