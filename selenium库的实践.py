from selenium import webdriver
import time
driver=webdriver.Chrome(r'C:\Users\林\Desktop\chromedriver.exe')
driver.get("https://www.airbnb.cn/s/Hangzhou--China/homes?refinement_paths%5B%5D=%2Fhomes&current_tab_id=home_tab&selected_tab_id=home_tab&screen_size=medium&hide_dates_and_guests_filters=false&place_id=ChIJmaqaQym2SzQROuhNgoPRv6c&map_toggle=false")
time.sleep(5)

name_list=driver.find_elements_by_css_selector("div._qrfr9x5")


price_list=driver.find_elements_by_css_selector("span._1d8yint7")
#print(price.text[3:])


    
    

for i in range(len(name_list)):
    print("name:%+30s"%name_list[i].text[:20]+'\t\t\t'+"price:%30s"%price_list[i].text[3:])

