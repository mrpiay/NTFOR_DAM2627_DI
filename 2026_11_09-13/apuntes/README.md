# Apuntes · semana del 9 al 13 de noviembre

Los apuntes de las unidades de esta semana.

| Archivo | Qué es |
|---|---|
| [`UD3-componentes-reutilizables.md`](UD3-componentes-reutilizables.md) | Lo básico de la UD3: componentes reutilizables, propiedades, métodos y señales propias, pruebas con pytest-qt, documentar y empaquetar |

Cada archivo tiene lo básico de una unidad. Las preguntas del [cuestionario](../cuestionario.md) se responden con ellos y con el proyecto, y las de la prueba escrita salen de lo mismo.

## Dónde consultar

- **PySide6 (Qt para Python):** la documentación oficial, en inglés: [señales y slots](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/signals_and_slots.html) (también cómo declarar una señal propia con `Signal`), [Property](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Property.html), [QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html) y [QSettings](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSettings.html). Busca el método con `Ctrl+F`.
- **Sin conexión, o si la web de Qt no responde:** la ayuda de cada clase está en el propio PySide6. Con el entorno virtual, por ejemplo: `.venv\Scripts\python -c "from PySide6.QtCore import QSettings; help(QSettings)"` (avanzas con `Espacio` y sales con `q`).
- **pytest:** la documentación oficial, en inglés: [primeros pasos](https://docs.pytest.org/en/stable/getting-started.html).
- **pytest-qt:** la documentación oficial, en inglés: [cómo se usa `qtbot`](https://pytest-qt.readthedocs.io/en/latest/tutorial.html) y [cómo esperar señales con `waitSignal`](https://pytest-qt.readthedocs.io/en/latest/signals.html).
- **Python:** la documentación oficial, en español: [docstrings](https://docs.python.org/es/3/tutorial/controlflow.html#documentation-strings) y [`help()`](https://docs.python.org/es/3/library/functions.html#help).
- **Empaquetar** (`pyproject.toml` y `python -m build`): la guía oficial de Python, en inglés: [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
