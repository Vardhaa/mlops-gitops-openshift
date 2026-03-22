FROM python:3.11-slim AS builder 
WORKDIR /app 
COPY requirements.txt . 
RUN pip install --no-cache-dir --upgrade pip 
 
FROM python:3.11-slim AS runtime 
RUN useradd -m -u 1001 appuser 
WORKDIR /app 
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages 
COPY --from=builder /usr/local/bin /usr/local/bin 
COPY serve/app.py . 
RUN chown -R 1001:0 /app 
USER 1001 
ENV APP_ENV=dev 
ENV MODEL_NAME=distilbert-base-uncased-finetuned-sst-2-english 
ENV LOG_LEVEL=INFO 
EXPOSE 8080 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"] 
