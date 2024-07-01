import os
from dotenv import load_dotenv

load_dotenv('.env')
print('Loading environment variables...')

# database configuration
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', '')
DB_HOST = os.getenv('DB_HOST', 'localhost')

# jwt configuration
JWT_SECRET = os.getenv('JWT_SECRET', '')
JWT_EXPIRES_IN = int(os.getenv('JWT_EXPIRES_IN', 1))

# RUC_API_TOKEN = os.getenv('RUC_API_TOKEN', '')
# TRANSPORTATION_RUC = os.getenv('TRANSPORTATION_RUC', '')
# API_SUNAT_URL = os.getenv('API_SUNAT_URL', '')
# API_SUNAT_TOKEN = os.getenv('API_SUNAT_TOKEN', '')