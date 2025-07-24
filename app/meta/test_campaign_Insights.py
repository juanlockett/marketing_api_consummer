from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.exceptions import FacebookRequestError



from consummer import api

print(f"\nObteniendo insights a nivel de campaña para la cuenta: {consummer.get_ad_account().get_id()}")

# Define los campos (métricas) que quieres obtener
fields_campaign = [
    AdsInsights.Field.campaign_name,
    AdsInsights.Field.spend,
    AdsInsights.Field.impressions,
    AdsInsights.Field.clicks,
    AdsInsights.Field.cpc,
    AdsInsights.Field.ctr,
    AdsInsights.Field.actions,
    AdsInsights.Field.date_start,
    AdsInsights.Field.date_stop,
]

# Define los parámetros (rango de fechas, etc.)
params = {
    'time_range': {'since': '2024-01-01', 'until': '2024-01-31'},
    'level': 'campaign', # Nivel de granularidad
    'time_increment': 1,
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