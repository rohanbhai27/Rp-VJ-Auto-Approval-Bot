# Don't Remove Credit @RnpUpdate
# Subscribe YouTube Channel For Amazing Bot @RnpDeveloper
# Ask Doubt on telegram @MrRnp

FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 bot.py
