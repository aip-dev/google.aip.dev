FROM python:3.8-alpine

# Define the working directory.
# Note: There is no code here; it is pulled from the repository by mounting
# the directory (see `serve.sh`).
WORKDIR /code/

# Install Python packages for this project.
COPY requirements.txt /code/requirements.txt
RUN apk add git && \
  pip install -r requirements.txt && \
  apk del git

# Set environment variables.
ENV FLASK_ENV development

# Expose appropriate ports.
EXPOSE 4000
EXPOSE 35729

# Run the development server.
# Reminder: Use -p with `docker run` to publish ports (see `serve.sh`).
ENTRYPOINT ["aip-site-serve", "."]
