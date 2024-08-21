from json import loads

from app.helpers import get_env_var

if ORIGINS := get_env_var( 'ORIGINS' ):
  ORIGINS = loads( ORIGINS )
else:
  ORIGINS = [ '*' ]

if ALLOWED_HOSTS := get_env_var( 'ALLOWED_HOSTS' ):
  ALLOWED_HOSTS = loads( ALLOWED_HOSTS )
else:
  ALLOWED_HOSTS = [ '*' ]
