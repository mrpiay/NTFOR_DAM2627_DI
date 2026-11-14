# UD2 y UD3 · Ampliación: contar con SQL y el componente en Qt Designer

Dos conceptos nuevos de esta semana que amplían lo visto: contar filas por grupos con SQL (UD2) y usar un componente propio desde Qt Designer (UD3). Continúan los [apuntes de la UD3 de la semana del 9 al 13](../../2026_11_09-13/apuntes/UD3-componentes-reutilizables.md). Las preguntas para comprobar que lo entiendes están en el [cuestionario](../cuestionario.md) de la semana.

---

## 1. Contar por grupos con SQL

*Para la práctica: paso 12 del proyecto.*

**En una frase:** `GROUP BY` junta las filas que tienen el mismo valor en una columna, y `COUNT(*)` cuenta cuántas hay en cada grupo.

**Lo que tienes que saber**

```sql
SELECT estado, COUNT(*) AS total
FROM incidencias
GROUP BY estado
ORDER BY estado
```

| estado | total |
|---|---|
| En proceso | 1 |
| Pendiente | 3 |
| Resuelta | 1 |

- `GROUP BY estado` hace un grupo por cada estado distinto; `COUNT(*)` cuenta las filas de cada grupo.
- `AS total` da nombre a la columna calculada: desde Python se lee como `fila["total"]`.
- Otras funciones de grupo: `SUM` (suma), `AVG` (media), `MIN` y `MAX`.
- Contar es trabajo de la **base de datos**, no de la interfaz: la consulta va en `bd.py`, y `main.py` solo muestra el resultado (la regla de separación).

---

## 2. Usar un componente propio desde Qt Designer

*Para la práctica: paso 13 del proyecto.*

**En una frase:** Qt Designer solo conoce los controles de Qt; para colocar uno propio se pone un control de Qt en su lugar y se **promociona** (*Promote to*) a la clase propia.

**Lo que tienes que saber**

- Se coloca un `QWidget` donde irá el componente, se le da nombre (`objectName`) y, con clic derecho → **Promote to…**, se indica la **clase** (`Buscador`) y el **archivo de cabecera** (`buscador.h`). En Python, la cabecera solo sirve para el nombre del módulo: el código generado hace `from buscador import Buscador`.
- Qt Designer no sabe dibujar el componente: en el diseño se ve un recuadro vacío, y el componente de verdad aparece al ejecutar.
- El código generado lo crea así: `self.buscador = Buscador(self.centralwidget)`, con el **padre como primer parámetro**. Por eso un componente pensado para usarse desde Qt Designer tiene `parent` como primer parámetro de `__init__`, como todos los controles de Qt.
- Cambiar la forma de crear un componente (el orden de sus parámetros) puede romper a quien ya lo usa: después de un cambio así, se repiten sus pruebas (**prueba de regresión**).

**Compara**

| | Añadido por código | Colocado en Qt Designer (promocionado) |
|---|---|---|
| Dónde se decide su posición | En `main.py` (`insertWidget`) | En el diseño, `bugtracker.ui` |
| Se ve en Qt Designer | No | Sí, como recuadro vacío con su nombre |
| Quién lo crea | El código de la ventana | `setupUi`, el código generado |
| Qué exige al componente | Nada especial | Que acepte el padre como primer parámetro |

> **Para saber más.** En C++, un componente se puede convertir en un *plugin* de Qt Designer para que aparezca en su lista de controles y se dibuje en el diseño. Con Python, la forma habitual es la promoción.

---

## Dónde consultar

- **Qt Designer y los componentes propios**, documentación oficial de Qt, en inglés: [Using Custom Widgets with Qt Designer](https://doc.qt.io/qt-6/designer-using-custom-widgets.html), apartado «Promoting Widgets».
- **SQL en SQLite:** [SELECT](https://www.sqlite.org/lang_select.html) y [funciones de grupo](https://www.sqlite.org/lang_aggfunc.html), en inglés.
