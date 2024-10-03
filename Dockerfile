# Usa una imagen base de Python 3 con Linux
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor
COPY . .

# Instala las dependencias (puedes ajustar esto según tu archivo de requirements.txt)
RUN pip install -r requirements.txt

# Exponer el puerto en el que correrá la app
EXPOSE 8000

# Comando para ejecutar tu aplicación con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]
