# TodoDI · paso 6: la inyección SQL

Este paso es un **experimento**: se estropea TodoDI a propósito, para ver qué pasa cuando el texto que escribe quien usa la aplicación se pega dentro de una consulta SQL, y después se vuelve a dejar bien.

Desde el paso 3, `insertar_tarea` pasa el texto en un `?`:

```python
ejecutar_sql("INSERT INTO tareas (texto) VALUES (?)", (texto,))
```

Con `?`, `sqlite3` manda el texto **aparte**, como un valor, y nunca lo trata como SQL. Si en lugar de eso el texto se pega dentro de la consulta, quien escribe la tarea puede escribir SQL, y la base de datos lo ejecuta. Eso es la **inyección SQL**, uno de los fallos de seguridad más conocidos y más graves.

## 1 · Antes de empezar: una copia de `tareas.db`

El experimento borra todas las tareas. Haz antes una copia de la base de datos, en CMD, desde la carpeta del proyecto:

```bat
copy tareas.db tareas-copia.db
```

## 2 · La versión mal hecha

En **`bd.py`**, cambia `insertar_tarea` por esta versión, con una función nueva, `ejecutar_script`, encima:

```python
# Paso 5 (bien)
def insertar_tarea(texto):
    # Guarda una tarea nueva; el texto va en el ?
    ejecutar_sql("INSERT INTO tareas (texto) VALUES (?)", (texto,))
```

```python
# Paso 6 (MAL, solo para el experimento)
def ejecutar_script(sql):
    # MAL: executescript ejecuta todas las sentencias SQL que haya en el texto, una detrás de otra
    conexion = sqlite3.connect(RUTA)
    conexion.executescript(sql)
    conexion.close()
def insertar_tarea(texto):
    # MAL: el texto de la tarea se pega dentro del SQL, entre comillas simples
    ejecutar_script("INSERT INTO tareas (texto) VALUES ('" + texto + "')")
```

Hay **dos** errores, y hacen falta los dos para que el ataque funcione:

| Error | Qué hace |
|---|---|
| El texto se **pega** dentro del SQL con `+` | Lo que escribe quien usa la aplicación pasa a formar parte de la consulta |
| Se ejecuta con **`executescript`** | Ejecuta todas las sentencias que haya en el texto, separadas por `;`. `execute`, en cambio, solo admite una |

## 3 · Probar

Ejecuta la aplicación (`python main.py`), añade un par de tareas normales y prueba estos dos textos, uno cada vez.

### Prueba 1 · Un apóstrofo: `Revisar l'agenda`

**Observa:** la tarea no se añade, el texto se queda en el campo y en la terminal aparece el error `sqlite3.OperationalError: near "agenda": syntax error`. La aplicación sigue abierta.

**Por qué:** al pegar el texto, la consulta queda así:

```sql
INSERT INTO tareas (texto) VALUES ('Revisar l'agenda')
```

En SQL, los textos van entre comillas simples. El apóstrofo de `l'agenda` **cierra el texto** antes de tiempo: para SQL, el texto es `'Revisar l'`, y después viene `agenda')`, que no significa nada. Error de sintaxis.

### Prueba 2 · Un texto que borra todas las tareas: `x'); DELETE FROM tareas; --`

**Observa:** la lista se queda **vacía**. Se han borrado todos los **registros** de la tabla `tareas`: al cerrar y volver a abrir, siguen sin estar. La base de datos, el archivo `tareas.db`, y la tabla siguen existiendo, vacías: se pueden añadir tareas nuevas como siempre.

**Por qué:** al pegar el texto, la consulta queda así:

```sql
INSERT INTO tareas (texto) VALUES ('x'); DELETE FROM tareas; --')
```

Pieza a pieza:

| Trozo | Qué es para SQL |
|---|---|
| `INSERT INTO tareas (texto) VALUES ('x');` | Una sentencia completa: guarda la tarea `x`. El `'` y el `)` del texto cierran el valor y el paréntesis, y el `;` termina la sentencia |
| `DELETE FROM tareas;` | **Una sentencia nueva**, escrita por quien usa la aplicación: borra todos los registros de la tabla. Sin un `WHERE`, el `DELETE` afecta a todas las filas |
| `--')` | `--` empieza un **comentario**: todo lo que sigue se ignora. Así, el `')` que añadía el programa no da error |

`executescript` ejecuta las dos sentencias, una detrás de otra: guarda `x` y, a continuación, borra todos los registros, también el de `x`. La tabla queda vacía, pero sigue ahí. Con `DROP TABLE tareas` en lugar del `DELETE`, el ataque borraría la tabla entera, y la aplicación fallaría al intentar leerla.

## 4 · Volver a la versión buena

1. En **`bd.py`**, borra `ejecutar_script` y deja `insertar_tarea` como estaba:

   ```python
   def insertar_tarea(texto):
       # Guarda una tarea nueva; el texto va en el ?
       ejecutar_sql("INSERT INTO tareas (texto) VALUES (?)", (texto,))
   ```

2. Recupera las tareas desde la copia, en CMD, con la aplicación cerrada:

   ```bat
   copy /y tareas-copia.db tareas.db
   ```

   `/y` sobrescribe `tareas.db` sin preguntar.

3. Vuelve a probar los dos textos.

**Observa:** los dos se añaden como **tareas normales**, con su texto tal cual, apóstrofo y punto y coma incluidos, y las demás tareas siguen ahí.

**Por qué:** con `?`, el texto nunca forma parte del SQL. La consulta es siempre `INSERT INTO tareas (texto) VALUES (?)`, y `sqlite3` le pasa el texto aparte, como un valor. Da igual lo que contenga: para la base de datos es solo texto.

## 5 · Resumen

Lo que pasa con cada texto, según cómo se haga la consulta:

| Cómo se hace la consulta | `Revisar l'agenda` | `x'); DELETE FROM tareas; --` |
|---|---|---|
| Texto pegado, con `executescript` (la versión mal hecha) | Error de sintaxis | **Borra todas las tareas** |
| Texto pegado, con `execute` | Error de sintaxis | Error: `You can only execute one statement at a time` |
| Con `?` (la versión de TodoDI) | Se guarda tal cual | Se guarda tal cual |

La segunda fila muestra que `execute` frena este ataque concreto, porque solo admite una sentencia. Pero el apóstrofo sigue rompiendo la consulta, y hay inyecciones que caben en una sola sentencia. La única forma segura es la de la tercera fila: **los datos siempre en `?`, nunca pegados en el SQL**.

## Preguntas y respuestas

**1. ¿Qué es la inyección SQL?**

Un ataque que aprovecha que un programa pega en una consulta SQL el texto que escribe quien lo usa. Escribiendo SQL en ese texto, se puede cambiar lo que hace la consulta: leer datos ajenos, entrar sin contraseña en un formulario de acceso o, como aquí, borrar datos.

**2. ¿Por qué con `?` no pasa?**

Porque la consulta y los datos viajan por separado: el SQL es siempre el mismo, con un hueco, y el texto va aparte, como un valor. La base de datos nunca lo interpreta como SQL, contenga lo que contenga.

**3. ¿Qué hacen el `;` y el `--` en el texto del ataque?**

El `;` termina la sentencia del programa, para empezar otra nueva, la del ataque. El `--` convierte en comentario lo que el programa añadía detrás (`')`), para que no dé error de sintaxis.

**4. Si `execute` solo admite una sentencia, ¿por qué no basta con usarlo?**

Porque solo frena los ataques que necesitan una segunda sentencia. El texto pegado sigue rompiendo la consulta con un apóstrofo, y hay ataques que caben en una sola sentencia, por ejemplo cambiando la condición de un `WHERE` para que se cumpla siempre.

**5. ¿Cuándo es seguro usar `executescript`?**

Con un SQL escrito por el programa y fijo, por ejemplo para crear todas las tablas de una vez. Nunca con texto que venga de quien usa la aplicación.

**6. ¿Para qué sirve la copia de `tareas.db`?**

Para recuperar las tareas después del experimento. Es la misma idea que las copias de seguridad de verdad: un ataque, o un error, puede borrar datos, y sin copia no hay forma de recuperarlos.
