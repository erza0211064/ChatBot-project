def responce(chat_id,msg):
    """do sth depends on the text"""
    global s
    s += msg['text']
    s=s.lower()
    print(s)
    
    #----------------------Just for Greeting-----------------------------#
    if s.find('hello')!= -1 or s.find('hi')!= -1 and s.find("change")==-1 and s.find("travel_info")==-1 and s.find("hotel")==-1 and s.find("weather")==-1 and s.find("ho chi minh city")==-1:
        bot.sendMessage(chat_id, """Hello, I'm TravelTravel.

I can help you :
(1)find good hotels(insert"hotel")
(2)check the weather (insert"weather")
(3)calculate money change(insert"money")
(4)Get travel information(insert"information")

How can I help you?""")
        s=""

    elif s.find('bye')!=-1:
        num = random.randrange(1,3)
        if num == 1:
          bot.sendMessage(chat_id,'Bye~Have a nice trip!')
        else:
          bot.sendMessage(chat_id,"See you soon, and please rate us with five stars")
        s=''

    elif s.find('thank')!=-1:
        bot.sendMessage(chat_id,'>///<Not to say lah~')
        s=''

        
    #---------------------Help change money-----------------------------#
    elif s.find('money')!= -1 : #User search for moneychanging
        bot.sendMessage(chat_id,"""What money and amount do you want to change into?
e.g. SGD 100, TWD 5000
【NOTE】seperate the money and amount by SPACE!!""")
        s='change '#to identify user is in moneychanging
        
    elif s.find('change')!=-1 and s.find('from')==-1:
        if len(s.split())!=3:
          bot.sendMessage(chat_id,"Your format is wrong, try again!!")
          bot.sendMessage(chat_id,"e.g. SGD 100, TWD 5000")
          bot.sendMessage(chat_id,"【NOTE】seperate the money and amount by SPACE!!")
          s = ""
          return
        bot.sendMessage(chat_id,"""What money do you use to change?
e.g. SGD, TWD""")
        s +=' from ' #to identify user has input money and amount they need

    elif s.find('change')!=-1 and s.find('from')!=-1:
        moneychanger(chat_id,s)
        s='' #clean the string to read next action
        
    #-------------------Get Travel Information--------------------------#
    elif s.find('information')!= -1 : #User search for travel info
        bot.sendMessage(chat_id,'What country are you searching?')
        s='travel_info ' #to identify user is in info

    elif s.find('travel_info')!=-1 and s.find('with')==-1:
        bot.sendMessage(chat_id,"""What kind of information you need?
(basic/to_do/climate)""")
        s +=' with ' #to identify user has input info type

    elif s.find('travel_info')!=-1 and s.find('with')!=-1:
        if s.find('basic')!=-1:
          basic_info(chat_id,s)
          s='' #clean the string to read next request
          bot.sendMessage(chat_id, "type 'help' to know what I can help!!")
        elif s.find('to_do')!=-1:
          to_do(chat_id,s)
          s='' #clean the string to read next request
          bot.sendMessage(chat_id, "type 'help' to know what I can help!!")
        elif s.find("climate")!=-1:
          getClimate(chat_id,s)
        else:
          bot.sendMessage(chat_id, """this is not basic, to_do or climate@ @
please check your spelling, and insert "information" to start again.""")
          return
    elif s.find('citycli')!= -1 : #User search for travel info
        getClimate(chat_id,s)
        s='' #to identify user is in info
        bot.sendMessage(chat_id, "type 'help' to know what I can help!!")

    #--------------------Get weather information----------------------------#
    elif s.find("weather")!=-1:
      if len(s)<8:
        bot.sendMessage(chat_id,'What country and city do you want to find?')
        bot.sendMessage(chat_id, "format is: weather country city")
      else:
        getWeather(chat_id,s)
        bot.sendMessage(chat_id, "type 'help' to know what I can help!!")
      s=""
      
    #--------------------Get hotel information----------------------------#
    elif s.find("hotel")!=-1:
        if len(s)<6:
          bot.sendMessage(chat_id,'Where and when do you want to find?')
          bot.sendMessage(chat_id, "format is: hotel city checkin(e.g 2017-05-02) checkout(e.g.2017-05-03) price(or rate)")
          bot.sendMessage(chat_id, "put 'price' will show low price to high price")
          bot.sendMessage(chat_id, "put 'rate' will show high rate to low rate")
          s = ""
          return 
        getHotelInfo(chat_id,s)
        s = ""
        bot.sendMessage(chat_id, "type 'help' to know what I can help!!")
    elif s.find("help")!=-1:
      num = random.randrange(1,4)
      if num == 1:
        bot.sendMessage(chat_id,'You really need help????')
        bot.sendMessage(chat_id,'Maybe call 999 for police or 995 for ambulance is faster la!!!')
        s = ""
      else:
        bot.sendMessage(chat_id, """

I can help you :
(1)find good hotels(insert"hotel")
(2)check the weather (insert"weathers")
(3)calculate money change(insert"money")
(4)Get travel information(insert"information")

How can I help you?""")
        s = ""
        
  
    

    

    

    #-----------------------Nothing can do-------------------------------#
    else:
        bot.sendMessage(chat_id,"Sorry, I don't understand what you said. T_T")
