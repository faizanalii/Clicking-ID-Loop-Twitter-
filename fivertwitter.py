from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from datetime import datetime
chromeOptions = Options() 
chromeOptions.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=r"F:\SOFTWARES\Web Drivers Automation\chromedriver.exe", options=chromeOptions)
#driver=webdriver.Chrome()
tweeter_url = "https://twitter.com/oye_chitta" 
driver.get(tweeter_url)
wait = WebDriverWait(driver, 10)
# check='Goodnight for me, good morning for you. Bye~ #rottmnt'
try:
	a=0
	start=datetime.now()
	while True:
		if a==10:
			break
		else:
			search_input = wait.until(ec.visibility_of_element_located((By.XPATH, "//div/input[@data-testid='SearchBox_Search_Input']")))
			search_input.clear() 
			search_input.send_keys("good morning #rottmnt" + Keys.ENTER)
			# driver.find_element_by_xpath('//div/a[@href="/JANny_itsmyname"]')
			# driver.findElement(By.cssSelector("a[href*='/JANny_itsmyname']")).click();
			pic_click=wait.until(ec.visibility_of_element_located((By.XPATH, "//div/a[@href='/JANny_itsmyname']")))
			# print(dir(pic_click))
			# print(pic_click.find_elements_by_link_text())
			# if pic_click.is_displayed():
			# 	print("Displayed")
			# 	test=0
			# 	while True:
			# 		tweet=wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@class='css-901oao r-jwli3a r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0']")))
			# 		# print(tweet.text)
			# 		test+=1
			# 		if test==6:
			# 			break
			# print(dir(pic_click))
			pic_click.click()
			explore=wait.until(ec.visibility_of_element_located((By.XPATH, "//nav/a[@href='/explore']")))
			explore.click()
			print("Found")
			a+=1
	print("Time Stamp is",datetime.now()-start)
	print("Count is",a)
except Exception as ex:
	print(ex)
print("Done")
