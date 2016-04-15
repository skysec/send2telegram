#!/usr/bin/env python
#
# telegram send message: send a text message to a chat_id
#

import telegram
import sys, getopt

def main(argv):
    bot_token = '<bot_token>'
    """ default chat id """
    send2chat = '<default chat id>'
    message= ''
    try:
	opts, args = getopt.getopt(argv,"hc:m:",["chatid=","msg="])
    except getopt.GetoptError:
	print 'telegram_send.py -c <chat_id> -m <message>'
	sys.exit(2)
    for opt, arg in opts:
	if opt == '-h':
	    print 'telegram_send.py -c <chat_id> -m <message>'
	    sys.exit()
	elif opt in ("-c","--chatid"):
	    send2chat = arg
	elif opt in ("-m","--msg"):
	    message = arg
    if message == '':
	print 'telegram_send.py -c <chat_id> -m <message>'
	print '-m | --msg is required'
	sys.exit(2)
    """ Create Bot """
    bot = telegram.Bot(token=bot_token)
    bot.sendMessage(chat_id=send2chat, text=message)

if __name__ == "__main__":
    main(sys.argv[1:])	
