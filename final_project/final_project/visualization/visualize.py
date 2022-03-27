import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def covid_time_series(df):
    """Esta funcion toma como parametrp
    un df con 3 columnas pais,date,valor 
    
    Retorna un plot con el comportamiento
    de estos paises
    """
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )      

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");


def comparacion_paises(countries_estudio,df,n,):
    """Contexto de latinoametica en relacion de otros paises

    Input    
    df : processed_covid_df es el df procesado de los paises con la informacion 
    countries : son los paises que se quieren resaltar
    n: cantidad de paises

    Explicacion
    Se hace un agrupapiendo en el cual se suman los datos de todas las 
    fechas y se guarda en al columna values

    Output
    Se returna una grafica de barras mostrando esta relacion, resaltando
    los paises de estudio
    """
    top_countries_df = (
        df.select_columns(["country_region", "value"])
        .groupby(["country_region"])
        .aggregate("sum")
        .sort_values("value", ascending=False)
        .reset_index()
        .head(n)
        .transform_column(
            column_name="country_region",
            function=lambda x: "red" if x in countries_estudio else "lightblue",
            dest_column_name="color"
        )
        )

    sns.barplot(
    data=top_countries_df,
    x="value",
    y="country_region",
    palette=top_countries_df.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");
