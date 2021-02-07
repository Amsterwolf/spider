from selenium import webdriver
import time

#限制图片、css、JS加载
options=webdriver.ChromeOptions()
prefs={
    'profile.default_content_setting_values':{
        'images':2,
        #'permissions.default.stylesheet':2,
        #'javascript':2,
    }
}
options.add_experimental_option('prefs',prefs)
driver=webdriver.Chrome(executable_path=r'C:\Users\林\Desktop\chromedriver.exe',options=options)
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
time.sleep(10)
#print(driver.page_source)
flag=1
cot=1
ten_page=1
while ten_page:
    
    
    for i in range(1,11):

        #下滑至页面底部(加载按钮)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        
        #转移至iframe(包含评论和按钮)
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
        #隐性等待评论加载
        driver.implicitly_wait(10)
        comment_list=driver.find_elements_by_css_selector('div.reply-content')
        for eachcomment in comment_list:
            content=eachcomment.find_element_by_tag_name('p')
            print(f"page {(ten_page-1)*10+i} NO.{cot}:",content.text[:100])
            cot+=1
        
        
        

        if i!=10:
            #按钮列表
            bottons=driver.find_elements_by_css_selector('button.page-btn')
          
            #下一页按钮
            try:
                print(f"bot[{i}].text:",bottons[i].text)
                bottons[i].click()     
            except:
                flag=0
        else:   
            try:
                page_last_botton=driver.find_element_by_css_selector('button.page-last-btn')
                print("last_bot.text:",page_last_botton.text)
                page_last_botton.click()
            except:
                flag=0
        
    
   
        if not flag:
            break

        #转移至主页
        driver.switch_to.default_content()
        #加载评论（不然会加载出上一页的评论）
        time.sleep(1.5)
        
       
       
        
    if not flag:
        break
    
    ten_page+=1

