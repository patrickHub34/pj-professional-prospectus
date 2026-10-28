FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir plotly==5.24.1

COPY pj_prospectus.py .

# Generate index.html during build
RUN python pj_prospectus.py

EXPOSE 8080

# Serve index.html on port 8080
CMD ["python", "-m", "http.server", "8080"]