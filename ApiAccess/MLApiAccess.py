import json
import urllib.request

status_url_ml = "http://127.0.0.1:5000/api/status"
evaluate_url_ml = "http://127.0.0.1:5000/api/check"
compare_titles_ml = "http://127.0.0.1:5000/api/predict/compare"


class MLApiAccess:
    def __init__(self):
        pass

    def getstatus_ml(self):
        response = urllib.request.urlopen(status_url_ml)
        data = response.read()
        response_dict = json.loads(data)

        return response_dict

    def evaluate_ml(self, title):
        url = evaluate_url_ml
        postdata = {"title": title}
        postdata = json.dumps(postdata).encode('utf-8')

        req = urllib.request.Request(url, data=postdata, headers={'Content-Type': 'application/json'})
        response = urllib.request.urlopen(req)

        data = response.read().decode('utf-8')
        response_dict = json.loads(data)
        return response_dict

    def evaluate_titles(self, title1, title2):
        url = compare_titles_ml

        post_data = {"title1": title1, "title2": title2}
        post_data = json.dumps(post_data).encode('utf-8')

        req = urllib.request.Request(url, data=post_data, headers={'Content-Type': 'application/json'})
        response = urllib.request.urlopen(req)

        data = response.read().decode('utf-8')
        response_dict = json.loads(data)

        print(response_dict)
