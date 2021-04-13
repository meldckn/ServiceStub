FROM python:3.8

# Test this Dockerfile locally by running `docker build -t app .`
# followed by `docker run -p 8000:8000 app`. Can then hit endpoint
# http://localhost:8000

# Make and set working directory for subsequent instructions
RUN mkdir -p /App
WORKDIR /App

# Copy app source
COPY . .

# Install python packages
RUN pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED True

# Execute the service (use 0.0.0.0 to bind on all available interfaces,
# including localhost/127.0.0.1 -- won't work to bind localhost directly?)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "launcher:app"]
