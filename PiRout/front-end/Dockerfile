FROM node:20-alpine
WORKDIR /app
COPY package.json vite.config.js ./
COPY src ./src
RUN npm install
RUN npm run build
RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "80"]
