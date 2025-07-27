# Utilise une image Python légère
FROM python:3.12-slim

# Définit le dossier de travail
WORKDIR /app

# Copie les fichiers dans le conteneur
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Lance Uvicorn avec le bon module (main.py est dans ce dossier)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
