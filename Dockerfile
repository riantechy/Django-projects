# Use the official Node.js 14 Alpine image as the base image
FROM node:14-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install production dependencies using npm
RUN npm install --production

# Copy the entire project directory to the working directory
COPY . .

# Clear the npm cache forcefully
RUN npm cache clear --force

# Define the default command to start your application
CMD ["npm", "start"]
