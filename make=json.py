import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def json_mk():
    driver = webdriver.Chrome()
    
    # 作成するJSONファイル名
    csv_file = open("D:\\npbWh\\player.csv", "r", encoding="utf-8")
    f = list(csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True))
    x = 0
    FILE_NAME = "npb_data.json"
    
    # データを蓄えるリスト
    all_data = []
   
    while x < len(f):
        s = str(f[x])
        cleaned_url_from_list = s.strip("['']").lstrip('\\ufeff')
        print(cleaned_url_from_list)
        
        try:
            driver.get(cleaned_url_from_list)
        except:
            print("miss")
            break
        
        notname = str(driver.title)
        pname = notname.split("（")[0]
        print(pname)
        
        wh = str(driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section[2]/table/tbody/tr[2]/td').text)
        
        split_string = wh.split("／")
        height = split_string[0]
        try:
            weight = split_string[1]
        except:
            wh = str(driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section[2]/table/tbody/tr[3]/td').text)
            split_string = wh.split("／")
            height = split_string[0]
            weight = split_string[1]
        
        # データを定義してリストに追加
        data = {
            "name": pname,
            "height": height,
            "weight": weight,
            "url": cleaned_url_from_list
        }
        all_data.append(data)
        
        print("データが追加されました: " + pname)
        x += 1

    # JSONファイルにリスト全体を書き込む
    with open(FILE_NAME, "w", encoding="utf-8") as json_file:
        json.dump(all_data, json_file, ensure_ascii=False, indent=4)
    
    print("JSONファイルが作成されました: " + FILE_NAME)
    csv_file.close()

json_mk()
