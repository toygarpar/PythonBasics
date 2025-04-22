from instagramUserInfo import email, username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class Instagram:
    def __init__(self, email: str, password):
        self.browserProfile = webdriver.ChromeOptions()   #yabancı dil ingilizce ekleme optionı
        self.browserProfile.add_experimental_option("pref", {"intl.accept_languages": "en, en_US"})
        
        
        self.browser = webdriver.Chrome("chromedriver.exe", chrome_options=self.browserProfile)
        self.email = email
        self.password = password
        self.username = username
        
        
    def sign_in(self):
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(3)
        emailInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        
        
        
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
        #self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        
    def get_followers(self):
        
        
        
        bilgikaydet = self.browser.find_element_by_css_selector(".xyamay9").find_element_by_css_selector("._acan")
        bilgikaydet.click()
        
        time.sleep(4)
        
        bildirimacma =  self.browser.find_element_by_css_selector("._a9-z").find_element_by_css_selector("._a9--._ap36._a9_1")
        # ("div[role="dialog"])
        bildirimacma.click()
        
        time.sleep(3)
        
        self.browser.get(f"https://www.instagram.com/{self.username}")
        
        time.sleep(2)
        
        
        
        
        
        takipci = self.browser.find_element_by_css_selector(".x78zum5").find_element_by_tag_name("header").find_elements_by_css_selector("li")
        
        
        
        takipci[1].click()
        
        time.sleep(2) 
        
        followerz = self.browser.find_element_by_css_selector("div[role=dialog]").find_element_by_css_selector("._aano").find_elements_by_css_selector("a")    
        followerCount = len(find_elements_by_css_selector("a"))
        
        print(f"first count: {followerCount}")   #scroll down bölümüne geç
        
        #☺buraya scroll down döngü kodu gelecek
        action = webdriver.ActionChains(self.browser)

        while True:
            followerz.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            
            
            newCount = len(find_elements_by_css_selector("a"))
            
            if followerCount != newCount:
                followerCount = newCount
                print(f"updated count : {newCount} ")
                time.sleep()
                
            else:
                break
        
        #yukardaki kot çalışmayabilir
        followliste = followerz.find_elements_by_css_selector("a")
        
        for user in followliste:
            link = user.get_attribute("href")
            print(link)
            
    
    
    
    def follow_user(self, username):
        self.browser.get("https:www.instagram.com/" + username)
        time.sleep(2)
        
        follow_button  = self.browser.find_element_by_tag_name("button")
        print(follow_button.text)
        
        if follow_button != "Takiptesin" or "Following":
            follow_button.click()
            time.sleep(2)
        else:
            print("Kullanıcıyı zaten takip ediyorsunuz")
        
        
        
        
        
insta = Instagram(email, password)
insta.sign_in()
insta.get_followers()

#örnek kod listeden userlar eklemek için
# list = ["kod_evreni",""]
# for user in list:
#     insta.follow_user(user)
#     time.sleep(3)

insta.follow_user("kod_evreni")

dir(Keys)




#scroll down followers window


        
            
   




    def followUser










