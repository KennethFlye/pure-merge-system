import json
import urllib

status_url_db = ''

def getstatus_db():
    pass
    response = urllib.request.urlopen(status_url_db)
    data = response.read()
    response_dict = json.loads(data)

    return response_dict

