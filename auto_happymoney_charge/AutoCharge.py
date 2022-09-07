from posixpath import split
from selenium import webdriver
import time as t
from datetime import datetime
from selenium.webdriver.common.keys import Keys



print(datetime.now())

pin_num = "0000-1111-2222-3333-20220427"
list_pin_num = pin_num.split('-')
#=====================초기변수 선언=========================
ID = "ID"
PW = "PW"

driver_path ='C:/python/Discord_Bot/auto_cultureland_charge/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
#=======================================================



#==================함수=======================
def click_virtual_btn_code(driver, target, num_1):
    board = driver.find_elements_by_class_name('transkey_div.transkey_number2_div')
    for b in board:
        if 'display: block' in b.get_attribute('style'):
            board = b
    board = board.find_elements_by_tag_name('img')
    for b in board:
        if target in b.get_attribute('alt'):
            b.click()
            break

def click_virtual_btn(driver, target):
    if target.isupper():
        shitf_c = driver.find_element_by_xpath("//img[@alt='쉬프트']")
        shitf_c = shitf_c.find_element_by_xpath("./../..")
        shitf_c.click()
        
        func_g = driver.find_element_by_xpath(f"//img[@alt='대문자{target}']")
        func_g = func_g.find_element_by_xpath("./../..")
        func_g.click()
        
        shitf_c = driver.find_element_by_xpath("//img[@alt='쉬프트']")
        shitf_c = shitf_c.find_element_by_xpath("./../..")
        shitf_c.click()
        
    elif target.isalnum() == False:
        alphs_c = driver.find_element_by_xpath("//img[@alt='특수키']")
        alphs_c = alphs_c.find_element_by_xpath("./../..")
        alphs_c.click()
        
        func_g = driver.find_element_by_xpath(f"//img[@alt='골뱅이']")
        func_g = func_g.find_element_by_xpath("./../..")
        func_g.click()
        
        alphs_c = driver.find_element_by_xpath("//img[@alt='특수키']")
        alphs_c = alphs_c.find_element_by_xpath("./../..")
        alphs_c.click()
        
    else:
        func_g = driver.find_element_by_xpath(f"//img[@alt='{target}']")
        func_g = func_g.find_element_by_xpath("./../..")
        func_g.click()
#==============================================



#==============컬쳐랜드 탭 열기=================
driver.get("https://m.happymoney.co.kr/svc/view/charge/charge/chargeHappyMoney")
#==============================================

driver.find_element_by_id('memberId').send_keys(ID)

driver.find_element_by_name('memberPwd').click()
for i in PW:
    click_virtual_btn(driver, i)
driver.find_element_by_xpath('//*[@id="loginWrap"]/section[1]/div[2]/input').click()


driver.find_element_by_id('originalName1_0').click()
for f_pin_code_num in list_pin_num[0]:
    click_virtual_btn(driver, f_pin_code_num)

# for s_pin_code_num in list_pin_num:
#     driver.find_element_by_id('originalName2_0').send_keys(s_pin_code_num)

for i in range(2,5):
    print(i)
    driver.find_element_by_id(f'originalName{i}_0').send_keys(list_pin_num[i - 1])
driver.find_element_by_id('expire0').send_keys(list_pin_num[4])


driver.find_element_by_xpath('//*[@id="contents"]/button[2]').click()
t.sleep(1)
accept_message = driver.switch_to_alert()
accept_message.accept()