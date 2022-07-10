from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

chrome_driver_path = CHROMEDRIVER_PATH
SIMILAR_ACCOUNT = TARGET_IG_ACCOUNT
USERNAME = YOUR_YOURNAME
PASSWORD = YOUR_PASSWORD


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.click()
        username.send_keys(USERNAME)
        time.sleep(1)

        password.click()
        password.send_keys(PASSWORD)
        time.sleep(1)

        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(3)

    def follow(self):
        while True:
            try:
                list_of_people = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
                for person in list_of_people:
                    if person.text == "Follow":
                        person.click()
                        time.sleep(random.randint(30, 60))
                    print(len(list_of_people))

                self.driver.execute_script("argument[0].scrollIntoView(true);", list_of_people[-1])

            except Exception as e:
                print(e)


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()