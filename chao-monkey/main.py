from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time

# 设置浏览器驱动路径
driver_path = "D:\\test\\chromedriver.exe"  # 替换为你的驱动程序路径

# options = Options()
# options.add_argument('--ignore-certificate-errors')

# 创建浏览器实例
driver = webdriver.Chrome()

# 要访问的URL
url = "https://controll-panel-main-test-tacos-kernel-demo.tsl.x/device-management/access"  # 替换为你要访问的网页地址

# 打开网页
driver.get(url)
time.sleep(30)
print('OK')
# 记录已点击的元素 
clicked_elements = []

for i in range(0,100):
    # 获取页面上的元素列表
    elements = driver.find_elements(by=By.XPATH, value="//*")

    # 过滤已点击的元素
    elements = [e for e in elements if e not in clicked_elements]

    if len(elements) == 0:
        break
    
    try:
        
        # 随机选择一个元素并点击
        random_element = random.choice(elements)
        
        driver.execute_script("arguments[0].click();",random_element)

        # 记录已点击的元素
        clicked_elements.append(random_element)
    except:
        print("Error.")

    print("wait")
    # 等待一段时间
    time.sleep(2)

# 关闭浏览器
print(clicked_elements)
time.sleep(60)
driver.quit()