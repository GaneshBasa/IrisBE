from json import loads

from app.helpers import get_env_var

if ORIGINS := get_env_var( 'ORIGINS' ):
  ORIGINS = loads( ORIGINS )
else:
  ORIGINS = [ 'http://localhost:3000' ]
