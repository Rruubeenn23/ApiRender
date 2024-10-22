# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:13:02 2024

@author: ruben
"""

from flask import Flask, jsonify

app = Flask(__name__)

# Lista 1. 

@app.route('/api/lista1', methods=['GET'])

def obtener_lista1():
    datos = {
        "nombre": "Sebastian", 
        "edad": 19, 
        "residencia": "Seseña"}
    return jsonify(datos)
    
# Lista 2. 

@app.route('/api/lista2', methods=['GET'])

def obtener_lista2():
    lista_datos = [
        {"nombre": "Sebastian", "edad": 19, "residencia": "Seseña"},
        {"nombre": "Javier", "edad": 19, "residencia": "Seseña"},
        {"nombre": "Manu", "edad": 26, "residencia": "Cuidad Real"},
        {"nombre": "Tymur", "edad": 20, "residencia": "Seseña"}]
    return jsonify(lista_datos)

# Ejecutar la API
if __name__ == '__main__':
    app.run(debug=True, port=5001, use_reloader=False)  # Desactivar el reloader automático

    
import subprocess as git
from datetime import datetime

def git_push(repo_path):
    """
    Realiza un commit y un push de todos los cambios en el repositorio local
    de Git.

    Parámetros:
        repo_path (str): Ruta local del repositorio de Git donde se encuentran
        los archivos.

    Esta función realiza los siguientes pasos:
        1. Obtiene la fecha y la hora actuales para incluirlas en el mensaje
        del commit.
        2. Ejecuta los comandos de Git para agregar todos los archivos
        modificados al área de staging.
        3. Realiza un commit con el mensaje que incluye la fecha y hora.
        4. Hace un push de los cambios a la rama principal (main) del
        repositorio remoto en GitHub.

    El commit se realiza con el mensaje: "Actualización dd/mm/aaaa HH:MM".

    Si ocurre algún error durante la ejecución de los comandos Git, se captura
    la excepción y se imprime el mensaje de error.

    Ejemplo de uso: git_push("C:/ruta/al/repositorio")
    """
    try:
        # Obtener la fecha actual en formato dd/mm/aaaa
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")

        # Definir el mensaje del commit (mensaje de subida)
        commit_message = f"Actualización {fecha_actual}"

        # Agregar todos los archivos modificados (solo agregamos archivos
        # modificados después del anterior commit)
        git.run(["git", "add", "."], check=True, cwd=repo_path)

        # Hacer el commit con el mensaje que incluye la fecha
        git.run(["git", "commit", "-m", commit_message], check=True,
                        cwd=repo_path)

        # Subir los cambios a la rama principal (main)
        git.run(["git", "push", "-u", "origin", "main"], check=True,
                        cwd=repo_path)

        print(f"Commit realizado con el mensaje: '{commit_message}'")
        print("Archivos subidos a GitHub correctamente.")

    except git.CalledProcessError as e:
        print(f"Error durante la ejecución de Git: {e}")

# Ruta a tu repositorio local (¡DEL ORDENADOR!)
repo_path = r"C:\\Users\\ruben\\Documents\\2ºDAM\\Desarrollo de Interfaces\\Desarrollo de Interfaces Python"  

# Llamada a la función para subir los archivos
git_push(repo_path)

import subprocess as git
from datetime import datetime

def git_push(repo_path):
    """
    Realiza un commit y un push de todos los cambios en el repositorio local
    de Git.

    Parámetros:
        repo_path (str): Ruta local del repositorio de Git donde se encuentran
        los archivos.

    Esta función realiza los siguientes pasos:
        1. Obtiene la fecha y la hora actuales para incluirlas en el mensaje
        del commit.
        2. Ejecuta los comandos de Git para agregar todos los archivos
        modificados al área de staging.
        3. Realiza un commit con el mensaje que incluye la fecha y hora.
        4. Hace un push de los cambios a la rama principal (main) del
        repositorio remoto en GitHub.

    El commit se realiza con el mensaje: "Actualización dd/mm/aaaa HH:MM".

    Si ocurre algún error durante la ejecución de los comandos Git, se captura
    la excepción y se imprime el mensaje de error.

    Ejemplo de uso: git_push("C:/ruta/al/repositorio")
    """
    try:
        # Obtener la fecha actual en formato dd/mm/aaaa
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")

        # Definir el mensaje del commit (mensaje de subida)
        commit_message = f"Actualización {fecha_actual}"

        # Agregar todos los archivos modificados (solo agregamos archivos
        # modificados después del anterior commit)
        git.run(["git", "add", "."], check=True, cwd=repo_path)

        # Hacer el commit con el mensaje que incluye la fecha
        git.run(["git", "commit", "-m", commit_message], check=True,
                        cwd=repo_path)

        # Subir los cambios a la rama principal (main)
        git.run(["git", "push", "-u", "origin", "main"], check=True,
                        cwd=repo_path)

        print(f"Commit realizado con el mensaje: '{commit_message}'")
        print("Archivos subidos a GitHub correctamente.")

    except git.CalledProcessError as e:
        print(f"Error durante la ejecución de Git: {e}")

# Ruta a tu repositorio local (¡DEL ORDENADOR!)
repo_path = r"C:\\Users\\ruben\\Documents\\2ºDAM\\Desarrollo de Interfaces\\Desarrollo de Interfaces Python"  

# Llamada a la función para subir los archivos
git_push(repo_path)

