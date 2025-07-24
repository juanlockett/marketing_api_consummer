from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.exceptions import FacebookRequestError





################

from consummer import api

print(f"\nObteniendo insights por edad y género para la cuenta: {consummer.get_ad_account().get_id()}")

fields = [
    AdsInsights.Field.spend,
    AdsInsights.Field.impressions,
    AdsInsights.Field.clicks,
    AdsInsights.Field.actions,
    AdsInsights.Field.age,
    AdsInsights.Field.gender,
]

params = {
    'time_range': {'since': '2024-01-01', 'until': '2024-01-31'},
    'level': 'adset', # Puedes usar 'campaign', 'ad', etc.
    'breakdowns': ['age', 'gender'], # Desglose por edad y género
}

try:
    insights = ad_account.get_insights(fields=fields, params=params)
    for insight in insights:
        print(f"  Conjunto de Anuncios ID: {insight.get('adset_id')}")
        print(f"    Edad: {insight.get('age')}, Género: {insight.get('gender')}")
        print(f"    Gasto: {insight.get('spend')}")
        print(f"    Impresiones: {insight.get('impressions')}")
        print(f"    Clics: {insight.get('clicks')}")
        actions = insight.get('actions', [])
        for action in actions:
            print(f"    Acción '{action.get('action_type')}': {action.get('value')}")
        print("-" * 30)
except FacebookRequestError as e:
    print(f"Error al obtener insights con desglose: {e}")

###################
