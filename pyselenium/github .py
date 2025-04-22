from githubUserInfo import username, password
from selenium import webdriver
import time

class GitHub:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username =  username
        self.password = password 
        self.following = []
        
        
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        
        username =  self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        password = self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        
        time.sleep(1)
        
        self.browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[13]').click()
        
    
    def get_following(self):
          self.browser.get(f"https://github.com/toygarpar?tab=following")
          time.sleep(2)
          
          
          
          items =self.browser.find_elements_by_id("user-profile-frame")
          #items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
          
          for i in items:
              self.following.append(i.find_element_by_css_selector(".f4.Link--primary").text)
          
          
          
          
github = GitHub(username, password)
github.signIn()   
#github.get_following()
github.get_following()
print(github.following)     
        
     
        
     
        
     
        
     
        
     
        
#sadıkturantoygarpar followersları için        

from githubUserInfo import username, password
from selenium import webdriver
import time


class GitHub:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username =  username
        self.password = password 
        self.followers = []
        
        
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        
        username =  self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        password = self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        
        time.sleep(1)
        
        self.browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[13]').click()
        
    def load_followers(self):
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        
        for i in items:
            self.followers.append(i.find_element_by_css_selector(".f4.Link--primary").text)
        
    def get_followers(self):
                    
          self.browser.get(f"https://github.com/toygarpar?tab=followers")
          time.sleep(2)
          
          #items =self.browser.find_elements_by_id("user-profile-frame")  #bunun ile tek follower alıyor
          self.load_followers()
          
          while True:
              
              links = self.browser.find_element_by_class_name("paginate-container").find_elements_by_tag_name("a")
             
              
              if len(links) == 1:
                  if links[0].text == "Next":
                      links[0].click()
                      time.sleep(2)
                      
                      self.load_followers()
                  else:
                      break
                       
                                       
                          
                    
              
                
              else:
                  for link in links:
                      time.sleep(3)
                      if link.text == "Next":
                          link.click()
                          time.sleep(2)
                          
                          self.load_followers()
                              
                      else:
                          continue
                      
                      
          
          
github = GitHub(username, password)
github.signIn()   
#github.get_following()
github.get_followers()
print(len(github.followers))
print(github.followers)             







        
     
        
     
"""
<div class="d-table table-fixed col-12 width-full py-4 border-bottom color-border-muted">
    <div class="d-table-cell col-2 col-lg-1 v-align-top">
      <a class="d-inline-block" data-hovercard-type="user" data-hovercard-url="/users/mvahit/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/mvahit"><img class="avatar avatar-user" src="https://avatars.githubusercontent.com/u/13828606?s=100&amp;v=4" width="50" height="50" alt="@mvahit"></a>
    </div>

    <div class="d-table-cell col-9 v-align-top pr-3">
      <a class="d-inline-block no-underline mb-1" data-hovercard-type="user" data-hovercard-url="/users/mvahit/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/mvahit">
        <span class="f4 Link--primary">Vahit Keskin</span>
        <span class="Link--secondary pl-1">mvahit</span>
</a>

        <div class="color-fg-muted text-small mb-2">
          <div>Lead Data Scientist | AI &amp; Data Science Consultant</div>
        </div>

        <p class="color-fg-muted text-small mb-0">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-location">
    <path d="m12.596 11.596-3.535 3.536a1.5 1.5 0 0 1-2.122 0l-3.535-3.536a6.5 6.5 0 1 1 9.192-9.193 6.5 6.5 0 0 1 0 9.193Zm-1.06-8.132v-.001a5 5 0 1 0-7.072 7.072L8 14.07l3.536-3.534a5 5 0 0 0 0-7.072ZM8 9a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 9Z"></path>
</svg> Sweden
        </p>
    </div>

    <div class="d-table-cell col-2 v-align-top text-right">
      
  <span class="user-following-container js-form-toggle-container">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-form-toggle-target" hidden="hidden" data-sr-feedback="You are following mvahit" data-turbo="false" action="/users/follow?target=mvahit" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="VTaZKQfUCjuwHxTzZ7Gqs0Jv0vFteLGwwSL0s7aVG1d_ROq99E9x1Ag_Ova_TOPcFyZRRp2Al7wzOIvbZ9hfDg">
        <input type="submit" name="commit" value="Follow" class="btn btn-sm" title="Follow mvahit" aria-label="Follow mvahit" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:121767033,&quot;target&quot;:&quot;FOLLOW_BUTTON&quot;,&quot;user_id&quot;:121767033,&quot;originating_url&quot;:&quot;https://github.com/toygarpar?tab=following&quot;}}" data-hydro-click-hmac="a90f5b79ab2ca3fab2e6069fd3430878d55667c7a99d1882661a873192a3eda0" data-disable-with="Follow">
</form>
    <!-- '"` --><!-- </textarea></xmp> --><form class="js-form-toggle-target" data-sr-feedback="You are unfollowing mvahit" data-turbo="false" action="/users/unfollow?target=mvahit" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="y2LOecCnQJHNTt0Oo2kwlM59DQzn4JDUqeKO5L5CjdJQq0pXlNpvP8u3QuspssuikckxlqvyDmvHgp-RMyvXGQ">
      <input type="submit" name="commit" value="Unfollow" class="btn btn-sm" data-disable-with="Unfollow" title="Unfollow mvahit" aria-label="Unfollow mvahit">
</form>  </span>

    </div>
  </div>        
"""     
