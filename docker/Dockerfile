FROM python:3.11-slim

RUN useradd -m appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries= \ 
    CMD python -c "import urlib.request; urlib.request.urlopen('http://localhost:8000/health')"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# requirements.txt:
# fastapi==0.110.0
# uvicorn==0.29.0
# pydantic==2.6.4
# httpx==0.27.0
# pytest==8.1.1