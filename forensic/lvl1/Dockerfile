FROM python:3

WORKDIR /lvl1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=1201

EXPOSE 1201

CMD [ "python3", "./main.py" ]
