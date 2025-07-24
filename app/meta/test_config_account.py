from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad

from consummer import api


consummer = api.Api()



print(f"Listando campañas para la cuenta: {consummer.get_ad_account().get_id()}")
campaigns = consummer.get_campaigns([Campaign.Field.name, Campaign.Field.status])
for campaign in campaigns:
    print(f"  Campaña ID: {campaign['id']}, Nombre: {campaign['name']}, Estado: {campaign['status']}")


print(f"\nListando conjuntos de anuncios para la cuenta: {consummer.get_ad_account().get_id()}")
ad_sets = consummer.get_ad_sets(fields=[AdSet.Field.name, AdSet.Field.status])
for ad_set in ad_sets:
    print(f"  Conjunto de Anuncios ID: {ad_set['id']}, Nombre: {ad_set['name']}, Estado: {ad_set['status']}")


print(f"\nListando anuncios para la cuenta: {consummer.get_ad_account().get_id()}")
ads = consummer.get_ads(fields=[Ad.Field.name, Ad.Field.status])
for ad in ads:
    print(f"  Anuncio ID: {ad['id']}, Nombre: {ad['name']}, Estado: {ad['status']}")