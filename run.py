from service.fetch import fetch_api
from service.storage import backup_json, save_to_db
from service.cleaner import clean_data

try :
    raw_json = fetch_api()
    backup_json(raw_json)
    processed_data = clean_data(raw_json)
    save_to_db(processed_data)
    
except Exception as e:
    print(e)
