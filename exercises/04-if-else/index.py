import os

DEVELOPMENT= 'dev'
PRODUCTION= 'prod'
STAGING= 'stage'
LOCAL= 'local'

current_env = os.environ.get("TEST_ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print('Development env')
elif current_env == PRODUCTION:
    print('Prod env')
elif current_env == STAGING:
    print('Stage env')
elif current_env == LOCAL:
    print('Local env')