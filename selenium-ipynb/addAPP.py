import time
def testAddApp(driver):
    AppName = 'new-app-1'

    driver.find_elements_by_css_selector("#app > div > div.tsl-layout-sider > div.menu-wrap > div > div > ul > div:nth-child(5) > li")[0].click()
    
    driver.find_elements_by_css_selector("#appContainer > div > div > div.tabel-header-box.flex-js > div.table-operate.flex-jc > button")[0].click()
    time.sleep(2)
    driver.find_elements_by_css_selector("body > div.ori-drawer.ori-drawer-right.ori-drawer-open > div.ori-drawer-content > div.ori-drawer-body > div > form > div:nth-child(1) > div > div > div > input")[0].send_keys(AppName)
    driver.find_elements_by_css_selector("body > div.ori-drawer.ori-drawer-right.ori-drawer-open > div.ori-drawer-content > div.ori-drawer-body > div > form > div:nth-child(2) > div > div > div > input")[0].send_keys(AppName)
    driver.find_elements_by_css_selector("body > div.ori-drawer.ori-drawer-right.ori-drawer-open > div.ori-drawer-content > div.ori-drawer-body > div > form > div:nth-child(3) > div > div.ori-input > div > input")[0].send_keys("114514")
    driver.find_elements_by_css_selector("body > div.ori-drawer.ori-drawer-right.ori-drawer-open > div.ori-drawer-content > div.ori-drawer-body > div > form > div:nth-child(4) > div > div.ori-input > div > input")[0].send_keys("name")
