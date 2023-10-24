"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    #Eeemplazar todas las letras a low_case
    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['barrio'] = df['barrio'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.lower()

    ## Reemplazar todas las raya al piso por espacio

    df['nombre_columna'] = df['nombre_columna'].str.replace('_', ' ')

    return df
