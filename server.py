from eve import Eve
import os

print os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/og_co')

my_settings = {
    'URL_PREFIX' : 'api',
    'X_DOMAINS' : '*',
    'HATEOAS' : False,
    'PAGINATION' : False,
    'MONGO_URI' : os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/og_co'),
    'DOMAIN' : { 
        'og_co':{
            'item_title':'og_co_record',
            'schema':{
                'link':{'type':'string'},
                'country':{'type':'string'},
                'headquarters_location':{'type':'string'},
                'name':{'type':'string'},
                'coordinate_location':{'type':'string'},
                'bio_img':{'type':'string'},
                'image_urls':{'type':'array'},
                'revenue':{'type':'float'},            
                'inception':{'type':'string'},            
                'instance_of':{'type':'string'},            
                'isin':{'type':'string'},            
            },
            'url':'og_co'
        }
    }
}

app = Eve(settings=my_settings)

if __name__=='__main__':
    app.run(debug=True)