import requests 
from bs4 import BeautifulSoup 
from urllib.request import urlopen 
import pandas as pd
import tabulate
import time
import os


class stock_monitor:
    def stock_info(self,name):
            try:
                  
                  apple_url = f"https://finance.yahoo.com/quote/{name}"
                  html_text = requests.get(url=apple_url).text 
                  soup = BeautifulSoup(html_text, "lxml")
                  stock_name = soup.find("h1", class_= "svelte-3a2v0c" ).text
                  stock_info = []
                  # print(f"stock_name: {stock_name}") 
                  stock_price = soup.find("fin-streamer", class_ = "livePrice svelte-mgkamr").find("span").text
                # print(f"stock price: {stock_price}")  
                  stock_time = soup.find("div", slot = "marketTimeNotice").find("span").text
                # print(f"stock_time: {stock_time}") 
                  stock_info.append([stock_name,stock_price,stock_time])
                  info_pd = pd.DataFrame(stock_info,columns=["stock_name","stock_price(in USD)","stock_time"])
                  tabulated_pd = tabulate.tabulate(info_pd, headers='keys', tablefmt='pretty')
                  print(tabulated_pd) 
            except Exception as ex:
                  print("Enter the company's stock name correctly")
                
                  
    


if __name__ == "__main__":
        
        while True:
            user = stock_monitor()
            nme = input("Enter company's stock to know it's stock: ")
            user.stock_info(name=nme)
            ttl = 1 
            print(f"This will again load in {ttl} minute") 
            time.sleep(ttl*60)
        

            
                
          

          

            



                  
                
            
          
         
        

    