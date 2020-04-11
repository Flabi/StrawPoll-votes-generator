import WebR #A script I made able to handle POST/GET requests
import DataManager #A script I made able to load and manage date from files
import time

HeadersRequest1={
'Host': 'strawpoll.com', 
'Connection': 'keep-alive', 
'Upgrade-Insecure-Requests': '1', 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36', 
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
'Sec-Fetch-Site': 'none', 
'Sec-Fetch-Mode': 'navigate', 
'Accept-Encoding': 'gzip, deflate, br', 
'Accept-Language': 'en-US,en;q=0.9', 
}

HeadersRequest2={
'Host': 'api2.strawpoll.com', 
'Connection': 'keep-alive', 
'Accept': 'application/json, text/plain, */*', 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36', 
'Content-Type': 'application/json;charset=UTF-8', 
'Origin': 'https://strawpoll.com', 
'Sec-Fetch-Site': 'same-site', 
'Sec-Fetch-Mode': 'cors', 
'Accept-Encoding': 'gzip, deflate, br', 
'Accept-Language': 'en-US,en;q=0.9', 
}


DataManager.load_data() #Load proxies
URL = str(input("Enter poll URL: "))   #Example "https://strawpoll.com/366ggz3"
CHECK = str(input("Enter checkbox ID: ")) #Example "4855207"
NR_VOT = int(input("How many votes, boss?: "))  #Example 10
POLL_HASH=URL.split("/")[3]

for i in range(0,NR_VOT):
    print("ADDING VOTE #" + str(i+1) + "...")
    w=WebR.WebR()
    w.set_proxy(DataManager.get_proxy())
    src1=w.GET("https://strawpoll.com/366ggz3", HeadersRequest1)
    time.sleep(1)
    src2=w.POST("https://api2.strawpoll.com/pollvote", '{"poll_hash":"' + str(POLL_HASH) + '","checked_answers":' + str(CHECK) + ',"name":null}', HeadersRequest2)
    if (src2.find("Thanks for your vot")>-1):
        print("Vote #" + str(i+1) + " ADDED!")
    else:
        print("Vote #" + str(i+1) + " FAILED to be added!" + src2)

