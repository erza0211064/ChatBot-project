def getHotelInfo(chat_id,s):   #format  hotel city checkin(e.g 2017-05-02) checkout 
    tmp = s.split()
    if len(tmp) < 5:
        bot.sendMessage(chat_id, "Sorry you lost some infomation. Or maybe you lost some space")
        bot.sendMessage(chat_id, "format is: hotel city checkin(e.g 2017-05-02) checkout(e.g.2017-05-03) price(rate)")
        return 
    elif len(tmp) > 5:
        bot.sendMessage(chat_id, "Sorry, too many infomation.")
        bot.sendMessage(chat_id, "format is: hotel city checkin(e.g 2017-05-02) checkout(e.g.2017-05-03) price(rate)")
        return
    CheckIn = tmp[2]
    CheckOut = tmp[3]
    if checkDate(chat_id,CheckIn,CheckOut) == True:
        return
#-------------------------------------read city data to get the URL------------------------------------------
    City = tmp[1]  
    f = open('city.txt','r', encoding = 'UTF-8')
    while True:
      string = f.readline().split()
      if City == string[0]:
        break
  
    f.close()
    CityNum = string[1]
#-------------------------------------read data form website----------------------------------------------------
    url = "https://www.agoda.com/zh-hk/pages/agoda/default/DestinationSearchResult.aspx?asq=u2qcKLxwzRU5NDuxJ0kOF8dmq7Ztgl2%2FfOEj7KAaspCTIbIpW83e1VFmJssp8bOXt54U2I0bQo%2Bgyn7ax3pfm8%2FHyb%2FWqadFiNS4Hk47%2FsKcGB4nTz%2F09FE%2FaJUjlfm5Co2qpZTXDnSzTz9ioXCxv%2BVU3tmaBdeCE2fSz7zkZEvjV5DKzeC%2FBkkLC3zOAuhD4vdy1KJtyI4jLLB6u%2BPlIBpaLA8WrczZYJ5naKggSn8%3D&city="+CityNum+"&recommendedIndex=1&pageType=1&panel=searchboxrecommended&pagetypeid=1&origin=SG&cid=-1&tag=&gclid=&aid=130243&userId=d1a8100f-5faa-413b-aeb6-cd56ab30fcf7&languageId=7&sessionId=ia4q5lj3hb1d0nlyp1xyrojm&storefrontId=3&currencyCode=SGD&htmlLanguage=zh-hk&trafficType=User&cultureInfoName=zh-HK&checkIn="+CheckIn+"&checkOut="+CheckOut+"&los=4&rooms=1&adults=2&children=0&priceCur=SGD&hotelReviewScore=5&ckuid=d1a8100f-5faa-413b-aeb6-cd56ab30fcf7"    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    #發送請求
    req = ur.Request(url = url,headers=headers)
    page = ur.urlopen(req)
    contentBytes = page.read()
    #進行分割
    soup = bs(str(contentBytes), "html.parser")
    #將資訊顯示出來
    #f = open('A.txt', 'w', encoding = 'UTF-8')
    #f.write(soup.prettify())
    #f.close()
    ratelist = []       # store rate
    pricelist = []      # store price
    hotellist = []      # store hotel name
    byPriceDict = {}    # dict to sort by price
    byRateDict = {}     # dict to sort by rate
    alllist = []        # after sorting store it here
#-----------------------------------read the price--------------------------------------------------
    for k in soup.select(".price-container "):
        inputToList = k.contents[3].contents[0]
        pricelist.append(inputToList)
#-----------------------------------read the name of hotel------------------------------------------
    for l in soup.select(".hotel-info h3"):
        hotelNameRaw = l.contents[0]
        try:
            hotelName = hotelNameRaw.split("(")[1].split(")")[0]
        except IndexError:
            hotelName = hotelNameRaw.strip(" \\rn").strip()
        hotellist.append(hotelName)
#-----------------------------------read the rate--------------------------------------------------
    for m in soup.select(".review-score "):
        inputToList = m.contents[0]
        ratelist.append(inputToList)
    if tmp[4] == "price":
#-----------------------sort by price------------------------------
      for j in range(len(pricelist)):
          tmp = hotellist[j]+" Rate:"+ratelist[j]
          byPriceDict['hotel'] = tmp
          byPriceDict['price'] = pricelist[j]
          alllist.append(byPriceDict)
          byPriceDict = {}
      alllist = sorted(alllist, key=itemgetter("price"))   # sort by price
      for index in range(len(alllist)):
        res = alllist[index]["price"]+" SGD"
        bot.sendMessage(chat_id, alllist[index]["hotel"])
        bot.sendMessage(chat_id, res)
        if index == 10:
          break
      alllist = []
      index = 0
#-----------------------sort by rate------------------------------
    else:
      for i in range(len(ratelist)):
          tmp = hotellist[i]+" /"+str(pricelist[i])
          byRateDict["hotel"] = tmp
          byRateDict["rate"] =  float(ratelist[i])
          alllist.append(byRateDict)
          byRateDict = {}
      alllist = sorted(alllist, key=itemgetter("rate"), reverse = True)  # store by rate and order from high to low
      for index in range(len(alllist)):
        temp = alllist[index]["hotel"].split("/")
        res1 = temp[0]+" Rate:"+str(alllist[index]["rate"])
        res2 = temp[1]+" SGD"
        bot.sendMessage(chat_id, res1)
        bot.sendMessage(chat_id, res2)
        if index ==  9:   # print less then 10 hotel information
          break
