FROM python:3

WORKDIR /lvl4

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=1004

EXPOSE 1004

CMD [ "python3", "./main.py" ]
