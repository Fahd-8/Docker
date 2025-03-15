# Use a slim version of Python
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Expose the port that Flask will run on
EXPOSE 5000

# Set Flask app environment variable
# Set Flask app environment variable
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["python", "app.py"]
