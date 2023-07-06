import os
import shutil
from github import Github

# Rutas del proyecto local
project_dir = "/home/xyb3ria/dotfiles"  # Ruta al directorio raíz del proyecto local

# Información de autenticación de GitHub
username = "xyb3ria"
token = "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"

# Información del repositorio en GitHub
repo_url = "https://github.com/xyb3ria/dotfiles"
branch_name = "main"  # Nombre de la rama

# Obtener el nombre del repositorio y propietario desde la URL
repo_owner, repo_name = repo_url.split("/")[-2:]

# Crear un cliente de GitHub y autenticarse con el token
github = Github(username, token)

# Obtener el repositorio
repo = github.get_repo(f"{repo_owner}/{repo_name}")

# Eliminar el contenido del repositorio existente en la rama especificada
contents = repo.get_contents("", ref=branch_name)
for content in contents:
    repo.delete_file(content.path, "Eliminando contenido del repositorio", content.sha, branch=branch_name)

# Copiar los archivos del proyecto al repositorio
for root, dirs, files in os.walk(project_dir):
    for file in files:
        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, project_dir)
        with open(file_path, "rb") as f:
            content = f.read()
        repo.create_file(rel_path, f"Subiendo archivo: {rel_path}", content, branch=branch_name)

print("Proyecto cargado exitosamente en GitHub.")
