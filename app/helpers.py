from os import environ
from json import loads

def get_env_var( var_name: str ):
  if var_name in environ:
    data  = loads( environ.get( var_name ) )
  else:
    data = None
  
  # print( 'ENV VAR', '|', var_name, '|', type( data ), '|', data  )
  return data
