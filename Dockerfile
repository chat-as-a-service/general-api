FROM --platform=linux/amd64 python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src

# Copy the current directory contents into the container at /usr/src/app
COPY ./app /usr/src/app
COPY requirements.txt /usr/src


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Run app.py when the container launches
CMD ["unvicorn", "app.main:app","--host", "0.0.0.0", "--port", "4000"]
# docker buildx build --push -t coldcup2020/wingflo-general-api:v0.1.3 --platform linux/amd64 .