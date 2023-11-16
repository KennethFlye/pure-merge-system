import json
import urllib.request

status_url_db = 'http://127.0.0.1:5000/api/articles'
group_number_url = 'http://127.0.0.1:5000/api/articles/getgroupnr'


class DBApiAccess:
    def __init__(self):
        pass

    @staticmethod
    def get_articles_from_db():
        response = urllib.request.urlopen(status_url_db)
        data = response.read()
        response_dict = json.loads(data)

        return response_dict

    def get_group_number(self):
        response = urllib.request.urlopen(group_number_url)
        data = response.read()
        response_dict = json.loads(data)

        return response_dict
