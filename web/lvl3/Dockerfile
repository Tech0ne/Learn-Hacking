FROM python:3

WORKDIR /lvl3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=1003

EXPOSE 1003

CMD [ "python3", "./main.py" ]