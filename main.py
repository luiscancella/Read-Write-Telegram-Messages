from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import bs4
import telebot
from time import sleep

#   Functions
def pressBtnDown():
    try:
        btn = WebDriverWait(browser, timeout=4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="column-center"]/div[1]/div/div[4]/div/button[1]')))
        btn.click()
    except Exception:
        pass

def getMsgs():
    return browser.find_elements(By.CSS_SELECTOR, '.bubbles-group .bubble .bubble-content-wrapper .bubble-content .message')

def htmlConverter(html_string):
    soup = BeautifulSoup(html_string, "html.parser")
    lista = []
    for tag in soup:
        if type(tag) == bs4.element.Tag:
            if tag.name == "img":
                lista.append(tag['alt'])
            elif tag.name == "span":
                pass
            elif tag.name == "a":
                lista.append(tag.string)
            elif tag.name == "div":
                continue
            else:
                raise "HTML Tag invalid | Tag: " + tag.name
        elif type(tag) == bs4.element.NavigableString:
            lista.append(tag)
        else:
            raise "Unsupported Element | Type: " + type(tag)
    return "".join(lista)

#   Bot CONFIG
with open("config.txt", "r") as f:
    config = f.readlines()
token = config[0].rstrip("\n")
id_chat_read = config[1].rstrip("\n")
id_chat_write = config[2].split(',')
bot = telebot.TeleBot(token)

#   Selenium CONFIG
sservice = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=sservice)

#   Open Telegram
browser.get(f"https://web.telegram.im/#{id_chat_read}")
WebDriverWait(browser, timeout=60).until(lambda d: d.find_element(By.TAG_NAME,"input"))
sleep(0.5)
browser.refresh()
print("Opening...")
WebDriverWait(browser, timeout=15).until(lambda d: d.find_element(By.TAG_NAME,"input"))
pressBtnDown()
sleep(2)
print("Opened!")

#   Verify Messagens
old_msg = getMsgs()
while True:
    new_msg = getMsgs()
    if len(new_msg) != len(old_msg):
        msgToSend = []
        for index, element in enumerate(new_msg, start=1):
            element = new_msg[index * -1]
            if element in old_msg:
                break
            else:
                msgToSend.append(element)
        for index, element in enumerate(msgToSend, start=1):
            element = msgToSend[index * -1]
            msg = htmlConverter(element.get_attribute('innerHTML'))
            print(msg + "\n")
            for id_chat in id_chat_write:
                bot.send_message(id_chat, msg)
        old_msg = new_msg
