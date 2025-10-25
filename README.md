# COMMANDS
# Builds a Docker image from the Dockerfile in the current folder 
docker build -t back-fastapi . 

# Lists all currently running Docker containers. 
docker ps

# Runs the container from the back-fastapi image in detached mode
docker run -d -p 8000:8000 back-fastapi 

# Runs the container in the foreground attached to your terminal
docker run -p 8000:8000 back-fastapi

# Lists all containers including those that have stopped or exited, helping you see the complete history of container activity on your system.
docker ps -a 

# Build docker file 
docker build -t back-fastapi .

# To activate the .venv file
poetry shell 

# Extensions used for this project
Python, Python Debugger et Pylance

# Dependencies installed 
poetry init
poetry config virtualenvs.in-project true --local
poetry add fastapi
poetry add uvicorn

# To be able to run the project 
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# or this 
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
