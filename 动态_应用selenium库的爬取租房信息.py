from selenium import webdriver
import time

#限制图片、css、js加载
options=webdriver.ChromeOptions()
prefs={
    "profile.default_content_setting_values":{
        "images":2,
        "permissions.default.stylesheet":2,
        "javascript":2,

    }
}
options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(r'C:\Users\林\Desktop\chromedriver.exe',options=options)
#爬取租房网站前五页数据
for i in range(5):
    driver.get("https://www.airbnb.cn/s/Hangzhou--China/homes?map_toggle=false&items_offset="+str(i*20) )
    time.sleep(5)

    rent_house_list=driver.find_elements_by_css_selector("div._gig1e7")
    for house in rent_house_list:
        name=house.find_element_by_css_selector("div._qrfr9x5").text
        price=house.find_element_by_css_selector("span._1d8yint7").text[3:]
        house_type_info_list=house.find_element_by_css_selector("span._faldii7").text.split(" · ")
        house_type=house_type_info_list[0]
        bed_num=house_type_info_list[1]
        try:
            comments_num=house.find_element_by_css_selector("span._69pvqtq").text
        except:
            comments_num=0
        print(name,price,house_type,bed_num,comments_num)
  
    


