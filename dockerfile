# Usa la imagen oficial de Python como imagen base
FROM python:3.10-slim

# Establece variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instala dependencias del sistema que puedan ser necesarias para tu proyecto (si usas MySQL, por ejemplo)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo el archivo requirements.txt primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Expone el puerto en el que la aplicación de Django ejecutará (ajusta si es necesario)
EXPOSE 8000

# Ejecuta el servidor de desarrollo de Django por defecto (esto se puede cambiar según lo que necesites)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
