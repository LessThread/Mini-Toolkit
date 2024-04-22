def testLogin(driver):
    login_elem = driver.find_element_by_class_name("logincont")

    # 在 login 元素范围内查找 com-input 元素
    com_input_elem = login_elem.find_element_by_class_name("com-input")

    user_input = com_input_elem.find_element_by_tag_name("input")
    user_input.send_keys("newnew")

    # 使用 CSS 选择器查找元素
    passwd_elem =  driver.find_element_by_class_name("com-input.mr-bt-32")
    passwd_input = passwd_elem.find_element_by_tag_name("input")
 
    passwd_input.send_keys("!QAZ2wsx")


    button_element = driver.find_element_by_class_name("com-button.com-button-primary.mt-30")
    button_element.click()
