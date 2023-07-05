import os
import sys
from solution.utils.common_logger import CommonLogger
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#common 
SERVICE_NAME = os.environ.get('SERVICE_NAME', '')
PROFILE_NAME = os.environ.get('PROFILE_NAME', '')
DB_TYPE = os.environ.get('DB_TYPE', '')
MARIADB_USER = os.environ.get('MARIADB_USER', "")
MARIADB_PASSWORD = os.environ.get('MARIADB_PASSWORD', "")
MARIADB_HOST = os.environ.get('MARIADB_HOST', "")
DB_NAME = os.environ.get('DB_NAME', "")
MARIADB_PORT = os.environ.get('MARIADB_PORT', 3306)
DB_SSL_ENABLED = os.environ.get('DB_SSL_ENABLED', 'true')
DB_SSL_PATH_CERT = os.environ.get('DB_SSL_PATH_CERT', 'BaltimoreCyberTrustRoot.crt.pem')
ssl_args = {"ssl_ca": DB_SSL_PATH_CERT}
OTEL_TRACES_ENDPOINT = os.environ.get('OTEL_TRACES_ENDPOINT', "")
TOKEN_GENERATOR = os.environ.get('TOKEN_GENERATOR', "")
SERVICE_ON_CLOUD = os.environ.get('SERVICE_ON_CLOUD', 'false')
DATABASE_CONNECTION_URI = f'mysql+pymysql://{MARIADB_USER}:{MARIADB_PASSWORD}@{MARIADB_HOST}:{MARIADB_PORT}/{DB_NAME}'


def get_db_url() -> str:
    return DATABASE_CONNECTION_URI

def get_connect_args():
    args = {}
    if DB_SSL_ENABLED in ["true", True, 1]:
        args['ssl_ca'] = DB_SSL_PATH_CERT
    return args
