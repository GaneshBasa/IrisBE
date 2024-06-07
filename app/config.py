from app.helpers import get_env_var

ORIGINS = get_env_var( 'ORIGINS' ) or [ 'http://localhost:3000' ]
