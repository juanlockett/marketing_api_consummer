from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
# from facebook_business.adobjects.campaign import Campaign
# from facebook_business.adobjects.adset import AdSet
# from facebook_business.adobjects.ad import Ad
# import configparser
# import os

from config import meta as conf_meta

class Api:
    def __init__(self):
        # 1. Inicializa la API de Facebook
        # Es mejor inicializarla una vez al inicio, quizás incluso fuera de la clase
        # si es una configuración global única, o aquí si cada instancia de Api
        # necesita su propia inicialización (menos común para APIs como esta).
        # Lo mantendremos aquí por ahora para que esté encapsulado.
        FacebookAdsApi.init(
            conf_meta.MY_APP_ID,
            conf_meta.MY_APP_SECRET,
            conf_meta.MY_SYSTEM_USER_ACCESS_TOKEN
        )
        self.fc_api = FacebookAdsApi.get_default_api() # Obtiene la instancia de API inicializada

        # 2. Inicializa la cuenta publicitaria predeterminada.
        # Directamente asigna una instancia de AdAccount al atributo 'ad_account'.
        # No usamos guion bajo '_' porque este atributo es parte de la interfaz pública
        # de tu clase Api y no requiere lógica extra de getter/setter por ahora.
        self.ad_account = AdAccount(conf_meta.MY_AD_ACCOUNT_ID)


    def get_campaigns(self, fields=None):
        """
        Obtiene las campañas de la cuenta publicitaria.
        :param fields: Lista de campos a recuperar.
        :return: Lista de campañas.
        """
        return self.ad_account.get_campaigns(fields=fields)

    def get_ad_sets(self, fields=None):
        """
        Obtiene los conjuntos de anuncios de la cuenta publicitaria.
        :param fields: Lista de campos a recuperar.
        :return: Lista de conjuntos de anuncios.
        """
        return self.ad_account.get_ad_sets(fields=fields)


    def get_ads(self, fields=None):
        """
        Obtiene los anuncios de la cuenta publicitaria.
        :param fields: Lista de campos a recuperar.
        :return: Lista de anuncios.
        """
        return self.ad_account.get_ads(fields=fields)


    def get_insights(self, fields=None, params=None):
        """
        Obtiene los insights de la cuenta publicitaria.
        :param fields: Lista de campos a recuperar.
        :param params: Parámetros adicionales para la consulta.
        :return: Lista de insights.
        """
        return self.ad_account.get_insights(fields=fields, params=params)

    




# --- Ejemplo de uso ---
if __name__ == "__main__":
    print("Iniciando aplicación...")

    # Instanciar tu API
    # La API se inicializa internamente y establece la ad_account por defecto
    api_consumer = Api()
    print(f"API inicializada con cuenta por defecto: {api_consumer.get_ad_account().get_id()}")

    # Supongamos que quieres cambiar a otra cuenta publicitaria
    nueva_cuenta_id = conf_meta.MY_AD_ACCOUNT_ID
    api_consumer.set_ad_account(nueva_cuenta_id)
    print(f"API ahora usando la cuenta: {api_consumer.get_ad_account().get_id()}")

    # Ahora puedes usar api_consumer.ad_account para hacer tus llamadas a la API de Facebook
    # Por ejemplo:
    # insights = api_consumer.ad_account.get_insights(fields=[...], params=[...])
    # print(insights)