from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.exceptions import FacebookRequestError



from consummer import api

print(f"\nObteniendo insights para la cuenta publicitaria: {consummer.get_ad_account().get_id()}")

# Define los campos (métricas) que quieres obtener
fields = [
    AdsInsights.Field.account_name,
    AdsInsights.Field.spend,
    AdsInsights.Field.impressions,
    AdsInsights.Field.clicks,
    AdsInsights.Field.cpc,
    AdsInsights.Field.cpm,
    AdsInsights.Field.ctr,
    AdsInsights.Field.actions, # Para conversiones, leads, etc.
    AdsInsights.Field.action_values,
    AdsInsights.Field.date_start,
    AdsInsights.Field.date_stop,
]

# Define los parámetros (rango de fechas, etc.)
params = {
    'time_range': {'since': '2025-07-07', 'until': '2025-07-14'}, # Ejemplo de rango de fecha: Determinar si el parametro 'until' valida con < o <=
    'level': 'account', # Nivel de granularidad
    'time_increment': 1, # Datos diarios. Puedes omitirlo para datos agregados en el rango. Validar si es un agrupamiento
}

try:
    #insights = ad_account.get_insights(fields=fields, params=params)
    consummer = api.Api()
    insights = consummer.get_insights(fields=fields, params=params)
    print(f"Total de insights obtenidos: {len(insights)}")

    for insight in insights:
        print(f"  Fecha: {insight.get('date_start')} - {insight.get('date_stop')}")
        print(f"    Gasto: {insight.get('spend')}")
        print(f"    Impresiones: {insight.get('impressions')}")
        print(f"    Clics: {insight.get('clicks')}")
        print(f"    CPC: {insight.get('cpc')}")
        print(f"    CPM: {insight.get('cpm')}")
        print(f"    CTR: {insight.get('ctr')}")
        # Acceder a acciones específicas (ej. 'offsite_conversions')
        actions = insight.get('actions', [])
        for action in actions:
            print(f"    Acción '{action.get('action_type')}': {action.get('value')}")
        print("-" * 30)
except FacebookRequestError as e:
    print(f"Error al obtener insights de la cuenta: {e}")