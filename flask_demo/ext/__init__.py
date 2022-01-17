from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_caching import Cache
from setting import DefaultConfig

db = SQLAlchemy()
bootstrap = Bootstrap()
cache = Cache(config={'CACHE_TYPE': DefaultConfig.CACHE_TYPE,
                      'CACHE_REDIS_HOST': DefaultConfig.CACHE_REDIS_HOST,
                      'CACHE_REDIS_PORT': DefaultConfig.CACHE_REDIS_PORT,
                      'CACHE_REDIS_DB': DefaultConfig.CACHE_REDIS_DB})

