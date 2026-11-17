# BugTracker

Aplicación de escritorio en Python con PySide6 (Qt) para gestionar incidencias de software, guardadas en una base de datos SQLite.

| Qué abarca | Dónde |
|---|---|
| Interfaz diseñada en Qt Designer y convertida a Python con `pyside6-uic` | `bugtracker.ui`, `ui_bugtracker.py` |
| Accesibilidad: etiquetas con atajo y *buddy*, orden de tabulación, botones con atajo y *tooltip* | `bugtracker.ui` |
| Acciones Nueva (`Ctrl+N`), Guardar (`Ctrl+S`), Eliminar (`Supr`) y Salir (`Ctrl+Q`) en el menú y la barra de herramientas | `bugtracker.ui`, `main.py` |
| Diálogo modal «Nueva incidencia» que valida el título | `dialogo.py` |
| Tabla con Model/View (`QStandardItemModel` y `QSortFilterProxyModel`) | `main.py` |
| Acceso a datos separado de la interfaz: todo el SQL en un módulo | `bd.py` |
| Componente reutilizable `Buscador`, con propiedad, método y señal propios | `buscador.py`, `README-buscador.md` |
| Pruebas del componente con pytest-qt | `test_buscador.py` |
| Tamaño y posición de la ventana y la última búsqueda, guardados con `QSettings` | `main.py` |
| Empaquetado del componente como biblioteca instalable | `pyproject.toml` |

## Abrirlo en VS Code

Todas las órdenes van en **PowerShell**.

1. Copia la carpeta `bugtracker` a `C:\dam2627\di\`. Una ruta corta, fuera de OneDrive, evita errores al instalar.
2. Entra en ella y crea el entorno virtual con sus paquetes:

    ```
    cd C:\dam2627\di\bugtracker
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

6. Pasa las pruebas; al final tiene que decir **5 passed**:

    ```
    .venv\Scripts\python -m pytest -v
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

Si Windows bloquea `pyside6-designer.exe` o `pyside6-uic.exe` con «Una directiva de Control de aplicaciones bloqueó este archivo» (por ejemplo, con *Smart App Control* activado), es porque son accesos directos que crea `pip` al instalar PySide6 y no están firmados. Los programas reales, firmados por The Qt Company, están en `.venv\Lib\site-packages\PySide6`, y se pueden abrir directamente (el `&` hace falta porque la ruta va entre comillas):

```
& ".venv\Lib\site-packages\PySide6\designer.exe" bugtracker.ui
& ".venv\Lib\site-packages\PySide6\uic.exe" -g python bugtracker.ui -o ui_bugtracker.py
```
