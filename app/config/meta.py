from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad

from configparser import ConfigParser

# Obtiene el directorio base del proyecto
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Instancia configparser y lee el archivo de configuración
config = configparser.ConfigParser()
config_path = os.path.join(PROJECT_PATH, 'config', 'config.ini')
config.read(config_path)

# Carga las variables del entorno [DEVELOPMENT]
env = config['DEVELOPMENT']

# --- Carga de constantes ---
MY_APP_ID = env.get('MY_APP_ID')
MY_APP_SECRET = env.get('MY_APP_SECRET')
MY_SYSTEM_USER_ACCESS_TOKEN = env.get('MY_SYSTEM_USER_ACCESS_TOKEN')
MY_AD_ACCOUNT_ID = env.get('MY_AD_ACCOUNT_ID') # Ejemplo: 'act_1234567890'



