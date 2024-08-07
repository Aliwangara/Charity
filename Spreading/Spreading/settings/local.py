from.base import*





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}








# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'CLIENT': {
#             'host': 'mongodb+srv://aliwangara63:l1FWqVWW0qBVoIFx@cluster0.pbhumyz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', # Replace with your MongoDB server address
#             # 'port': 27017,               # Replace with your MongoDB port if different
#             'username': 'aliwangara63', # Replace with your MongoDB username (optional)
#             'password': 'l1FWqVWW0qBVoIFx', # Replace with your MongoDB password (optional)

#         },
#         'NAME': 'Charity',
#     }
# }


