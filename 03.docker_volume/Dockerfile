FROM node:lts-alpine3.15
WORKDIR /node_app
COPY package.json /node_app/
RUN npm install
COPY . /node_app/
VOLUME [ "/node_app/node_modules" ]
VOLUME [ "/node_app/temp" ]
EXPOSE 80
CMD ["npm", "start"]