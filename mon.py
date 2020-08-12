import sys
import os
import time
import telepot
from telepot.loop import MessageLoop
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import pyscreenshot as ImageGrab
from tokens import *

class MyBot(telepot.Bot):
	def __init__(self, *args, **kwargs):
		super(MyBot, self).__init__(*args, **kwargs)
		self.answerer = telepot.helper.Answerer(self)
		self._message_with_inline_keyboard = None
		
	def on_chat_message(self, msg):
		content_type, chat_type, chat_id = telepot.glance(msg)
		if chat_id in adminId:
			if content_type == 'text':
				if msg['text'] == '/capturegdocs':
					bot.sendChatAction(chat_id, 'typing')
					bot.sendMessage(chat_id, "Capturing image, Wait a minute")
					self.capture_gdocs()
					bot.sendPhoto(chat_id, photo=open('img\\gdoc.png', 'rb'))

		if chat_id in adminId:
			if content_type == 'text':
				if msg['text'] == '/HK':
					bot.sendChatAction(chat_id, 'typing')
					bot.sendMessage(chat_id, "Capturing image, Wait a minute")
					self.capture_housekeeping()
					bot.sendPhoto(chat_id, photo=open('img\\gdoc.png', 'rb'))
		
		else:
			bot.sendMessage(chat_id, "MAAF ANDA TIDAK MEMILIKI AKSES!!! SILAHKAN HUBUNGI DEVELOPER")
	def capture_gdocs(self):
		im = ImageGrab.grab(bbox=(50, 250, 850, 600))  # X1,Y1,X2,Y2
		workDir = os.getcwd()
		options = webdriver.ChromeOptions()
		options.add_argument('--ignore-certificate-errors')
		options.add_argument("--test-type")
		driver = webdriver.Chrome('./chromedriver')
		driver.maximize_window()
		driver.get('https://docs.google.com/spreadsheets/d/1Kgx9AAjC9gSM6LUTIIt-S7-oTAG99St-1p5VbiBxeqo/edit#gid=1974762253')
		zoomOption = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[6]/div/div/div[1]/input")
		zoomOption.click()
		time.sleep(1)
		zoomOption.send_keys("50%\n")
		time.sleep(1)
		im = ImageGrab.grab(bbox=(110, 400, 1500, 900))
		im.save('img\\gdoc.png')
		driver.quit()

	def capture_housekeeping(self):
		im = ImageGrab.grab(bbox=(50, 250, 850, 600))  # X1,Y1,X2,Y2
				
		USERNAME = '940055'
		PASSWORD = 'witeljambi'

		workDir = os.getcwd()
		options = webdriver.ChromeOptions()
		options.add_argument('--ignore-certificate-errors')
		options.add_argument("--test-type")
		driver = webdriver.Chrome('./chromedriver')
		driver.maximize_window()
		driver.get('http://10.27.30.154/HouseKeeping/index.php?page=dashboard')

		user_input = driver.find_element_by_name('user')
		user_input.send_keys(USERNAME)

		password_input = driver.find_element_by_name('pass')
		password_input.send_keys(PASSWORD)

		login_buton = driver.find_element_by_class_name('login')
		login_buton.click()
		
		zoomOption = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[6]/div/div/div[1]/input")
		zoomOption.click()
		time.sleep(1)
		zoomOption.send_keys("70%\n")
		time.sleep(1)
		im = ImageGrab.grab(bbox=(110, 400, 1500, 900))
		im.save('img\\gdoc.png')
		driver.quit()

TOKEN = telegrambot
bot = MyBot(TOKEN)
MessageLoop(bot).run_as_thread()
while 1:
	time.sleep(10)