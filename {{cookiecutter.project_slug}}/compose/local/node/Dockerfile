FROM node:10-stretch-slim

WORKDIR /app/frontend_react

COPY ./frontend_react/package.json /app/frontend_react

RUN npm install && npm cache clean --force

ENV PATH ./frontend_react/node_modules/.bin/:$PATH
