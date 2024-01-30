#image
FROM node:14

#dir inside container to host app code
WORKDIR /usr/src/app

# copy app code
COPY /Users/namrata/Desktop/frontend .

# install dependencies
RUN npm install -g http-server

# port app runs on
EXPOSE 80

# command
CMD ["http-server", "-p", "80"]