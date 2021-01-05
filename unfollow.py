#usr/bin/python3.8
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date, datetime

username = '<YOUR USERNAME HERE>'
password = '<YOUR PASSWORD HERE>'

class InstaUnfollowers:
    def __init__(self, username, password):
        global response
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome(ChromeDriverManager().install()) #webdriver.Firefox() to use Firefox
        self.driver.set_window_size(600, 1080)
        self.driver.set_window_position(1000, 0)
        self.driver.get("https://instagram.com")
        sleep(2)
        # instagram login
        print(f"[{date.today().strftime('%Y-%m-%d')} {datetime.now().strftime('%H:%M:%S')}] Logging In")
        username_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        username_type.send_keys(username)
        password_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password_type.send_keys(password)
        submit = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        submit.click()
        sleep(3)
        try:
            ad = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
            print(f"[{date.today().strftime('%Y-%m-%d')} {datetime.now().strftime('%H:%M:%S')}] [{self.username}] Successful LogIn")
            ad.click()
            sleep(3)
            ad = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
            ad.click()
        except:
            response = f"[{today.strftime('%Y-%m-%d')} {now.strftime('%H:%M:%S')}] Sorry, username or password was incorrect." + \
                       f"[{date.today().strftime('%Y-%m-%d')} {datetime.now().strftime('%H:%M:%S')}] [{self.username}] Time expired"
            self.driver.close()

    def unfollow(self):
        global response
        User = self.driver.find_element_by_xpath("html/body/div/section/nav/div[2]/div/div/div[2]/input")
        custom_list = ['<add all usernames here>', '<you can add how many you want!>'] # usernames to unfollow

        for i, user in enumerate(custom_list):
            try:
                User = self.driver.find_element_by_xpath("html/body/div/section/nav/div[2]/div/div/div[2]/input")
                User.send_keys(user)
                sleep(1)
                User_profile = self.driver.find_element_by_xpath("html/body/div/section/nav/div[2]/div/div/div[2]/div[4]/div/a/div/div[2]/span")
                User_profile.click()
            except:
                response = f"[{today.strftime('%Y-%m-%d')} {now.strftime('%H:%M:%S')}] Can't find this username"
                self.driver.close()


            print(f"[{date.today().strftime('%Y-%m-%d')} {datetime.now().strftime('%H:%M:%S')}] [{self.username}] Unfollow [{i+1}/{len(custom_list)}] Unfollowing {custom_list[i]}")
            sleep(3)
            try:
                self.driver.find_element_by_xpath("//span[contains(@aria-label,'Following')]").click()
                sleep(3)
                unfollow = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button")
                unfollow.click()
                print(f"[{date.today().strftime('%Y-%m-%d')} {datetime.now().strftime('%H:%M:%S')}] [{self.username}] You are not following anymore {user}")
                sleep(2)
            except:
                print(f"[{date.today().strftime('%Y-%m-%d')} {datetime.now().strftime('%H:%M:%S')}] [{self.username}] You already unfollow {user} ")
                self.driver.close()

today = date.today()
now = datetime.now()

try:
    instabot = InstaUnfollowers(username, password)
    instabot.unfollow()
    instabot.driver.close()
except:
    print(response)

