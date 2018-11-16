def getClimate(chat_id,st):     #format climate city
    global s
    tmp = st.split()  # split string into climate and city
    City = ""
    print(tmp)
    if len(tmp)>2 and st.find("travel_info")==-1:
      for i in range(1,len(tmp)):
        if i == len(tmp)-1:
          City +=tmp[i]
        else:
          City +=tmp[i]
          City += "-"
    else:
      City = tmp[1]    # get the city name
    if City =="macau" or City == "singapore":
      City = City.lower()+"-city"
#----------------------------if input a country, show the cities which is able to search---------------------------------#
    try:
        url = "http://www.worldtravelguide.net/"+City+"/weather-climate-geography"
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        print(url)
        #發送請求
        req = ur.Request(url = url,headers=headers)
        page = ur.urlopen(req)
        contentBytes = page.read()
        #進行分割
        soup = bs(str(contentBytes), "html.parser")
        tag = soup.find("div", id="related-links")
        citylist = []
        print(tmp)
        for k in tag.select("ul li"):
            tmp = k.contents[0].contents[0].split("in ")
            try:
              citylist.append(tmp[1])
            except IndexError:
              continue
        bot.sendMessage(chat_id, "You can choose the city below:")
        for j in range(len(citylist)):
            bot.sendMessage(chat_id, citylist[j])
        bot.sendMessage(chat_id, "which one do you want to choose?")
        s = 'citycli '
#----------------------------if input is city, find city's climate info ----------------------------------------------------#      
    except  HTTPError as e:
        try:
            url = "http://www.worldtravelguide.net/"+City+"/weather"
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
            #發送請求
            req = ur.Request(url = url,headers=headers)
            page = ur.urlopen(req)
            contentBytes = page.read()
            #進行分割
            soup = bs(str(contentBytes), "html.parser")
#------------------------------------temperature data---------------------------------------------------------------#
            try:
                cityTemp = soup.find("div", id="block-block-324").find("div", class_="view-header").contents[1].contents[0]
                pictureUrl = soup.find("div", id="block-block-324").find("img").attrs['src']
                bot.sendMessage(chat_id, cityTemp)
                bot.sendPhoto(chat_id, pictureUrl)
            except AttributeError:
                bot.sendMessage(chat_id, "Sorry it don't have any temperature figures")
            
#------------------------------------sunlight data--------------------------------------------------------------------#
            try:
                citySun = soup.find("div", id="block-block-325").find("div", class_="view-header").contents[1].contents[0]
                pictureUrl = soup.find("div", id="block-block-325").find("img").attrs['src']
                bot.sendMessage(chat_id, citySun)
                bot.sendPhoto(chat_id, pictureUrl)
            except AttributeError:
                bot.sendMessage(chat_id, "Sorry it don't have any Sunlight figures")
#------------------------------------Precipitation data-----------------------------------------------------------#
            try:
                cityPre = soup.find("div", id="block-block-326").find("div", class_="view-header").contents[1].contents[0]
                pictureUrl = soup.find("div", id="block-block-326").find("img").attrs['src']
                bot.sendMessage(chat_id, cityPre)
                bot.sendPhoto(chat_id, pictureUrl)
            except AttributeError:
                bot.sendMessage(chat_id, "Sorry it don't have any precipitaion figures")
#------------------------------------Humidity data------------------------------------------------------------------#
            try:
                cityHum = soup.find("div", id="block-block-327").find("div", class_="view-header").contents[1].contents[0]
                pictureUrl = soup.find("div", id="block-block-327").find("img").attrs['src']
                bot.sendMessage(chat_id, cityHum)
                bot.sendPhoto(chat_id, pictureUrl)
            except AttributeError:
                bot.sendMessage(chat_id, "Sorry it don't have any humidity figures")
#-------------------------------cannot find anything, then inform user----------------------------------------------#            
        except HTTPError as e:
            bot.sendMessage(chat_id, "I couldn't find the city or country, please check your spelling and use 'information' to find again")

        s = "" #clean up for next request
