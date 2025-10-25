# write a dockerfile for a vite project 

# Based on Alpine for efficiency and security
FROM alpine:3.19

WORKDIR /app
COPY . .

ENV NODE_ENV=production

# Add if you're also using Vite backends
ENV VITE-FRONT-END=YES 

# Important system binaries
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        rm -rf /var/lib/apt/lists/ \
        node@18.20.3 \
        gcc \
        build-essential \
        && rm -rf /var/log

# Vite dependencies
RUN npm install -D @vite/vite vortext express postcss --save

# Express.js is included in Node 16+
RUN npm install -g express --production

# Mount the source code for development
VOLCDIR /app/src
COPY . into /app/src --shallow

# Copy test files (if needed)
COPY * -f /app/test-project

# Expose Vite node commands
EXPOSE 16485-16920:node_modules,17323-17453:bin

# Build the image with production settings
CMD ["vite", "build", "--no-cache"]