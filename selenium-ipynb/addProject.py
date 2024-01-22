import time
def testAddProject(driver):
    ProjectName = 'New Project2'

    system_button = driver.find_elements_by_class_name("el-sub-menu")[5]
    system_button.find_elements_by_class_name("el-sub-menu__title")[0].click()
    user_button = system_button.find_elements_by_class_name("el-menu-item")[0]
    user_button.click()
    add_user_button = driver.find_elements_by_css_selector(".ori-button__contain.ori-button__contain-primary")[0]
    add_user_button.click()

    time.sleep(5)

    input_ele = driver.find_elements_by_css_selector("#app > div > div > div > div.steps-content__box > div.steps-content.cont-padding-right > div.step-operate__box.cont-padding-right > div.create-project > div > form > div.el-form-item.el-form-item--default.is-required > div > div > div > input")
    input_ele[0].send_keys(ProjectName)

    time.sleep(5)

    nextstep_button = driver.find_elements_by_css_selector("#app > div > div > div > div.steps-content__box > div.steps-action > button")
    nextstep_button[0].click()
    
    time.sleep(5)

    nextstep_button = driver.find_elements_by_css_selector("#app > div > div > div > div.steps-content__box > div.steps-action > button:nth-child(2)")
    nextstep_button[0].click()

    time.sleep(5)
    
    nextstep_button = driver.find_elements_by_css_selector("#app > div > div > div > div.steps-content__box > div.steps-action > button:nth-child(2)")
    nextstep_button[0].click()

    time.sleep(5)
    
    nextstep_button = driver.find_elements_by_css_selector("#app > div > div > div > div.steps-content__box > div.steps-action > button:nth-child(2)")
    nextstep_button[0].click()