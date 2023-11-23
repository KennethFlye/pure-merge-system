import json
import urllib.request

articles_list_url = 'http://127.0.0.1:5000/api/articles'
group_number_url = 'http://127.0.0.1:5000/api/articles/getgroupnr'


class DBApiAccess:
    def __init__(self):
        pass

    @staticmethod
    def get_articles_from_db():
        response = urllib.request.urlopen(articles_list_url)
        data = response.read()
        response_dict = json.loads(data)

        return response_dict

    @staticmethod
    def get_group_number():
        response = urllib.request.urlopen(group_number_url)
        data = response.read()
        response_dict = json.loads(data)

        return response_dict

    def post_to_db(self, article_dict):
        url = articles_list_url
        try:
            post_data = article_dict
            post_data = json.dumps([post_data]).encode('utf-8')

            req = urllib.request.Request(url, data=post_data, headers={'Content-Type': 'application/json'})
            response = urllib.request.urlopen(req)

            data = response.read().decode('utf-8')
            print(data)

            return response.status  # should always return 201 Ok

        except:
            return None
