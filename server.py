from eve import Eve
from settings import URL_PREFIX, X_DOMAINS, HATEOAS, PAGINATION, MONGO_URI, DOMAIN 

SETTINGS = {
    'URL_PREFIX': URL_PREFIX,
    'X_DOMAINS': X_DOMAINS,
    'HATEOAS': HATEOAS,
    'PAGINATION': PAGINATION,
    'MONGO_URI': MONGO_URI,
    'DOMAIN': DOMAIN
}

app = Eve()

if __name__=='__main__':
    app.run(settings=SETTINGS, debug=True)