FROM python:3

WORKDIR /lvl3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5555

EXPOSE 5555

CMD [ "python3", "./main.py" ]