from selenium import webdriver
import webbrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def t_mobile_script():
    # create an instance of Chrome with the excludeSwitches and window-size options
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    # maximize the window to full screen
    driver.maximize_window()


    # navigate to the website
    driver.get('https://nowymoj.t-mobile.pl/')

    # wait for the cookies button to appear and click on it
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'didomi-notice-agree-button'))).click()

    # minimize the window to taskbar
    driver.minimize_window()

    # wait for the email input field to appear and enter the email address
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'email'))).send_keys('tiomu44@gmail.com')

    # click on the "Dalej" button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.primary-button-lg.button'))).click()

    # wait for the password input field to appear and enter the password
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys('Tema456q')

    # click on the "Zaloguj się" button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'emailPasswordSubmit'))).click()

    print('Enter the 6-digit code: ')
    otp_code = input() # prompt the user to enter the code in the terminal

    # wait for the OTP input field to appear and enter the OTP code
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'otpInput'))).send_keys(otp_code)

    # press the "Zaloguj się" button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'submit1'))).click()

    # wait for the "Ok, rozumiem" button to appear and click on it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.primary-button-lg.first-letter-up.mt-15.w-100.m-0'))).click()


    # press the "Zarzadzaj kontami" button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.CommonDashboard_button__23ay9.secondary-button-black-md.d-block.px-0.active'))).click()


    # wait for the "Przełącz konto" buttons to appear and store them in a list
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.ManagementModal_accountText__2y9EG.ManagementModal_switchAccountBtn__16Yqe.secondary-button-black-sm.action-button.d-none.d-xl-inline-block')))
    switch_account_buttons = driver.find_elements(By.CSS_SELECTOR, 'a.ManagementModal_accountText__2y9EG.ManagementModal_switchAccountBtn__16Yqe.secondary-button-black-sm.action-button')

    # open all the "Przełącz konto" buttons in new tabs
    for switch_account_button in switch_account_buttons:
        driver.execute_script("window.open(arguments[0].href,'_blank');", switch_account_button)

    # wait for all the tabs to open
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(len(switch_account_buttons) + 1))

    #wait for 5 seconds after clicking the "Ok, rozumiem" button
    time.sleep(2)

    # switch to the first window handle and close it
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    #wait for 5 seconds after clicking the "Ok, rozumiem" button
    time.sleep(2)

    # switch to the first window handle
    driver.switch_to.window(driver.window_handles[0])

    #wait for 5 seconds after clicking the "Ok, rozumiem" button
    time.sleep(2)


    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        time.sleep(1)
        service_number = driver.find_element(By.CLASS_NAME, 'service-number').text
        service_name = driver.find_element(By.CLASS_NAME, 'service-name.text-truncate').text
        print(f'{service_name} - {service_number}:')
        elements = driver.find_elements(By.CLASS_NAME, 'col-6.col-md-4.mb-1.d-inline-block.ml-md-n1.ml-lg-0.text-right.pr-10.pl-0.px-md-7.px-lg-10')
        for element in elements:
            print(element.text)

        print('\n')


    # minimize the window to taskbar
    driver.minimize_window()

    input('Press Enter to exit')
    # close the remaining tabs and keep the browser open until the user closes it
    driver.quit()
