FROM ruby:2.6-alpine

# Copy the existing code into the Docker image.
#
# This will copy everything *at build time* (not at runtime), so it is
# still important to use `--mount` to get a reasonable development loop.
# This makes the image work for both purposes, though.
COPY . /code/
WORKDIR /code/

# Install bundler and gems for this project.
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc && \
  apk add --no-cache alpine-sdk && \
  gem update --system && \
  gem install bundler && \
  bundle install && \
  apk del --no-cache alpine-sdk && \
  rm ~/.gemrc

# Install git. (Jekyll expects it.)
RUN apk add --no-cache git

# Expose appropriate ports.
EXPOSE 4000
EXPOSE 35729

# Run Jekyll's dev server.
# Reminder: Use -p with `docker run` to publish ports.
ENTRYPOINT ["bundle", "exec", "jekyll", "serve", \
  "--destination", "/site", \
  "--host", "0.0.0.0"]
