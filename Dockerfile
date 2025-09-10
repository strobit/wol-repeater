FROM node:lts-alpine

WORKDIR /app

RUN apk update 
RUN apk add git python3
RUN git clone https://github.com/strobit/wol-repeater
WORKDIR /app/wol-repeater
ENV ENV_ADDR=192.168.1.100
ENV ENV_BROADCAST=192.168.1.255
ENV ENV_PORT=9
CMD ["python3", "-u", "wol-repeater.py"]

EXPOSE 9/udp
