FROM python:3

WORKDIR /lvl1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=1001

EXPOSE 1001

CMD [ "python3", "./main.py" ]