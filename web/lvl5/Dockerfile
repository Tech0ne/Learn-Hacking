FROM python:3

WORKDIR /lvl3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=1005

EXPOSE 1005

CMD [ "python3", "./main.py" ]