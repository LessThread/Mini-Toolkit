
def testAddUser(driver):
    username = "newnew2"
    name = "newnew2"
    phone = "13245678910"
    passwd = "!QAZ2wsx"

    # 选中新增用户
    system_button = driver.find_elements_by_class_name("el-sub-menu")[5]
    system_button.find_elements_by_class_name("el-sub-menu__title")[0].click()
    user_button = system_button.find_elements_by_class_name("el-menu-item")[2]
    user_button.click()
    add_user_button = driver.find_elements_by_css_selector(".ori-button__contain.ori-button__contain-primary")[0]
    add_user_button.click()

    add_user_view = driver.find_elements_by_class_name("ori-drawer-content")[0]
    
    # 添加用户账号
    add_user_username_input = add_user_view.find_elements_by_css_selector(".el-form-item__content")[0].find_elements_by_class_name("ori-input__inner")[0]
    add_user_username_input.find_element_by_class_name("input-inner").send_keys(username)

    # 添加名称
    add_user_username_input = add_user_view.find_elements_by_css_selector(".el-form-item__content")[2].find_elements_by_class_name("ori-input__inner")[0]
    add_user_username_input.find_element_by_class_name("input-inner").send_keys(name)

    # 添加手机信息
    add_user_username_input = add_user_view.find_elements_by_css_selector(".el-form-item__content")[3].find_elements_by_class_name("ori-input__inner")[0]
    add_user_username_input.find_element_by_class_name("input-inner").send_keys(phone)

    # 指定角色信息
    add_user_username_input = add_user_view.find_elements_by_css_selector(".el-form-item__content")[5].find_elements_by_class_name("ori-input__inner")[0]
    add_user_username_input.find_element_by_class_name("input-inner").click()
    driver.find_elements_by_id("NAx2pNBWFLx6nTQCtVE262XP1SkL7Gbx")[1].click()

    # 设定初始密码
    add_user_username_input = add_user_view.find_elements_by_css_selector(".el-form-item__content")[7].find_elements_by_class_name("ori-input__inner")[0]
    add_user_username_input.find_element_by_class_name("input-inner").send_keys(passwd)

    # 点击添加确定
    add_user_ok_button = add_user_view.find_elements_by_css_selector(".ori-button__contain.ori-button__contain-primary.ori-button.mr-rt-8")
    add_user_ok_button[0].click()
    