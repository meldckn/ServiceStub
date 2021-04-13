
Starter code for a basic Python microservice that can respond to HTTP requests. Uses Falcon, a framework for making HTTP APIs, and Gunicorn to run a server in the Docker container. 

## Run Python service locally

Requirements: Python 3, Falcon 3.

1. Install Falcon (3.0+): `pip3 install falcon` (If you have an earlier version already installed, consider following the virtual environment instructions below.)

2. Run script: `python3 launcher.py`

3. Visit the URL printed on the command line (e.g., localhost:8000), with or without extra route data (localhost:8000/generate). Either visit the URL in your web browser to test supported HTTP GET requests, or use as the request URL in something like Postman or CURL, for non-GET requests.

4. Control-C to stop launcher.py

### Using a virtual environment

If you have a lot of other Python projects using different versions of dependencies like Falcon, consider running the project in a virtual environment (so it uses its own dependencies and versions, regardless of others installed on your computer).

1. [First-time setup only] Create a virtual environment from this project directory using the `venv` module for Python3, which comes with the Python3 standard library: `python3 -m venv env`. This will create a folder called `env` (which should always be `.gitignore`'d).

2. Activate the virtual environment: `source env/bin/activate`

3. [First-time setup only, or if dependencies change] Install dependencies: `python3 -m pip install -r requirements.txt`

4. Run script: `python3 launcher.py`

5. Visit the URL printed on the command line (e.g., localhost:8000) in your web browser (to test supported HTTP GET requests), or input as the request URL in something like Postman (for non-GET requests).

6. Ctrl-C to stop launcher.py

7. Leave the virtual environment: `deactivate`

## Build and run service as a Docker container

Requires Docker.

1. Build the Docker image with: `docker build -t app .` (Tag it with the name "app" so we can reference it in the run command. And search in the current directory for the Dockerfile.)

2. Run the newly built image with: `docker run -p 8000:8000 app` (`-p` to expose container port 8000 to port 8000 of the host machine.)

3. Hit endpoint http://localhost:8000 by visiting it in your web browser or using as the request URL in Postman or Curl.
