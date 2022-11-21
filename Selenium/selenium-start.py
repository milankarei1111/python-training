"""
#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#設定 Chrome Driver 的執行檔路徑
options=Options()
options.chrome_exeutable_path="D:\JOY-PC\程式\Python\python-training\Selenium\chromedriver.exe"
#建立 Driver 物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
#driver.get("https://www.google.com/")
#driver.close()
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print("----------------------------------------------")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()
