# build env
FROM node:13.12.0-alpine as build
# FROM node:18
# FROM node:10.5.2-alpine as build
WORKDIR /app
# COPY package*.json ./
# # RUN npm cache clean --force
# # RUN rm -rf node_modules/

# RUN rm -rf node_modules
# RUN rm -f package-lock.json
# RUN npm cache clean --force

# # ENV API_URL https://python.nomoredomainsrocks.ru
# # RUN npm ci

# RUN npm install
# COPY . ./
# RUN chmod +x node_modules/.bin/*
# RUN npm run build
# CMD cp -r build result_build


COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

COPY . .
RUN npm run build


# COPY . .
# RUN npm run build
# CMD cp -r /app/build/. /static/