# BugTracker

Aplicación de escritorio en Python con PySide6 (Qt) para gestionar incidencias de software, guardadas en una base de datos SQLite.

| Qué abarca | Dónde |
|---|---|
| Interfaz diseñada en Qt Designer y convertida a Python con `pyside6-uic` | `bugtracker.ui`, `ui_bugtracker.py` |
| Accesibilidad: etiquetas con atajo y *buddy*, orden de tabulación, botones con atajo y *tooltip* | `bugtracker.ui` |
| Acciones Nueva (`Ctrl+N`), Guardar (`Ctrl+S`), Eliminar (`Supr`) y Salir (`Ctrl+Q`) en el menú y la barra de herramientas | `bugtracker.ui`, `main.py` |
| Diálogo modal «Nueva incidencia» que valida el título | `dialogo.py` |
| Tabla con Model/View (`QStandardItemModel` y `QSortFilterProxyModel`), ordenable por columnas | `main.py` |
| Acceso a datos separado de la interfaz: todo el SQL en un módulo | `bd.py` |

## Abrirlo en VS Code

Todas las órdenes van en **PowerShell**.

1. Copia la carpeta `bugtracker` a `C:\dam2627\`. Una ruta corta, fuera de OneDrive, evita errores al instalar.
2. Entra en ella y crea el entorno virtual con sus paquetes:

    ```
    cd C:\dam2627\bugtracker
    python -m venv .venv
    .venv\Scripts\python -m pip install -r requirements.txt
    ```

3. Añade las incidencias de ejemplo (solo la primera vez):

    ```
    .venv\Scripts\python datos_ejemplo.py
    ```

4. Abre la carpeta en VS Code:

    ```
    code .
    ```

    Si VS Code propone instalar la extensión **Python**, acepta. El intérprete de `.venv` ya está elegido en `.vscode/settings.json`.

5. Lanza la aplicación:

    ```
    .venv\Scripts\python main.py
    ```

## Cambiar la interfaz

```
Start-Process .venv\Scripts\pyside6-designer.exe -ArgumentList bugtracker.ui -WindowStyle Hidden
```

Después de guardar en Designer, regenera el código y vuelve a lanzar la aplicación:

```
.venv\Scripts\pyside6-uic bugtracker.ui -o ui_bugtracker.py
.venv\Scripts\python main.py
```
