from service.fetch import fetch_api
from service.storage import backup_json
from service.cleaner import clean_data

try :
    raw_json = fetch_api()
    backup_json(raw_json)
    print(raw_json)
    clean_data = clean_data(raw_json)
    print("*******************************")
    print(clean_data)
except Exception as e:
    print(e)
