def to_date(columns, dataframe):
    """
    Convierte las columnas especificadas de un DataFrame a formato de fecha.

    Esta función toma una lista de nombres de columnas y las convierte a tipo datetime 
    utilizando la función `pd.to_datetime`. Si no puede convertir un valor de alguna 
    de las columnas, lo reemplaza por NaT (Not a Time), gracias al parámetro 
    `errors="coerce"`.

    Parámetros:
    columns (list): Una lista de nombres de las columnas del DataFrame que se desean 
                    convertir a formato de fecha.
    dataframe (pandas.DataFrame): El DataFrame que contiene las columnas a convertir.

    Retorna:
    pandas.DataFrame: El DataFrame original, pero con las columnas especificadas convertidas
                       a tipo datetime.

    Ejemplo:
    >>> df = pd.DataFrame({
    >>>     'fecha': ['2021-01-01', '2021-02-01', '2021-03-01'],
    >>>     'valor': [10, 20, 30]
    >>> })
    >>> df = to_date(['fecha'], df)
    >>> print(df['fecha'])
    0   2021-01-01
    1   2021-02-01
    2   2021-03-01
    Name: fecha, dtype: datetime64[ns]
    """
    for col in columns:
        dataframe[col] = pd.to_datetime(dataframe[col], errors="coerce")
    return dataframe


def scrap_hoteles(url):
    """
    Función para extraer información sobre hoteles desde una URL utilizando web scraping con BeautifulSoup.

    Esta función realiza una solicitud HTTP a la URL proporcionada, obtiene el contenido HTML de la página, y extrae
    los nombres de los hoteles y sus estrellas desde los elementos `<h2>` que contienen esta información.
    La función asume que el texto en cada `<h2>` está separado por un salto de línea (`\n`), donde la primera parte es 
    el nombre del hotel y la segunda parte es la cantidad de estrellas del hotel.

    Parámetros:
    ----------
    url : str
        La URL de la página web desde la cual se desea hacer scraping.

    Retorna:
    --------
    dict_hoteles : dict
        Un diccionario que contiene dos claves:
        - 'nombres_hotel': una lista con los nombres de los hoteles extraídos de la página.
        - 'estrellas_hotel': una lista con la cantidad de estrellas de cada hotel.
    
    Si la solicitud HTTP falla (código de estado diferente a 200), la función retorna un mensaje de error.

    Ejemplo:
    --------
    url = "https://ejemplo.com/hoteles"
    resultado = scrap_hoteles(url)
    
    print(resultado)
    # {'nombres_hotel': ['Mercure Madrid Centro', 'Hotel XYZ'], 'estrellas_hotel': ['4 Estrellas', '5 Estrellas']}
    """
    dict_hoteles = {
        "nombres_hotel": [],
        "estrellas_hotel": []
    }
    
    # Realizar solicitud HTTP
    res = requests.get(url)
    
    # Verificar que la solicitud fue exitosa (código 200)
    if res.status_code == 200:
        sopa_hoteles = BeautifulSoup(res.text, "html.parser")
        
        # Buscar todos los elementos <h2> que contienen la información de los hoteles
        headings = sopa_hoteles.find_all("h2")
        
        for head in headings:
            # Obtener el texto y eliminar espacios al principio y final
            text = head.get_text().strip()
            parts = text.split("\n")
            
            # Manejar el caso donde hay menos de dos partes
            if len(parts) >= 2:
                nombres_hotel = parts[0].strip()  # El nombre del hotel es la primera parte
                estrellas_hotel = parts[1].strip()  # La cantidad de estrellas es la segunda parte
            else:
                nombres_hotel = parts[0].strip()  # Si solo hay el nombre del hotel
                estrellas_hotel = "No rating available"  # Asignar valor por defecto para la estrella si falta
            
            # Añadir los datos al diccionario
            dict_hoteles["nombres_hotel"].append(nombres_hotel)
            dict_hoteles["estrellas_hotel"].append(estrellas_hotel)
    
    else:
        return f"No se ha podido encontrar la url, status code: {res.status_code}"
    
    return dict_hoteles
    