FROM python:3

WORKDIR /lvl1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN gcc main.c -o main

ENV PORT=1102

EXPOSE 1102

CMD [ "python3", "./main.py" ]
