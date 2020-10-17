import streamlit as st
import latam
from datetime import datetime as dt

st.markdown("# Como usar `latam`")

""" 
Comenzamos importando `latam`

```python
import latam
```

Por el momento la versión `0.1.2` incluye solo a México
```python
latam.paises.MEX
```
"""
st.write(latam.paises.MEX)

""" 
`latam` viene con 3 tipos de entidades: `Ciudad`, `Subdivision` y `Pais`. México es un `Pais`.

Viene con la siguiente información:
"""
mexico = latam.paises.MEX
st.write(mexico.__dict__)

"""
Como puedes ver, México tiene un diccionario de `.subdivisiones` con cada uno de sus estados. 
Subdivisión se refiere al primer nivel de gobernación después del nivel nacional. 
En algunos paises se le conoce como "estado", en otros como "provincia" o "distrito."

Cada `Subdivision` tiene la siguiente información:
"""
n_estado = st.selectbox(label = "Estado", options = [mexico.subdivisiones.keys()])
estado = mexico.subdivisiones["Baja California"]
st.write(estado.__dict__)

""" 
Cada `Subdivision` incluye por lo menos una `Ciudad`, su capital. 
```python
latam.paises.MEX.subdivisiones['Baja California'].capital
```
"""
st.write(estado.capital)

"""
Cada `Ciudad` incluye la siguiente información:
"""
st.write(estado.capital.__dict__)

"""
***
Entre otras cosas `latam` toma ventaja de ciertos estandares. 
* Utilizamos `pytz` para incluir los husos horarios de cada `Ciudad`, `Subdivision` y `Pais`.
* Utilizamos objetos `datetime.date` para las fechas de fundación 
* Utilizamos la norma ISO-3611-1 y 2 para los códigos de identificación de cada `Pais` y `Subdivision`.
* Utilizamos el formato EPSG:4326 o WSG84 para la latitud y longitud de cada `Ciudad`.
* Utilizamos el Alfabeto Fonético Internacional (AFI) para el atributo `.nombre_pronunciacion_local`.

Veamos su utilidad.
```python
from datetime import datetime as dt
for subdivisionn in mexico.subdivisiones.values():
    print(f"En la capital de {subdivision.nombre_comun} ({subdivision.capital.nombre_comun}) son las {dt.now(tz = subdivision.capital.huso_horario).strftime('%HH:%MM')}")
"""

for subdivision in mexico.subdivisiones.values():
    f"En la capital de {subdivision.nombre_comun} ({subdivision.capital.nombre_comun}) son las {dt.now(tz = subdivision.capital.huso_horario).strftime('%HH:%MM')}"

""" 
***
Cada `Pais` también tiene los atributos `.df` y `.subdivisiones_df` los cuales son DataFrames de Pandas con la información del país y sus subdivisiones, respectivamente.

```python
latam.paises.MEX.df
```
"""
mexico.df

"""
```python
latam.paises.MEX.subdivisiones_df
```
"""
mexico.subdivisiones_df

"""
Esto es para facilitar el análisis de los datos ya que Pandas es una herramienta común en el mundo del análisis de datos en python.

Esto funciona muy bien también con Streamlit. Si cambiamos el nombre de nuestras columndas de `capital_lat` y `capital_long` a `lat` y `long` podemos crear un mapa con una sola línea de código.
```python
import streamlit as st

estados_mx = mexico.subdivisiones_df.copy()
estados_mx.rename(columns = {"capital_lat": "lat", "capital_long": "lon"}, inplace=True)
st.map(estados_mex)
```
"""
estados_mx = mexico.subdivisiones_df.copy()
estados_mx.rename(columns = {"capital_lat": "lat", "capital_long": "lon"}, inplace=True)
st.map(estados_mx)
