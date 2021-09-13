FROM node:latest
WORKDIR /usr/src/project/
COPY ./project/package*.json ./
RUN npm install
COPY ./project .


#FROM node:latest as build-stage
#WORKDIR /app
#COPY ./project/package*.json ./
#RUN npm install
#COPY ./project/ .
#RUN npm run build
#
#FROM nginx as production-stage
#WORKDIR /app
#COPY --from=build-stage /app/dist /app
#COPY nginx.conf /etc/nginx/nginx.conf