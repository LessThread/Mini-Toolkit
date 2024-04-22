import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException

def random_click(driver):
    try:
        # 检查浏览器窗口是否仍然打开
        if driver.current_url:
            # 查找页面上的所有可点击元素
            clickable_elements = driver.find_elements(By.XPATH, '//*[self::a or self::button or self::input[@type="submit"]]')

            if clickable_elements:
                random_element = random.choice(clickable_elements)
                random_element.click()
                time.sleep(3)  # 等待页面加载，可以根据实际情况调整时间
            else:
                print("页面中没有找到可点击元素")
        else:
            print("浏览器窗口已关闭")

    except StaleElementReferenceException as stale_ex:
        print("元素引用已过时，可能页面已经发生变化")
        print(f"发生异常: {stale_ex}")

    except WebDriverException as wd_ex:
        print("WebDriver异常，可能浏览器窗口已关闭")
        print(f"发生异常: {wd_ex}")


if __name__ == "__main__":
    
    # 创建Chrome浏览器实例
    driver = webdriver.Chrome()

    for _ in range(10):
        try:
            # 打开初始页面
            driver.get("https://baidu.com")

            # 模拟随机点击，可以根据需要设置循环次数或其他条件
            random_click(driver)
            time.sleep(1)

        except Exception as e:
                print(f"发生异常: {e}")

    # 关闭浏览器
    print("OK")
    driver.quit()