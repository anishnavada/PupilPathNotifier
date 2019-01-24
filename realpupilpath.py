from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

def send_simple_message(oldaverage,newaverage):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox7a7e37430d0847b7a7211fac27ed21f2.mailgun.org/messages",
        auth=("api", "key-8b84727cf598c2e14b4e3f79cbce7265"),
        data={"from": "Anish <navadaa1@bxscience.edu>",
              "to": "Anish <navadaa1@bxscience.edu>",
              "subject": "Average change!",
              "text": "Your Average has changed from a " + str(oldaverage) + " to a " + str(newaverage)})

def pupilpath(paverage):
      usr = "207473984"
      pwd = "anish321"
      driver = webdriver.Chrome()
      driver.get("https://auth.casenex.com/users/sign_in")    
      driver.find_element_by_id("usernamefield").send_keys(usr)
      driver.find_element_by_id("passwordfield").send_keys(pwd)
      driver.find_element_by_id("passwordfield").send_keys(Keys.RETURN)
      driver.find_element(By.cssSelector("a[style*='height: 215px; text-align: center; background: url(https://s3.amazonaws.com/casenex-public/authserver-2016/PupilPath-White.png) no-repeat center; background-size: 60%;']")).click();
      driver.find_element_by_id("sign_in").click()
      driver.find_element_by_id("usernamefield").send_keys(usr)
      elem = driver.find_element_by_id("passwordfield")
      elem.send_keys(pwd)
      elem.send_keys(Keys.RETURN)
      time.sleep(1)
      driver.find_element_by_id("loginSKD").click()
      soup = BeautifulSoup(driver.page_source, "html.parser")
      index = 0
      #print "Here are your classes and averages-"
      #for a in soup.find_all("tr"):
      #    if index>0:
      #            print a.getText()
      #    index = index + 1
      i= 0
      s = 0
      for a in soup.find_all(title = 'Marking Period 1 Average'):
          if i!=3:
              s = s + round(float(a.getText()[6:]))
      #        print s
          i = i + 1
      for a in soup.find_all(title = 'Marking Period 2 Average'):
          s = s + round(float(a.getText()[6:]))
      #    print s
      average = s / 6
      print "Your average is- " + str(average)
      if average != paverage:
          send_simple_message(paverage,average)
      time.sleep(600)
      pupilpath(average)       
     
             
        
    
   
           
        

pupilpath(94.8333333333)   
     
