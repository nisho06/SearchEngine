from LoadBulkElasticSearch.preprocess import preprocess


def generator(dataFrame):
    for line in (dataFrame):
        yield {
            '_index': 'actors',
            '_type': '_doc',
            '_id': line.get('id', None),
            '_source': {
                'பெயர்': line.get('பெயர்', None),
                'அறிமுக_வருடம்': line.get("அறிமுக வருடம்", None),
                'அறிமுக_படம்': line.get("அறிமுக படம்", None),
                'பிறந்த_திகதி': line.get('பிறந்த திகதி', None),
                'பிறந்த_இடம்': line.get('பிறந்த இடம்', None),
                'அறிமுகம்': line.get('அறிமுகம்', None),
                'உள்ளடக்கம்': line.get('உள்ளடக்கம்', None)
            }
        }


try:
    import elasticsearch
    from elasticsearch import Elasticsearch

    import pandas as pd
    import json
    from ast import literal_eval
    from tqdm import tqdm
    import datetime
    import os
    import sys

    import numpy as np
    from elasticsearch import helpers

    print("Loaded.......")

except Exception as e:
    print("Some Modules are missing ()".format(e))

df = pd.read_csv('data.csv')

ENDPOINT = 'http://localhost:9200/'
es = Elasticsearch(timeout=600, hosts=ENDPOINT)

dataFrame = preprocess(df)

record = dataFrame.to_dict('records')
print(record)

mycustom = generator(record)

Settings = {
    'settings': {
        'number_of_shards': 1,
        'number_of_replicas': 0
    },
    'mappings': {
        'properties': {
            'அறிமுக_வருடம்': {
                'type': 'integer'
            },
            'பிறந்த_திகதி': {
                'type': 'date'
            }
        }
    }
}

indexName = 'actors'
my = es.indices.create(index=indexName, ignore=[400, 404], body=Settings)

# Uploading documents on elastic search
try:
    res = helpers.bulk(es, mycustom)
    print('working...')
except Exception as e:
    print(e)
    pass
