import json
import time
import gzip
from service.config import RAW_JSON_DIR, DB_PATH
import sqlite3

def backup_json(data: json):
    with gzip.open(f"{RAW_JSON_DIR}/{time.time()}.json.gz","wt") as file:
        json.dump(data,file)

def save_to_db(cleaned_data):
    # 請確保 DB 路徑正確
    conn = sqlite3.connect(f"{DB_PATH}/TE.db")
    cursor = conn.cursor()

    # 使用具名占位符 (Named Placeholders)，這能直接對應你的字典 Key
    sql = '''
    INSERT OR IGNORE INTO Power_Load_Logs (
        curr_load, 
        curr_util_rate, 
        reserve_rate, 
        obs_time, 
        real_hr_peak_time
    ) VALUES (
        :curr_load, 
        :curr_util_rate, 
        :fore_peak_resv_rate, 
        :publish_time, 
        :real_hr_peak_time
    )
    '''
    
    try:
        cursor.execute(sql, cleaned_data)
        if cursor.rowcount > 0:
            print(f"成功寫入電力數據：{cleaned_data['publish_time']}")
        else:
            print(f"資料已存在，跳過重複項：{cleaned_data['publish_time']}")
        
        conn.commit()
    except Exception as e:
        print(f"資料庫寫入失敗: {e}")
    finally:
        conn.close()
