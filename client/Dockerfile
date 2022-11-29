# pull official base image
FROM node:18-alpine

WORKDIR /usr/src/app

RUN npm install -g @vue/cli
RUN npm install -g @vue/cli-service-global

ENV HOST 0.0.0.0
EXPOSE 8888