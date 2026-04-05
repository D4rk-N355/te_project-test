import sqlite3
import os
from service.config import DB_PATH

FULL_DB_PATH = DB_PATH / 'TE.db'

def init_taipower_table():
    os.makedirs(os.path.dirname(FULL_DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(FULL_DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Power_Load_Logs (
            obs_time TIMESTAMP PRIMARY KEY,      -- 存放 publish_time (清洗後)
            curr_load REAL,                      -- 目前總用電量 (MW)
            curr_util_rate INTEGER,               -- 目前使用率 (%)
            reserve_rate REAL,                   -- 預估備轉容量率 (%)
            real_hr_peak_time TIMESTAMP,         -- 新增：今日實績最高用電的時間點
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"台電資料表已在 {FULL_DB_PATH} 初始化完成。")

if __name__ == "__main__":
    init_taipower_table()