# Proyecto_ETL
# ETL de Hoteles en Madrid

## Descripción

Este proyecto de ETL (Extract, Transform, Load) tiene como objetivo recopilar, limpiar y almacenar datos sobre hoteles en Madrid. Para manejar los datos faltantes estructuralmente, se utilizan APIs y web scraping con las bibliotecas Beautiful Soup y Selenium.

## Tecnologías Utilizadas

- **Python**
- **Pandas**
- **Beautiful Soup**
- **Selenium**
- **APIs externas**
- \*\*SQL \*\*

## Pipeline de ETL

1. **Extracción**:
   - Obtención de datos desde APIs de hoteles.
   - Web scraping con Beautiful Soup y Selenium para completar datos faltantes.
2. **Transformación**:
   - Limpieza y normalización de datos.
   - Manejo de valores nulos mediante APIs y scraping.
   - Conversión de formatos de datos.
3. **Carga**:
   - Almacenamiento en bases de datos SQL.

## Instalación

Para ejecutar este proyecto, instala las dependencias necesarias:

```bash
pip install pandas beautifulsoup4 selenium requests
```

## Uso

Ejecuta el script principal para iniciar el proceso ETL:

```bash
python src.py
```

## Autor

- Carlos Javier Ramírez Kunja


