FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m appuser
COPY --chown=appuser:appuser app/ .
USER appuser

EXPOSE 5000

CMD ["python", "-u", "app.py"]
