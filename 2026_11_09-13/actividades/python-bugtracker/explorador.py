"""Explorador del BugTracker: un programa de terminal que lee los archivos del proyecto
y su base de datos para sacar información.

Va en la misma carpeta que main.py. Uso:
    python explorador.py                       ayuda
    python explorador.py archivos              qué archivos hay y para qué sirve cada uno
    python explorador.py estructura            clases y funciones de cada archivo .py
    python explorador.py dependencias          qué archivo importa a cuál
    python explorador.py incidencias [ESTADO]  resumen de la base de datos
    python explorador.py informe               guarda todo en informes/informe.txt
"""
# ----------------------------------------------------------------------------
# 1. Importar módulos
# ----------------------------------------------------------------------------
import os          # archivos y carpetas del sistema operativo
import sys         # el propio intérprete: argumentos, salida, rutas de búsqueda
import sqlite3     # para reconocer los errores de la base de datos

import bd          # bd.py, de esta misma carpeta: Python la encuentra por sys.path[0]

# La carpeta donde está este archivo (la del proyecto), se ejecute desde donde se ejecute.
CARPETA = os.path.dirname(os.path.abspath(__file__))

# Para qué sirve cada archivo. Es un diccionario: nombre del archivo -> descripción.
DESCRIPCIONES = {
    "main.py": "Programa principal: la ventana, sus botones y acciones. Une todo lo demás",
    "bugtracker.ui": "Diseño de la ventana hecho con Qt Designer (XML). No se ejecuta",
    "ui_bugtracker.py": "Código generado a partir de bugtracker.ui con pyside6-uic. No se edita a mano",
    "dialogo.py": "Diálogo «Nueva incidencia» / «Editar incidencia»",
    "buscador.py": "Componente reutilizable Buscador (2.ª parte del proyecto)",
    "bd.py": "Acceso a la base de datos: todo el SQL está aquí",
    "bugtracker.db": "La base de datos SQLite. La crea bd.crear_bd() la primera vez",
    "datos_ejemplo.py": "Añade incidencias de ejemplo a la base de datos",
    "test_buscador.py": "Pruebas automáticas del Buscador (pytest)",
    "requirements.txt": "Librerías que hay que instalar con pip",
    "explorador.py": "Este programa",
}


# ----------------------------------------------------------------------------
# 2. Clases: un archivo cualquiera y, heredando de él, un archivo de Python
# ----------------------------------------------------------------------------
class Archivo:
    """Un archivo de la carpeta del proyecto."""

    def __init__(self, nombre):
        self.nombre = nombre                              # atributos: datos de cada objeto
        self.ruta = os.path.join(CARPETA, nombre)
        self.tamano = os.path.getsize(self.ruta)          # en bytes

    def descripcion(self):
        return DESCRIPCIONES.get(self.nombre, "(sin descripción)")

    def __str__(self):                                    # lo que sale al hacer print(objeto)
        return f"{self.nombre:<20} {self.tamano:>7} bytes  {self.descripcion()}"


class ArchivoPython(Archivo):
    """Un archivo .py: además de lo de Archivo, sabe leer sus clases, funciones e imports."""

    def __init__(self, nombre):
        super().__init__(nombre)                          # primero, lo que hace Archivo
        with open(self.ruta, encoding="utf-8") as f:
            self.lineas = f.readlines()                   # lista con las líneas del archivo

    def clases(self):
        """Diccionario: cada clase, con la clase de la que hereda entre paréntesis -> lista de sus métodos."""
        resultado = {}
        clase_actual = None
        for linea in self.lineas:
            if linea.startswith("class "):
                clase_actual = linea[6:].split(":")[0].strip()      # "VentanaPrincipal(QMainWindow)"
                resultado[clase_actual] = []
            elif linea.startswith("    def ") and clase_actual:
                resultado[clase_actual].append(linea.strip()[4:].split("(")[0])
            elif linea.startswith("def "):
                clase_actual = None
        return resultado

    def funciones(self):
        """Funciones que no están dentro de una clase."""
        return [linea[4:].split("(")[0] for linea in self.lineas if linea.startswith("def ")]

    def importa(self):
        """Módulos que importa este archivo."""
        modulos = []
        for linea in self.lineas:
            if linea.startswith("import "):
                modulos.append(linea.split()[1])
            elif linea.startswith("from "):
                modulos.append(linea.split()[1])
        return modulos

    def __str__(self):
        return super().__str__() + f"  ({len(self.lineas)} líneas)"


def leer_archivos():
    """Crea un objeto por cada archivo de la carpeta, del tipo que le corresponde."""
    archivos = []
    for nombre in sorted(os.listdir(CARPETA)):
        if os.path.isdir(os.path.join(CARPETA, nombre)):
            continue                                      # las carpetas no se cuentan
        if nombre.endswith(".py"):
            archivos.append(ArchivoPython(nombre))
        else:
            archivos.append(Archivo(nombre))
    return archivos


# ----------------------------------------------------------------------------
# 3. Una función por orden: cada una devuelve una lista de líneas de texto
# ----------------------------------------------------------------------------
def orden_archivos():
    lineas = [f"Carpeta del proyecto: {CARPETA}", ""]
    for archivo in leer_archivos():
        lineas.append(str(archivo))
    return lineas


def orden_estructura():
    lineas = []
    for archivo in leer_archivos():
        if not isinstance(archivo, ArchivoPython):
            continue
        lineas.append(f"{archivo.nombre}")
        for clase, metodos in archivo.clases().items():
            lineas.append(f"    clase {clase}: {', '.join(metodos) or '(sin métodos)'}")
        for funcion in archivo.funciones():
            lineas.append(f"    función {funcion}")
    return lineas


def orden_dependencias():
    archivos = [a for a in leer_archivos() if isinstance(a, ArchivoPython)]
    propios = [a.nombre[:-3] for a in archivos]           # "bd.py" -> "bd"
    lineas = []
    for archivo in archivos:
        del_proyecto = [m for m in archivo.importa() if m in propios]
        externos = [m for m in archivo.importa() if m not in propios]
        lineas.append(f"{archivo.nombre:<20} usa {', '.join(del_proyecto) or '-'}"
                      f"   |   librerías: {', '.join(externos) or '-'}")
    return lineas


def contar(incidencias, campo):
    """Cuenta cuántas incidencias hay de cada valor de un campo: {'Pendiente': 3, ...}."""
    cuenta = {}
    for incidencia in incidencias:
        valor = incidencia[campo]
        cuenta[valor] = cuenta.get(valor, 0) + 1
    return cuenta


def orden_incidencias(estado=None):
    if not os.path.exists(bd.RUTA_BD):
        return ["No hay base de datos. Créala con: python datos_ejemplo.py"]
    try:
        incidencias = bd.obtener_incidencias()
    except sqlite3.Error as error:
        return [f"No se ha podido leer la base de datos: {error}"]

    lineas = [f"Base de datos: {bd.RUTA_BD}", f"Incidencias: {len(incidencias)}", ""]
    for campo in ("estado", "prioridad", "tipo"):
        lineas.append(f"Por {campo}:")
        for valor, numero in contar(incidencias, campo).items():
            lineas.append(f"    {valor:<20} {numero}")
    if estado:
        lineas += ["", f"Incidencias en estado «{estado}»:"]
        elegidas = [i for i in incidencias if i["estado"] == estado]
        for i in elegidas:
            lineas.append(f"    #{i['id']} [{i['prioridad']}] {i['titulo']}")
        if not elegidas:
            lineas.append("    (ninguna)")
    return lineas


def orden_informe():
    carpeta = os.path.join(CARPETA, "informes")
    os.makedirs(carpeta, exist_ok=True)                   # crea la carpeta si no existe
    ruta = os.path.join(carpeta, "informe.txt")
    partes = [("ARCHIVOS", orden_archivos()), ("ESTRUCTURA", orden_estructura()),
              ("DEPENDENCIAS", orden_dependencias()), ("INCIDENCIAS", orden_incidencias())]
    with open(ruta, "w", encoding="utf-8") as f:
        for titulo, lineas in partes:
            f.write(f"== {titulo} ==\n" + "\n".join(lineas) + "\n\n")
    return [f"Informe guardado en {ruta}"]


ORDENES = {
    "archivos": orden_archivos,
    "estructura": orden_estructura,
    "dependencias": orden_dependencias,
    "incidencias": orden_incidencias,
    "informe": orden_informe,
}


# ----------------------------------------------------------------------------
# 4. Programa principal: lee los argumentos con sys.argv
# ----------------------------------------------------------------------------
def main():
    # sys.argv es la lista de lo escrito en la orden:
    # python explorador.py incidencias Pendiente  ->  ['explorador.py', 'incidencias', 'Pendiente']
    if len(sys.argv) < 2 or sys.argv[1] not in ORDENES:
        print(__doc__)                                    # el texto del principio del archivo
        print(f"sys.argv = {sys.argv}")
        sys.exit(1)                                       # termina indicando que algo no fue bien

    orden = ORDENES[sys.argv[1]]
    if sys.argv[1] == "incidencias" and len(sys.argv) > 2:
        lineas = orden(sys.argv[2])
    else:
        lineas = orden()
    print("\n".join(lineas))


if __name__ == "__main__":                                # solo si se ejecuta, no si se importa
    main()
