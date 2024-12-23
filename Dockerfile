# Use the official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy any requirements.txt file if you have dependencies
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the default command to open an interactive shell
CMD ["python", "setup.py"]

