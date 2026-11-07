"""Acceso a la base de datos SQLite del BugTracker.

Aquí está todo el SQL. Este módulo no usa widgets de Qt: si algo falla,
lanza sqlite3.Error y es main.py quien muestra el mensaje.
"""
import sqlite3
from pathlib import Path

# La base de datos se guarda junto a este archivo, se ejecute desde donde se ejecute.
RUTA_BD = Path(__file__).with_name("bugtracker.db")


def conectar():
    conexion = sqlite3.connect(RUTA_BD)
    conexion.row_factory = sqlite3.Row   # acceso por nombre: fila["titulo"]
    return conexion


def crear_bd():
    conexion = conectar()
    try:
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS incidencias (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo      TEXT NOT NULL,
                tipo        TEXT NOT NULL,
                prioridad   TEXT NOT NULL,
                estado      TEXT NOT NULL,
                descripcion TEXT
            )
        """)
        conexion.commit()
    finally:
        conexion.close()


def obtener_incidencias():
    conexion = conectar()
    try:
        cursor = conexion.execute(
            "SELECT id, titulo, tipo, prioridad, estado, descripcion "
            "FROM incidencias ORDER BY id"
        )
        return cursor.fetchall()
    finally:
        conexion.close()


def obtener_incidencia(id_incidencia):
    """Devuelve una sqlite3.Row o None si no existe."""
    conexion = conectar()
    try:
        cursor = conexion.execute(
            "SELECT id, titulo, tipo, prioridad, estado, descripcion "
            "FROM incidencias WHERE id = ?",
            (id_incidencia,)
        )
        return cursor.fetchone()
    finally:
        conexion.close()


def insertar_incidencia(titulo, tipo, prioridad, estado, descripcion):
    conexion = conectar()
    try:
        conexion.execute(
            "INSERT INTO incidencias (titulo, tipo, prioridad, estado, descripcion) "
            "VALUES (?, ?, ?, ?, ?)",
            (titulo, tipo, prioridad, estado, descripcion)
        )
        conexion.commit()
    finally:
        conexion.close()


def actualizar_incidencia(id_incidencia, titulo, tipo, prioridad, estado, descripcion):
    conexion = conectar()
    try:
        conexion.execute(
            """UPDATE incidencias
               SET titulo = ?, tipo = ?, prioridad = ?, estado = ?, descripcion = ?
               WHERE id = ?""",
            (titulo, tipo, prioridad, estado, descripcion, id_incidencia)
        )
        conexion.commit()
    finally:
        conexion.close()


def eliminar_incidencia(id_incidencia):
    conexion = conectar()
    try:
        conexion.execute("DELETE FROM incidencias WHERE id = ?", (id_incidencia,))
        conexion.commit()
    finally:
        conexion.close()
