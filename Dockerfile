FROM python:3.12-alpine

# Install nginx
RUN apk add --no-cache nginx


WORKDIR .


COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# Copy the main nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8000


# Start Nginx and Uvicorn
CMD ["sh", "-c", "nginx && uvicorn main:app --host 0.0.0.0 --port 8000 --proxy-headers"]