'''
CLEAN MAP
層級路徑,原始欄位,建議轉換型別,說明
1.records[0],curr_load,float,即時總負載
2.records[0],curr_util_rate,int,目前使用率
3.records[1],fore_peak_resv_rate,float,預估備轉率
4.records[1],publish_time,datetime,民國年格式時間
5.records[3],real_hr_peak_time,datetime,今日實績最高用電的時間點
'''
def clean_data(data: dict):
    clean_data = {}
    #1
    curr_load = data['records'][0]['curr_load']
    clean_data['curr_load']  = float(curr_load)
    #2
    curr_util_rate = data['records'][0]['curr_util_rate']
    clean_data['curr_util_rate']  = int(curr_util_rate)
    #3
    fore_peak_resv_rate = data['records'][1]['fore_peak_resv_rate']
    clean_data['fore_peak_resv_rate'] = float(fore_peak_resv_rate)
    #4
    publish_time = data['records'][1]['publish_time']
    clean_data['publish_time'] = timestamp_convert(publish_time)
    
    #5
    real_hr_peak_time = data['records'][3]['real_hr_peak_time']
    clean_data['real_hr_peak_time'] = real_hr_peak_time_convert(real_hr_peak_time)

    return clean_data

def timestamp_convert(unprocessed_str):
    # unprocessed_str 範例: "115.03.19(四)21:30"
    try:
        # 1. 拆出日期與時間：先去掉 (星期) 部分
        # 用 split('(') 拆開：["115.03.19", "四)21:30"]
        parts = unprocessed_str.split('(')
        date_part = parts[0]  # "115.03.19"
        time_part = parts[1].split(')')[-1]  # "21:30"

        # 2. 處理民國年轉西元
        yy, mm, dd = date_part.split('.')
        ad_year = str(int(yy) + 1911)
        
        # 3. 組合標準 ISO 格式: YYYY-MM-DD HH:MM:00
        clean_str = f"{ad_year}-{mm}-{dd} {time_part}:00"
        return clean_str
    except Exception as e:
        print(f"時間轉換錯誤: {e}")
        return None
    
def real_hr_peak_time_convert(unprocessed_str):
        unprocessed_str = unprocessed_str.replace(".","-") + ":00"
        return unprocessed_str


        
