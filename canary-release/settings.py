RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
SERVER_NAME = None
MONGO_HOST = 'mongo'
MONGO_PORT = 27017
DOMAIN = {
    'specie': {
        'schema': {
            'name': {
                'type': 'string',
                'unique': True,
                'required': True,
            },
            'clade_id': {
                'type': 'integer',
                'required': True,
            },
            'habitat': {
                'type': 'string',
                'required': True,
            },
	    'population': {
		 'type': 'integer',
		 'required': True,
             },

        }
    }
}
