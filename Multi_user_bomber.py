'''
@Author - Abhishek Kumar
Disclaimer  - This code is only for educational and entertainment purpose. Don't use it to harm anyone.
'''

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://web.whatsapp.com/')

input("Scan the Qr code in the browser for whatsapp and press Enter")
no_of_users = int(input("Enter the number of target users :"))
target_users = []
for i in range(no_of_users):
    target = input('Enter the name of person or group : ')
    target_users.append(target)
message = input('Type the message here : ')
no_of_msg = int(input('Enter the number of messages you want to send : '))

input('Press Enter Again')
for name in target_users:
    target_user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    target_user.click()

    msg_box = driver.find_element_by_class_name('_1Plpp')

    for i in range(no_of_msg):
        msg_box.send_keys(message)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
