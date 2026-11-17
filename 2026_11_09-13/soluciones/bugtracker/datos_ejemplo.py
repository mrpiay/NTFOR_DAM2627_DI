"""Añade unas incidencias de ejemplo para probar la tabla, el filtro y la usabilidad.

Ejecútalo una sola vez:  python datos_ejemplo.py
"""
import bd

EJEMPLOS = [
    ("El botón Guardar no responde", "Error", "Alta", "Pendiente",
     "Al pulsar Guardar con el título vacío no pasa nada."),
    ("Exportar a CSV", "Nueva funcionalidad", "Media", "Pendiente",
     "Poder exportar la lista de incidencias a un archivo CSV."),
    ("Mejorar el contraste de la tabla", "Mejora", "Baja", "En proceso",
     "El texto gris claro se lee mal."),
    ("Error al abrir la base de datos", "Error", "Crítica", "Resuelta",
     "Fallaba si la carpeta tenía tildes."),
    ("Atajo de teclado para eliminar", "Mejora", "Media", "Pendiente",
     "Que la tecla Supr elimine la incidencia seleccionada."),
]

if __name__ == "__main__":
    bd.crear_bd()
    for incidencia in EJEMPLOS:
        bd.insertar_incidencia(*incidencia)
    print(f"Añadidas {len(EJEMPLOS)} incidencias de ejemplo.")
