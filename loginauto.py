from selenium import webdriver

USERNAME = '940055'
PASSWORD = 'witeljambi'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://10.27.30.154/HouseKeeping/login.php')

user_input = driver.find_element_by_name('user')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_name('pass')
password_input.send_keys(PASSWORD)

login_buton = driver.find_element_by_class_name('login')
login_buton.click()