from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import options
import io
import sys
from selenium.common.exceptions import NoSuchElementException
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



chrome_options = Options()
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-data-dir=C:\\Users\\gabri\\Local\Google\\Chrome\\")
options.add_argument('--profile-directory=Profile 1') #Path to your chrome profile

user_agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
options.add_argument("user-agent="+user_agent)

driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\Chrome\Application\chromedriver.exe')
tik = driver.get('https://tiktok.com')
wait = WebDriverWait(driver, 2)


time.sleep(2)
driver.maximize_window()


def main():
	for x in range(0, 6):
		driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div/div[5]/div[2]/div[2]').click()
		time.sleep(2)

		try:
			wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/main/div/div[2]/div[2]/div[2]/div[3]/div')))
		except TimeoutException:
			print('comments are disabled or there are no comments')
			driver.get('https://tiktok.com')
			main()
		try:
			wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jsx-2175848453 disable-text')))

		except:
			print('video isnt limited or has no comments, commenting.')
			pyautogui.click(1508,1006)
			pyautogui.write(comment1)
			time.sleep(2)
			driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/main/div/div[2]/div[2]/div[3]/div/div[2]').click()
			driver.back()
			time.sleep(2)
			driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button[1]').click()
			driver.get('https://tiktok.com')

def main2():
	for x in range(0, 6):
		driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div/div[5]/div[2]/div[2]').click()
		time.sleep(2)

		try:
			wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/main/div/div[2]/div[2]/div[2]/div[3]/div')))
		except TimeoutException:
			print('comments are disabled or there are no comments')
			driver.get('https://tiktok.com')
			main()
		try:
			wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jsx-2175848453 disable-text')))

		except:
			print('video isnt limited or has no comments, commenting.')
			pyautogui.click(1508,1006)
			pyautogui.write(comment2)
			time.sleep(2)
			driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/main/div/div[2]/div[2]/div[3]/div/div[2]').click()
			driver.back()
			time.sleep(2)
			driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button[1]').click()
			driver.get('https://tiktok.com')


def main49

def main3():
	for x in range(0, 6):
		driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div/div[5]/div[2]/div[2]').click()
		time.sleep(2)

		try:
			wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/main/div/div[2]/div[2]/div[2]/div[3]/div')))
		except TimeoutException:
			print('comments are disabled or there are no comments')
			driver.get('https://tiktok.com')
			main()
		try:
			wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jsx-2175848453 disable-text')))

		except:
			print('video isnt limited or has no comments, commenting.')
			pyautogui.click(1508,1006)
			pyautogui.write(comment3)
			time.sleep(2)
			driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/main/div/div[2]/div[2]/div[3]/div/div[2]').click()
			driver.back()
			time.sleep(2)
			driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button[1]').click()
			driver.get('https://tiktok.com')


print('do not enter duplicate comments or you will be limited to comment.')
print('bot will not comment on a video with no comments to avoid looking spammyx')
comment1 = input('Comment 1: ')
comment2 = input('Comment 2: ')
comment3 = input('Comment 3: ')

body = driver.find_element_by_tag_name('body')

if body.is_displayed():
	main()

else:
	print('error loading page')
