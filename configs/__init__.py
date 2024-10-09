import os
from dotenv import load_dotenv

load_dotenv()

configs_env = {}
database_url = os.environ.get('DATABASE_URL')

configs_env['database_url'] = database_url