from selenium import webdriver
import webbrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time
import re
import sys
import colorama
from colorama import Fore, Style
colorama.init()

print("V5")
# create an instance of Chrome with the excludeSwitches and window-size options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
# maximize the window to full screen
driver.maximize_window()
# navigate to the website
driver.get('https://nowymoj.t-mobile.pl/')
# wait for the cookies button to appear and click on it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID, 'didomi-notice-agree-button'))).click()
# minimize the window to taskbar
driver.minimize_window()
# wait for the email input field to appear and enter the email address
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID, 'email'))).send_keys('tiomu44@gmail.com')
# click on the "Dalej" button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, '.primary-button-lg.button'))).click()
# wait for the password input field to appear and enter the password
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID, 'password'))).send_keys('Tema456q')
# click on the "Zaloguj się" button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID, 'emailPasswordSubmit'))).click()
print('Enter the 6-digit code: ')
otp_code = input()  # prompt the user to enter the code in the terminal
# wait for the OTP input field to appear and enter the OTP code
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID, 'otpInput'))).send_keys(otp_code)
# press the "Zaloguj się" button
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'submit1'))).click()
# wait for the "Ok, rozumiem" button to appear and click on it
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, 'button.primary-button-lg.first-letter-up.mt-15.w-100.m-0'))).click()
# press the "Zarzadzaj kontami" button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                            'a.CommonDashboard_button__23ay9.secondary-button-black-md.d-block.px-0.active'))).click()
# wait for the "Przełącz konto" buttons to appear and store them in a list
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                                     'a.ManagementModal_accountText__2y9EG.ManagementModal_switchAccountBtn__16Yqe.secondary-button-black-sm.action-button.d-none.d-xl-inline-block')))
switch_account_buttons = driver.find_elements(
    By.CSS_SELECTOR, 'a.ManagementModal_accountText__2y9EG.ManagementModal_switchAccountBtn__16Yqe.secondary-button-black-sm.action-button')
# open all the "Przełącz konto" buttons in new tabs
for switch_account_button in switch_account_buttons:
    driver.execute_script(
        "window.open(arguments[0].href,'_blank');", switch_account_button)
# wait for all the tabs to open
WebDriverWait(driver, 10).until(
    EC.number_of_windows_to_be(len(switch_account_buttons) + 1))
# wait for 5 seconds after clicking the "Ok, rozumiem" button
""" time.sleep(2) """
# switch to the first window handle and close it
driver.switch_to.window(driver.window_handles[0])
driver.close()
# wait for 5 seconds after clicking the "Ok, rozumiem" button
""" time.sleep(2) """
# switch to the first window handle
driver.switch_to.window(driver.window_handles[0])
# wait for 5 seconds after clicking the "Ok, rozumiem" button
""" time.sleep(2) """

# maximize the window to full screen
driver.maximize_window()

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    service_number = driver.find_element(By.CLASS_NAME, 'service-number').text
    service_name = driver.find_element(
        By.CLASS_NAME, 'service-name.text-truncate').text
    
    """ cubot x50 - 692 693 032: """
    print(Style.BRIGHT, service_name + '-' + service_number, Fore.RESET, Style.RESET_ALL)

    # Map the elements with class 'col-6 col-md-8 mb-1 pr-0 d-inline-block' to the elements with class 'col-6 col-md-4 mb-1 d-inline-block ml-md-n1 ml-lg-0 text-right pr-10 pl-0 px-md-7 px-lg-10'
    elements_map = {}
    col1_elements = driver.find_elements(
        By.CLASS_NAME, 'col-6.col-md-8.mb-1.pr-0.d-inline-block')
    col2_elements = driver.find_elements(
        By.CLASS_NAME, 'col-6.col-md-4.mb-1.d-inline-block.ml-md-n1.ml-lg-0.text-right.pr-10.pl-0.px-md-7.px-lg-10')
    for i in range(len(col1_elements)):
        if i < len(col2_elements):
            value = col2_elements[i].text.split(' ')[1].replace(',', '.')
            if 'MB' in col2_elements[i].text:
                value = float(value) * 0.001
            else:
                value = float(value)
            elements_map[col1_elements[i].text] = value
        else:
            elements_map[col1_elements[i].text] = '-'

        # Click on the Lista połączen element
    try:
        button = driver.find_element(By.XPATH, "//span[@class='SubheaderSingleButton_item__3PJ8c']/span[contains(text(), 'Lista połączeń')]")
        button.click()
        #time.sleep(1)
    except:
        pass
    
for handle in driver.window_handles: 
    #Find date
    try:
        # Wait for either the CallListSingleDay_title__U8sOz element or PaymentHistoryEmpty_title__2FR30 element to appear
        title_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'pt-15.pt-md-20.pb-7.pb-md-10.pl-10.pl-md-20.CallListSingleDay_title__U8sOz')))
        title = title_element.text
        is_date = True

        # Convert date from Polish to "dd.mm.yyyy" format
        day, month, year = title.split()
        if month == 'stycznia':
            month_num = 1
        if month == 'lutego':
            month_num = 2
        if month == 'marca':
            month_num = 3
        elif month == 'kwietnia':
            month_num = 4
        elif month == 'maja':
            month_num = 5
        elif month == 'czerwca':
            month_num = 6
        elif month == 'lipca':
            month_num = 7
        elif month == 'sierpnia':
            month_num = 8
        elif month == 'września':
            month_num = 9
        elif month == 'października':
            month_num = 10
        elif month == 'listopada':
            month_num = 11
        elif month == 'grudnia':
            month_num = 12
        else:
            raise ValueError(f'Invalid month: {month}')
        date_str = f'{day.zfill(2)}.{str(month_num).zfill(2)}.{year}'

        print(f'DATE: {Style.BRIGHT}{date_str}{Style.RESET_ALL}')

    except TimeoutException:
        try:
            empty_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'PaymentHistoryEmpty_title__2FR30.pt-15.pb-10')))
            print('NO DATE')
            is_date = False
        except TimeoutException:
            print('Element not found')

    # Print the elements_map
    sum_gb = 0
    for key, value in elements_map.items():
        if 'Limit Danych UE' in key:
            continue
        print(f'{key.ljust(40)} {value}')
        if isinstance(value, float):
            sum_gb += value
    
    if is_date:
        # Check if it's less than 3 days from date_str
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        delta = datetime.now() - date_obj
        if delta.days < 3 and sum_gb <= 6:
            print(f'Sum of GB is {Style.BRIGHT}{Fore.RED}{sum_gb}{Style.RESET_ALL}')
        else:
            print(f'Sum of GB is {Style.BRIGHT}{sum_gb}{Style.RESET_ALL}')
    else:
        print(f'Sum of GB is {Style.BRIGHT}{sum_gb}{Style.RESET_ALL}')


print()
    
    

# minimize the window to taskbar
driver.minimize_window()
input('Press Enter to exit')
# close the remaining tabs and keep the browser open until the user closes it
driver.quit()
# end the program
sys.exit()