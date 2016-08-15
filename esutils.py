#coding=utf-8
#author@alingse
#2016.05.16

from pyelasticsearch import ElasticSearch
import sys

#hosts = ['http://192.168.0.80']
def init_es(hosts=['127.0.0.1'],port=9200,):
    urls = map(lambda x:'http://'+x,hosts)
    es = ElasticSearch(urls = urls, port = port, timeout = 2*60)
    return es


def create(es,index):
    settings = {'settings': 
                    {'index': 
                        {'number_of_replicas': '0',
                         'number_of_shards': '5'
                         }
                    }
                }
    es.create_index(index, settings = settings)


def putmap(es,index,doc_type):
    #"date_detection":False,
    mapping = {
        doc_type: {
            "_all": {
                "analyzer": "ik_smart",
                "search_analyzer": "ik_smart",
                "term_vector": "no",
                "store": "false"
                },
            "properties": {
                "content": {
                    "type": "string",
                    "store": "no",
                    "term_vector": "with_positions_offsets",
                    "analyzer": "ik_smart",
                    "search_analyzer": "ik_smart",
                    "include_in_all": "true",
                    "boost": 8
                    }
                }
            }
        }
    
    es.put_mapping(index,doc_type,mapping)


def bulk_post(es,index, doc_type , docs = [],**kwargs):
    #,id_field = 'id'
    res = es.bulk_index(index,doc_type,docs,**kwargs)
    return res


if __name__ == '__main__':
    es = init_es()
    if len(sys.argv) == 1:
        pass
    elif sys.argv[1] == 'create':
        index = sys.argv[2]
        create(es,index)
    elif sys.argv[1] == 'putmap':
        index = sys.argv[2]
        doc_type = sys.argv[3]
        putmap(es,index,doc_type)
    elif sys.argv[1] =='delete_all':
        index = sys.argv[2]
        doc_type = sys.argv[3]
        es.delete_all(index,doc_type)
    elif sys.argv[1] == 'delete_index':
        index = sys.argv[2]
        res = es.delete_index(index)
        print res