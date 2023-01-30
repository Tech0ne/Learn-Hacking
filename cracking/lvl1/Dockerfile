FROM python:3

WORKDIR /lvl1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=1301

EXPOSE 1301

CMD [ "python3", "./main.py" ]
