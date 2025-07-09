# Use the official Node.js 18 image as the base
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install all npm dependencies
RUN npm install

# Build the React app for production (optional if using 'npm start' for development)
RUN npm run build

# Expose port 3000 (default for React development server)
EXPOSE 3000

# Start the React development server
CMD ["npm", "start"]
