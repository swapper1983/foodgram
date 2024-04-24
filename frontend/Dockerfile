# build env
FROM node:13.12.0-alpine as build
WORKDIR /app
COPY package*.json ./
# RUN npm cache clean --force
# RUN rm -rf node_modules/

RUN rm -rf node_modules
RUN rm -f package-lock.json
RUN npm cache clean --force

RUN npm install
COPY . ./
RUN chmod +x node_modules/.bin/*
RUN npm run build
CMD cp -r build result_build


