FROM python:3.8

# Set the working directory
WORKDIR /action

# Copy the Python script into the container
COPY entrypoint.py /action/entrypoint.py

# Install required dependencies
RUN pip install json2table

# Run the Python script as the entry point
ENTRYPOINT ["python", "/action/entrypoint.py"]
