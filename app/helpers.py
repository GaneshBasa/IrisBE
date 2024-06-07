from os import environ
from json import loads

def get_env_var( var_name: str ):
  data  = loads( environ.get( var_name ) )
  # print( 'ENV VAR', '|', var_name, '|', type( data ), '|', data  )
  return data
