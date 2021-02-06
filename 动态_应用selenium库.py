from selenium import webdriver
driver=webdriver.Firefox(executable_path=r'C:\Users\林\Desktop\geckodriver.exe')
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
print(driver.page_source)
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
comment=driver.find_element_by_css_selector('div.reply-content')
content=comment.find_element_by_tag_name('p')
print(content.text)