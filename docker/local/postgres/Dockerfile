# FROM postgres:15-bullseye


# RUN COPY /docker/local/postgres/maintenance /usr/local/bin/maintenance

# RUN chmod +x /usr/local/bin/maintenance/*

# RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
#       && rmdir /usr/local/bin/maintenance

FROM postgres:15-bullseye

# Copy the maintenance scripts into the container
COPY /docker/local/postgres/maintenance /usr/local/bin/maintenance
 
# Make all scripts in the maintenance directory executable
RUN chmod +x /usr/local/bin/maintenance/*

# Move all scripts to /usr/local/bin and remove the maintenance directory
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance

  