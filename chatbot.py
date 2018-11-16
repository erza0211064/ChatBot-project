from bs4 import BeautifulSoup as bs
import urllib.request as ur
from urllib.error import HTTPError
from optparse import OptionParser
from operator import itemgetter
import sys
import time
import telepot
import random
from all_responce import responce
def handle(msg): #telebot mainfunction
    global s
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        responce(chat_id,msg)
    elif content_type == 'sticker':
        bot.sendMessage(chat_id, "Well ... I cannot choose a sticker to send to you, Sorry")
#-------------------------------send different picture to delight the user--------------------------------------------#
    elif content_type == 'photo':
        num = random.randrange(1,6)
        if num == 1:
          bot.sendPhoto(chat_id, "https://farm8.staticflickr.com/7621/16591611807_1f5172a8dd_b.jpg")
        elif num == 2:
          bot.sendPhoto(chat_id, "http://www.ld12.com/upimg358/allimg/c141127/141FO4L593Z-104B2.jpg")
        elif num == 3:
          bot.sendPhoto(chat_id,"https://www.23yy.com/upload/2015/02/22/02fcb396-6daf-4673-bafa-1b44bee213a0.jpg")
        elif num == 4:
          bot.sendPhoto(chat_id, "http://cdn2.ettoday.net/images/1382/d1382902.jpg")
        else:
          bot.sendPhoto(chat_id, "http://imgs.niusnews.com/upload/imgs/default/16OctC/1023Wildphoto/2.jpg")
    else:
        bot.sendMessage(chat_id, "What are you sending???")

#---------------put your key below~~~~--------------------------------#   
bot = telepot.Bot('key-your-token-inside-here')
bot.message_loop(handle)
print ('Listening ...')
# Keep the program running.
while 1:
    time.sleep(10)
