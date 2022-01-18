FROM node:lts-alpine3.15
WORKDIR /backend 
COPY package.json /backend/
RUN npm install
COPY . .
EXPOSE 80
ENV MONGODB_U=root
ENV MONGODB_P=Ayu321
CMD ["npm", "start"]