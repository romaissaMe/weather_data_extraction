FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the script to the working directory
COPY etl.py /app/etl.py

RUN apt-get update && apt-get -y install cron

COPY crontab /etc/cron.d/crontab

# Give execution rights to the cron job
RUN chmod 0644 /etc/cron.d/crontab

RUN crontab /etc/cron.d/crontab

# Start cron service
CMD cron && tail -f /var/log/cron.log


