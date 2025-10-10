FROM node:lts

WORKDIR /app

# COPY remaining project files
COPY . /app

RUN ls -al

# Install packages
RUN npm install

# EXPOSE the port
EXPOSE 3000

ENTRYPOINT [ "npm", "start" ]