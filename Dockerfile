FROM python:3.8-slim-buster

# Install the security updates.
RUN apt-get update
RUN apt-get -y upgrade

# Install the required dependancies
RUN apt-get install -y libgl1-mesa-glx libgomp1

# Remove all cache file. Get a smaller image
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# Copy the application
COPY . /opt/app
WORKDIR /opt/app

# Install the app libraries
RUN pip install -r requirements.txt

# Start the app
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]