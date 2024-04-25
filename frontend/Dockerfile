# build env
FROM node:13.12.0-alpine as build
WORKDIR /app
COPY package*.json ./

# RUN npm install
RUN npm install react-scripts --save

RUN chmod +x node_modules/.bin/react-scripts
# ERROR: failed to solve: process "/bin/sh -c npm run build" did not complete successfully: exit code: 126
COPY . ./
RUN npm run build
CMD cp -r build result_build
