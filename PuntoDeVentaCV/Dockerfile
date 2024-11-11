# Usar la imagen oficial de Python como base
FROM python:3.12-slim

# Instalar dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev-compat \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos al contenedor
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto al contenedor
COPY . .

# Exponer el puerto en el que corre el servidor Django
EXPOSE 8000

# Comando para ejecutar el servidor Django cuando el contenedor inicie
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]