# Importamos librería
import pandas as pd

# Importamos las bases de datos 
# ad_data_2 contiene datos sobre los gastos de publicidad y site_data_2 contiene los datos sobre registros
ad_data= pd.read_csv('/ad_data_2.csv')
site_data = pd.read_csv('/site_data_2.csv')

# Juntamos las dos bases de datos en la variable funnel_daily
funnel_daily = pd.merge(ad_data, site_data, on='date')

# Calculamos el CTR y CR y los agregamos a unas nuevas columnas
funnel_daily['ctr, %'] = (funnel_daily['clicks'] / funnel_daily['impressions']) * 100
funnel_daily['cr, %'] = (funnel_daily['registrations'] / funnel_daily['clicks']) * 100

# Convertimos los datos de 'date' en formato 'datetime'
funnel_daily['date'] = pd.to_datetime(funnel_daily['date'])