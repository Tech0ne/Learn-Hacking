FROM python:3

WORKDIR /lvl1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN gcc -O0 main.c -o main

ENV PORT=1101

EXPOSE 1101

CMD [ "python3", "./main.py" ]
