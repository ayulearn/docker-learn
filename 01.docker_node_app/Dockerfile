FROM node:lts-alpine3.15
WORKDIR /node_app
COPY  /home/ayu/Desktop/docker_bret/node_app /node_app /node_app/
# this 👆 command can be written as
#COPY . ./ #
RUN npm install
EXPOSE 80
CMD ["node", "server.js"]

