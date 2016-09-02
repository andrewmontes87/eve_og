import os

URL_PREFIX = 'api'
X_DOMAINS = '*'
HATEOAS = False
PAGINATION = False

MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/og_co')

DOMAIN = { 
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
# {
#     "_id": {
#         "$oid": "57c8fc48e0831eea5bcb8e0e"
#     },
#     "bio_img": "full/811ee4352837f20673bd0dd3c937fe603a7d1769.jpg",
#     "name": "Royal Dutch Shell",
#     "revenue": 265,
#     "country": "United Kingdom",
#     "image_urls": [
#         "https://upload.wikimedia.org/wikipedia/en/thumb/e/e8/Shell_logo.svg/120px-Shell_logo.svg.png"
#     ],
#     "isin": "GB00B03MLX29",
#     "link": "http://en.wikipedia.org/wiki/Royal_Dutch_Shell",
#     "coordinate_location": "51.5072222222, -0.1275",
#     "inception": "2005",
#     "instance_of": "business enterprise"
# }