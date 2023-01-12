FROM python:3

WORKDIR /lvl2

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5000

EXPOSE 8080

CMD [ "python3", "./main.py" ]