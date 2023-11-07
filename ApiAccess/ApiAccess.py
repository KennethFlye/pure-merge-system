import json
import urllib.request

status_url = "http://127.0.0.1:5000/api/status"
evaluate_url = "http://127.0.0.1:5000/api/check"


def getstatus():
    response = urllib.request.urlopen(status_url)
    data = response.read()
    response_dict = json.loads(data)

    return response_dict


def evaluate(title):
    url = evaluate_url
    postdata = {"title": title}
    postdata = json.dumps(postdata).encode('utf-8')

    req = urllib.request.Request(url, data=postdata, headers={'Content-Type': 'application/json'})
    response = urllib.request.urlopen(req)

    data = response.read().decode('utf-8')
    response_dict = json.loads(data)
    return response_dict
