from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import re
import csv
def seach_com():
    
    list_50 = ["a","i","u","e","o","ka","ki","ku","ke","ko","sa","si","su","se","so","ta","ti","tu","te","to","na","ni","nu","ne","no","ha","hi","hu","he","ho","ma","mi","mu","me","mo","ya","yu","yo","ra","ri","ru","re","ro","wa"]
    driver = webdriver.Chrome()
    base = 0
    for tango in list_50:
        
        url = f'https://npb.jp/bis/players/all/index_{tango}.html'
        
        driver.get(url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        counter = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/section[1]/div[2]/small').text
        match = re.search(r'\d+', counter)
        count = int(match.group())
        base = base + count
        print(base)
        links=[]
        while True:
            
            try:
                driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/section[2]/div[2]/a").click()
            except:
                links =links + soup.find_all('a', class_=re.compile('player_unit_1 old_player|player_unit_1'))
                break

        csvpath = "player.csv"
 
        with open(csvpath, "a", encoding="utf_8_sig") as f:
            writer = csv.writer(f, lineterminator='\n')
            for link in links:
                i=link.get('href')
                writer.writerow([f"https://npb.jp/{i}"])

         

    
   
seach_com()