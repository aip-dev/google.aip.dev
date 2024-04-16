FROM python:3.10-alpine

# Define the working directory.
# Note: There is no code here; it is pulled from the repository by mounting
# the directory (see `serve.sh`).
WORKDIR /code/

# Install Python packages for this project.
COPY requirements.txt /code/requirements.txt
COPY cython_constraint.txt /code/cython_constraint.txt
RUN apk add git
RUN PIP_CONSTRAINT=cython_constraint.txt pip install -r requirements.txt
RUN pip install -r requirements.txt
RUN apk del git

# Set environment variables.
ENV FLASK_DEBUG=True

# Expose appropriate ports.
EXPOSE 4000
EXPOSE 35729

# Run the development server.
# Reminder: Use -p with `docker run` to publish ports (see `serve.sh`).
ENTRYPOINT ["aip-site-serve", "."]
