FROM python:3.8-alpine

# Copy the existing code into the Docker image.
#
# This will copy everything *at build time* (not at runtime), so it is
# still important to use `--mount` to get a reasonable development loop.
# This makes the image work for both purposes, though.
COPY site/requirements.txt /code/site/requirements.txt
WORKDIR /code/site/

# Install Python packages for this project.
RUN pip install -r requirements.txt

# Set environment variables.
ENV PYTHONPATH $PYTHONPATH:/code/site/
ENV FLASK_ENV development

# Expose appropriate ports.
EXPOSE 4000
EXPOSE 35729

# Run Flask's dev server.
# Reminder: Use -p with `docker run` to publish ports.
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "4000"]
