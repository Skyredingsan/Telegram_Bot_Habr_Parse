from os import environ
from typing import Final

class TgKey:
    TOKEN: Final = environ.get('TOKEN', 'define me!')

class Pars_api:
    api_id: Final = environ.get('api_id', 'define me!')
    api_hash: Final = environ.get('api_hash', 'define me!')
    id_channel: Final = environ.get('id_channel', 'define me!')

class Database:
    PGUSER = environ.get('pguser', 'define me!')
    PGPASSWORD = environ.get('pgpassord', 'define me!')
    DATABASE = environ.get('DATABASE', 'define me!')
    POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@'