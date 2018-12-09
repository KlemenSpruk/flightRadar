import urllib
import json


def get(url):
    """
    Returns json response for GET api url
    :param url: Url string
    :return: Json
    """
    opened_url = urllib.request.urlopen(url)
    data = opened_url.read()
    encoding = opened_url.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))
