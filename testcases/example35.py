# https://dumskaya.net/
def register_user():
    import time
    from factory.new_user import User
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    import os
    from selenium.webdriver.common.by import By
    from xpath.registration_page import registration
    from xpath.home_page import home
    from details.registration_page import reg_page

    my_user = User()
    options = ChromeOptions()
    foptions = FirefoxOptions()
    options.headless = False  # True Запуск теста без включения браузера

    path = f'{os.getcwd()}/drivers/chromedriver'
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://dumskaya.net/'
    e1_page = reg_page()
    driver.maximize_window()
    driver.get(url)

    enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', home.xpath_enter_button)))
    enter_button.click()
    enter_registration_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', home.xpath_enter_registration_button)))
    enter_registration_button.click()

    e1_page.email_field(driver, my_user.email)
#Пользователь с таким адресом электронной почты уже зарегистрирован.Укажите е-mail. Он нужен для входа в сайт.

    e1_page.nick_field(driver, my_user.nick)
#если не ввести ник, то ошибка - Пользователь с таким ником уже зарегистрирован. Придумайте другой. Укажите ник.

    # e1_page.password_field(driver, my_user.password)
#Длина пароля должна быть не меньше 6 символов. А то его у вас украдут, а мы виноваты будем. Пароли не совпадают.

    e1_page.password2_field(driver, my_user.password)
# Пароли не совпадают.
    e1_page.female_radio(driver)


    register_gender_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', registration.xpath_register_button)))
    register_gender_button.click()

#1LOGIN
#     n = '''Пользователь с таким ником уже зарегистрирован. Придумайте другой
# Укажите ник.'''


#2EMAIL
#     n = '''Пользователь с таким адресом электронной почты уже зарегистрирован.
# Укажите е-mail. Он нужен для входа в сайт.'''


#3PASSWORD
    n = '''Длина пароля должна быть не меньше 6 символов. 
А то его у вас украдут, а мы виноваты будем. Пароли не совпадают.'''


#1LOGIN
    # login_textarea = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located(('xpath', '//tr/td/div[contains(text()," ")]')))
    # login_err = login_textarea.text
    
# #2EMAIL
#     login_textarea = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located(('xpath', '//tr/td/div[contains(text()," ")]')))
#     login_err = login_textarea.text

#3 password
    login_textarea = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', '//tr/td/div[contains(text()," ")]')))
    login_err = login_textarea.text

    # time.sleep(5000)
#1
    # driver.close()
    # if n == login_err:
    #     print('Great!')
    # return n, login_err  # 'Пользователь с таким ником уже зарегистрирован. Придумайте другой'
    #
 #2
#     driver.close()
#     if n == login_err:
#         print('Great!')
#     return n, login_err  # 'Пользователь с таким адресом электронной почты уже зарегистрирован.
    # # Укажите е-mail. Он нужен для входа в сайт.'

#3
    driver.close()
    if n == login_err:
        print('Perfect!')
    return n, login_err  # 'Длина пароля должна быть не меньше 6 символов. А то его у вас украдут, а мы виноваты будем. Пароли не совпадают.'

if __name__ == '__main__':
    print(register_user())
