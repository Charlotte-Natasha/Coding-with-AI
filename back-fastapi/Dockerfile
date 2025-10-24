##dockerfile

# Use the official node image as a base
FROM python:3.12-slim

# Set working directory to /app
WORKDIR /app

# Copy package*.json files to /app
COPY pyproject.toml poetry.lock ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev

# Copy source code from current directory to /app
COPY . .

# Run vite command when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]