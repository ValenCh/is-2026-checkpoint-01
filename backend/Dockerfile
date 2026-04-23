FROM python:3.12-slim

# Crear usuario no-root
RUN useradd -m appuser

WORKDIR /app

# Aprovechar caché de capas de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY app.py .

# Cambiar a usuario sin privilegios
USER appuser

# Healthcheck interno sin dependencias extra
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/api/health')" || exit 1

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]