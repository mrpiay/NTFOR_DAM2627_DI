# Buscador

Componente de PySide6 para buscar: una etiqueta, una caja de texto y un botón «Limpiar».

## Uso

```python
from buscador import Buscador

buscador = Buscador()
buscador.busquedaCambiada.connect(lambda texto: print("Buscar:", texto))
layout.addWidget(buscador)
```

## Interfaz

| Tipo | Nombre | Qué hace |
|---|---|---|
| Propiedad | `texto` (`str`) | El texto que se busca; se puede leer y cambiar |
| Método | `limpiar()` | Borra el texto y devuelve el foco a la caja |
| Señal | `busquedaCambiada(str)` | Se emite cada vez que cambia el texto |

## Instalar en otro proyecto

Con `pyproject.toml` en la misma carpeta y `build` instalado (`pip install build`, una vez): `python -m build` crea `dist/buscador_dam-0.1.0-py3-none-any.whl`, que se instala con `pip install dist/buscador_dam-0.1.0-py3-none-any.whl`.
