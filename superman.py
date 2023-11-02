from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from faker import Faker

data = [[i.name(),i.email(),i.password()] for i in list(map(lambda x: Faker(), range(10)))]

options = webdriver.ChromeOptions()


options.add_argument("--incognito")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
s = Service('.\chromedriver.exe')

for i in range(10):
    driver = webdriver.Chrome(service=s,options=options)
    username = data[i][0]
    email = data[i][1]
    password = data[i][2]
    driver.implicitly_wait(10)

    # driver.set_page_load_timeout(20)

    driver.get("https://award.abga.asia/awards/the-most-popular-crypto-community%22")
    


    button = driver.find_element(By.XPATH,value="/html/body[@class='archive tax-awards term-the-most-popular-crypto-community term-23']/div[@class='vote-page']/div[@class='container px-5 lg:px-0']/div[@class='py-10']/div[@class='term-list py-10']/ul[@class='grid grid-cols-1 lg:grid-cols-4 gap-5 lg:gap-10 awards_term_list']/li[@id='vote_824']/div[@class='actions']/button[@class='custom_border py-2 px-3 flex-1 w-full']") 

    button.click()

    register = driver.find_element(By.XPATH,value="/html/body[@class='archive tax-awards term-the-most-popular-crypto-community term-23']/div[@id='login_modal']/div[@class='grid grid-cols-1 lg:grid-cols-3 overflow-hidden']/div[@class='col-span-2']/div[@id='login_modal_body']/form[@class='space-y-5']/p[@class='text-blue-500 text-xs px-5']/button")

    register.click()

    usernameInput = driver.find_element(By.XPATH, value="/html/body[@class='archive tax-awards term-the-most-popular-crypto-community term-23']/div[@class='jquery-modal blocker current']/div[@id='reg_modal']/div[@class='grid grid-cols-1 lg:grid-cols-3']/div[@class='col-span-2']/div[@id='reg_modal_body']/form[@class='space-y-5']/div[1]/input[@class='login-input']")

    usernameInput.send_keys(username)
    
    emailInput = driver.find_element(By.XPATH, value="/html/body[@class='archive tax-awards term-the-most-popular-crypto-community term-23']/div[@class='jquery-modal blocker current']/div[@id='reg_modal']/div[@class='grid grid-cols-1 lg:grid-cols-3']/div[@class='col-span-2']/div[@id='reg_modal_body']/form[@class='space-y-5']/div[2]/input[@class='login-input']")

    emailInput.send_keys(email)

    passwordInput = driver.find_element(By.XPATH, value="/html/body[@class='archive tax-awards term-the-most-popular-crypto-community term-23']/div[@class='jquery-modal blocker current']/div[@id='reg_modal']/div[@class='grid grid-cols-1 lg:grid-cols-3']/div[@class='col-span-2']/div[@id='reg_modal_body']/form[@class='space-y-5']/div[3]/input[@class='login-input']")
    passwordInput.send_keys(password)

    password2Input = driver.find_element(By.XPATH, value="/html/body[@class='archive tax-awards term-the-most-popular-crypto-community term-23']/div[@class='jquery-modal blocker current']/div[@id='reg_modal']/div[@class='grid grid-cols-1 lg:grid-cols-3']/div[@class='col-span-2']/div[@id='reg_modal_body']/form[@class='space-y-5']/div[4]/input[@class='login-input']")
    password2Input.send_keys(password)

    registerandlogin = driver.find_element(By.XPATH,value=r'//*[@id="reg_modal_body"]/form/div[5]/button')
   
    registerandlogin.click()
    
    vote = driver.find_element(By.XPATH, value=r'//*[@id="vote_824_btn"]')
    vote.click()
    
    driver.close()