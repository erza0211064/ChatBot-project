def getWeather(chat_id,s):  #format: weather country city
    tmp = s.split()
#-----------------------------------------check if the format is correct-----------------------------------------------#
    if len(tmp)<3:
      bot.sendMessage(chat_id, "Sorry you lost some information, try again!")
      bot.sendMessage(chat_id, "format is: weather country city")
      return
    elif len(tmp)>3:
      bot.sendMessage(chat_id, "Sorry, too much information, try again!")
      bot.sendMessage(chat_id, "format is: weather country city")
      return
    weatherInfo = []    #store weather type and Max temperature
    POP = []            #store rain probility of percentage (POP)
    MinTemp = []        #store Min temperature(the data in html puts in different place)
    TodayCount = 0      #calculate the probility of percentage
    TomorrCount = 0     #calculate the probility of percentage
#---------------------------------------get weather info from website----------------------------------------------------#
    url = "https://www.worldweatheronline.com/country.aspx"
    countryInput = tmp[1].capitalize()
    cityInput = tmp[2].capitalize()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = ur.Request(url = url,headers=headers)
    page = ur.urlopen(req)
    contentBytes = page.read()
    soup = bs(str(contentBytes), "html.parser")
#----------------------------get all country data and check which one is same as user's input-------------------------------#
    for k in soup.select(".listofcountries li "):
        if countryInput ==k.contents[1].contents[0]:
            urlCountry = str(k.contents[1]["href"])
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}        
            req = ur.Request(url = urlCountry,headers=headers)
            page = ur.urlopen(req)
            contentBytes = page.read()
            soup = bs(str(contentBytes), "html.parser")
            tag1 = soup.find("div",class_="countrylistdiv")
#-------------------------get the cities data according to the country and look for the city user input
            for j in tag1.select("ul li"):
                if cityInput == j.contents[0].contents[0]:
                    urlCity = str(j.contents[0].attrs["href"])+"?day=0"
                    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}        
                    req = ur.Request(url = urlCity,headers=headers)
                    page = ur.urlopen(req)
                    contentBytes = page.read()
                    soup = bs(str(contentBytes), "html.parser")
                    #tag2 = soup.find("div", class_="tab-content")
                    
                    
                    for l in soup.select(".forecast-block p"):
                        weatherInfo.append(l.contents[0])
                    for i in soup.select(".forecast-block p span"):
                        MinTemp.append(i.contents[0])
                    for h in soup.select(".table-responsive tbody tr"):
                        if h.contents[0].contents[0] == "Rain?":
                            for g in h.select("td"):
                                POP.append(g.contents[0])
                    i = 0
#-------------------------raw data gives 8 probility of percentage so here do the average------------------------------------------------#
                    for i in range(int(len(POP)/2)):
                        POP[i] = POP[i].split("%")[0]
                        POP[i+8] = POP[i+8].split("%")[0]
                        TodayCount+=int(POP[i])
                        TomorrCount+=int(POP[i+8])
                    TodayCount/=8
                    TomorrCount/=8
                    MinTemp[0] = MinTemp[0].split("| ")[1]
                    MinTemp[0] = MinTemp[1].split("| ")[1]
                    res = "Today:                                               "+"   weather type: "+weatherInfo[0]+"                        Max temp: "+weatherInfo[1].split(": ")[1]+"                                 Min temp: "+str(MinTemp[0].split(": ")[1])+"                                         probility of percentage:"+str(TodayCount)+"%"
                    bot.sendMessage(chat_id, res)
                    res = "Tomorrow:                                            "+"weather type: "+weatherInfo[5]+"                           Max temp: "+weatherInfo[6].split(": ")[1]+"                                 Min temp: "+str(MinTemp[1].split(": ")[1])+"                                          probility of percentage:"+str(TomorrCount)+"%"
                    bot.sendMessage(chat_id, res)
                    return 
            break
#-----------------------------------if cannot find anything, inform the user---------------------------------------------------------------#
    bot.sendMessage(chat_id, "Sorry I can't find, maybe check your spelling!!")
    bot.sendMessage(chat_id, "format is: weather country city")
    return
