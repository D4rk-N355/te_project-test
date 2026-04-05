import sqlite3
from service.config import DB_PATH
db_path = DB_PATH



def init_taipower_table():
    conn = sqlite3.connect(db_path/'TE.db')
    cursor = conn.cursor()

    # 針對 001.json 結構設計的獨立資料表
    # 使用 obs_time 作為 Primary Key，確保每 10 分鐘一筆唯一紀錄
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Power_Load_Logs (
            obs_time TIMESTAMP PRIMARY KEY,  -- 存放 publish_time 轉換後的 ISO 時間
            curr_load REAL,                  -- 目前總用電量 (MW)
            curr_util_rate REAL,             -- 目前使用率 (%)
            reserve_rate REAL,               -- 預估備轉容量率 (%)
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"✅ 台電資料表已在 {db_path} 初始化完成。")

if __name__ == "__main__":
    init_taipower_table()