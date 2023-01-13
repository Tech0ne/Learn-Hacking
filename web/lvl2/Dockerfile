FROM python:3

WORKDIR /lvl2

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=1002

EXPOSE 1002

CMD [ "python3", "./main.py" ]