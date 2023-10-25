"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)

    #
    # Inserte su código aquí
    #
    #Reemplazar todas las letras a low_case

    df.dropna(inplace=True)
    
    #df.fecha_de_beneficio = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True)
    def unificar_fecha(fecha):
        try:
            return pd.to_datetime(fecha,  dayfirst=True).strftime('%d/%m/%Y')
        except:
            return fecha
    
    
    # Aplicar la función a la columna 'fecha'
    #df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(unificar_fecha)
    df.fecha_de_beneficio = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True)
    
    
    df = df.apply(lambda x: x.astype(str).str.replace("_","-"))
    df = df.apply(lambda x: x.astype(str).str.replace("-"," "))
    df = df.apply(lambda x: x.astype(str).str.replace("$",""))
    df = df.apply(lambda x: x.astype(str).str.replace(",",""))
    df = df.apply(lambda x: x.str.lower())
    
    df.monto_del_credito = df.monto_del_credito.astype(float)
      
    df.drop_duplicates(inplace=True)
    return df
