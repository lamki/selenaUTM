from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def login(browser):
    browser.get('https://intake.xxx.edu.my/login')
    browser.find_element_by_id('email').send_keys('email@domain.com')
    browser.find_element_by_id('password').send_keys('password')
    browser.find_element_by_tag_name('button').click()
    iterateWeb(browser)


def iterateWeb(brw):
    j = 0;

    # browser.get('https://intake.xxx.edu.my/intake/summary/' + str(i))
    for i in range(56500, 57375):
        ++j
        sleep(0.05)
        browser.get('https://intake.xxx.edu.my/intake/summary/' + str(i))
        # browser.get('https://intake.xxx.edu.my/intake/summary/xxxxx')
        try:
            name = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/span').text
            SCSR = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div/h4').text
            if SCSR == 'SARJANA MUDA SAINS KOMPUTER (RANGKAIAN DAN KESELAMATAN KOMPUTER)':
                print(name+" berminat!!! - " + str(i))
        except NoSuchElementException:
             print('',end='')
    print("Total human interested to join this program is: "+ str(j))


if __name__ == "__main__":
    browser = webdriver.Chrome("C:\\Users\\xxx\\xxx\\d.exe")
    login(browser)
