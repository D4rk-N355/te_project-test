import requests
from service.config import SSL_CRT_FILE
def fetch_api():    
    url = "https://service.taipower.com.tw/data/opendata/apply/file/d006020/001.json"
    response = requests.get(url,verify = SSL_CRT_FILE)
    raw_json = response.json()

    return raw_json
