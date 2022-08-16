import requests
from bs4 import BeautifulSoup

from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt




# def home(request):
#     url = "https://www.imdb.com/chart/moviemeter/"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     table = soup.find('table',  {'class': 'chart full-width'})
#     rows = table.find_all('tr')
#     movies = []
#     for row in rows:
#         image = row.find('img')
#         if image:
#             movies.append(image['alt'])
#     return render(request, "movies/home.html", {'movies': movies})

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import re
import csv
import array as arr 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW




service = Service('C:\work\git\scrape-linkedin-selenium/chromedriver.exe')
service.creationflags = CREATE_NO_WINDOW




def home(request):
    # data = ['','','','']
    # header = ['Company','Person Name', 'Email', 'Phone']
    # with open('personData.csv', 'w', encoding='UTF8') as f:
    #  writer = csv.writer(f)
    # # write the header
    #  writer.writerow(header)
    
    #     # declare variable to store the URL to be visited
    # base_url="https://www.google.com/"
    # # declare variable to store search term
    # search_term="site:www.linkedin.com/in/ AND \"chewy\" \"profile\" \"phone\" \"gmail\""
    # # -- Pre - Condition --
    # # declare and initialize driver variable
    # #driver=webdriver.Chrome(executable_path="C:\work\git\scrape-linkedin-selenium/chromedriver.exe")
    # options = webdriver.ChromeOptions()
    # #options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")
    # options.add_argument("--disable-extensions")

    # driver = webdriver.Chrome(chrome_options=options,service=service)
    # #driver = webdriver.Chrome(chrome_options=options,executable_path="C:\work\git\scrape-linkedin-selenium/chromedriver.exe")

    # # browser should be loaded in maximized window
    # driver.maximize_window()
    # # driver should wait implicitly for a given duration, for the element under consideration to load.
    # # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
    # driver.implicitly_wait(10) #10 is in seconds
    # # to load a given URL in browser window

    # driver.get(base_url)
    # time.sleep(2)
    # searchTextBox=driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    # searchTextBox.clear()
    # # to enter the search term in the search textbox via send_keys() function
    # searchTextBox.send_keys(search_term)
    # # to search for the entered search term
    # searchTextBox.send_keys(Keys.RETURN)
    # movies = []
    # for i in range(10):
    #     try:
    #         searchTitle = driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(i+1)+"]/div/div/div[1]/div/a/h3").text.replace("- LinkedIn","").replace("LinkedIn","")
    #         searchContent=driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(i+1)+"]/div/div/div[2]").text.replace("LinkedIn","")
    #         # extracting the gmail
    #         searchGmail = re.findall('\S+@\S+', searchContent)  
    #         # extracting the mobile number
            
    #         m=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', searchContent)
            
    #         print(str(i)+".Name:"+searchTitle)
    #         #print(str(i)+".Detail:"+ searchContent)
    #         print(str(i)+".Email:"+ str(searchGmail))
    #         print(str(i)+".Phone:"+ str(m))
    #         # write the data
    #         data[0]="chewy"
    #         data[1]=searchTitle
    #         data[2]=searchGmail
    #         data[3]=m
    #         movies.append(str(i)+":"+searchTitle+"|Email:"+str(searchGmail)+"|Phone:"+str(m))
    #         with open('personData.csv', 'a', encoding='UTF8') as f:
    #              writer = csv.writer(f)
            
    #              writer.writerow(data)
    #     except NoSuchElementException:        
    #         print("Oops! no more result #########################################################")
    #         break
    
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # driver.find_element(By.XPATH, "//*[@id=\"botstuff\"]/div/div[3]/table/tbody/tr/td[3]/a").click()
    # print("Click next page")
    # for i_p in range (6):
    #     for i in range(10):
    #         try:
    #             searchTitle = driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(i+1)+"]/div/div/div[1]/div/a/h3").text.replace("- LinkedIn","").replace("LinkedIn","")
    #             searchContent=driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(i+1)+"]/div/div/div[2]").text.replace("LinkedIn","")       
    #             searchGmail = re.findall('\S+@\S+', searchContent)     
    #             # extracting the mobile number
    #             m=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', searchContent)
    #             print(str(8*i_p+i)+".Name:"+searchTitle)
    #             #print(str(8*i_p+i)+".Detail:"+ searchContent)
    #             print(str(8*i_p+i)+".Email:"+ str(searchGmail))
    #             print(str(8*i_p+i)+".Phone:"+ str(m))
    #             # write the data
    #             data[0]="chewy"
    #             data[1]=searchTitle
    #             data[2]=searchGmail
    #             data[3]=m
    #             movies.append(str(8*i_p+i)+":"+searchTitle+"|Email:"+str(searchGmail)+"|Phone:"+str(m))
    #             with open('personData.csv', 'a', encoding='UTF8') as f:
    #                 writer = csv.writer(f)
                    
    #                 writer.writerow(data)
    #         except NoSuchElementException:        
    #             print("Oops! no more result #########################################################")
    #             break
            

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.find_element(By.XPATH, "//*[@id=\"botstuff\"]/div/div[3]/table/tbody/tr/td["+str(i_p+4)+"]/a").click()

    # # -- Post - Condition --
    # # to close the browser
    # driver.close()
    movies = []
    return render(request, "movies/home.html", {'movies': movies})
@csrf_exempt 
def sreach_view(request):
       
    if request.method == "POST":
        movies = ['']
        pagenum = 0
        
        searchWord = request.POST.get('search','')
        print("you enter keyword:"+searchWord)
        if len(searchWord)>0:
            data = ['','','','']
            header = ['Company','Person Name', 'Email', 'Phone']
            with open('personData.csv', 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                # write the header
                writer.writerow(header)
            
                # declare variable to store the URL to be visited
            base_url="https://www.google.com/"
            # declare variable to store search term
            search_term="site:www.linkedin.com/in/ AND \""+searchWord+"\" \"profile\" \"phone\" \"gmail\""
            
            #search_term="site:twitter.com -site:m.twitter.com intitle:”on Twitter” "+searchWord+"  gmail"
            
            # -- Pre - Condition --
            # declare and initialize driver variable
            #driver=webdriver.Chrome(executable_path="C:\work\git\scrape-linkedin-selenium/chromedriver.exe")
            options = webdriver.ChromeOptions()
            #options.add_argument('headless')
            options.add_argument('window-size=1920x1080')
            options.add_argument("disable-gpu")
            options.add_argument("--disable-extensions")

            driver = webdriver.Chrome(chrome_options=options,service=service)
            #driver = webdriver.Chrome(chrome_options=options,executable_path="C:\work\git\scrape-linkedin-selenium/chromedriver.exe")

            # browser should be loaded in maximized window
            driver.maximize_window()
            # driver should wait implicitly for a given duration, for the element under consideration to load.
            # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
            driver.implicitly_wait(10) #10 is in seconds
            # to load a given URL in browser window

            driver.get(base_url)
            time.sleep(2)
            searchTextBox=driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
            searchTextBox.clear()
            # to enter the search term in the search textbox via send_keys() function
            searchTextBox.send_keys(search_term)
            # to search for the entered search term
            searchTextBox.send_keys(Keys.RETURN)
            movies = []
            
            for i in range(10):
                try:
                    searchTitle = driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(i+1)+"]/div/div/div[1]/div/a/h3").text.replace("- LinkedIn","").replace("LinkedIn","")
                    searchContent=driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(i+1)+"]/div/div/div[2]").text.replace("LinkedIn","")
                    # extracting the gmail
                    searchGmail = re.findall('\S+@\S+', searchContent)  
                    # extracting the mobile number
                    
                    m=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', searchContent)
                    
                    print(str(i)+".Name:"+searchTitle)
                    #print(str(i)+".Detail:"+ searchContent)
                    print(str(i)+".Email:"+ str(searchGmail))
                    print(str(i)+".Phone:"+ str(m))
                    # write the data
                    data[0]=searchWord
                    data[1]=searchTitle
                    data[2]=searchGmail
                    data[3]=m
                    movies.append(str(i)+":"+searchWord+"-"+searchTitle+"|Email:"+str(searchGmail)+"|Phone:"+str(m))
                    with open(searchWord+'_personData.csv', 'a', encoding='UTF8') as f:
                        writer = csv.writer(f)
                    
                        writer.writerow(data)
                except NoSuchElementException:        
                    print("Oops! first page no more result #########################################################")
                    
                    break
            
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                 driver.find_element(By.XPATH, "//*[@id=\"botstuff\"]/div/div[3]/table/tbody/tr/td[3]/a").click()
                except NoSuchElementException:        
                 print("Oops! first page no more click #########################################################")
                 #pagenum=0
                 if len(movies)==0:
                        movies = ['No data found']
                 break
             
            # if pagenum>0:
                print("Click next page")
            for i_p in range (4):
                    
                    for i in range(10):
                        try:
                            searchTitle = driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(i+1)+"]/div/div/div[1]/div/a/h3").text.replace("- LinkedIn","").replace("LinkedIn","")
                            searchContent=driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(i+1)+"]/div/div/div[2]").text.replace("LinkedIn","")       
                            searchGmail = re.findall('\S+@\S+', searchContent)     
                            # extracting the mobile number
                            m=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', searchContent)
                            print(str(8*i_p+i)+".Name:"+searchTitle)
                            #print(str(8*i_p+i)+".Detail:"+ searchContent)
                            print(str(8*i_p+i)+".Email:"+ str(searchGmail))
                            print(str(8*i_p+i)+".Phone:"+ str(m))
                            # write the data
                            data[0]=searchWord
                            data[1]=searchTitle
                            data[2]=searchGmail
                            data[3]=m
                            movies.append(str(8*i_p+i)+":"+searchWord+"-"+searchTitle+"|Email:"+str(searchGmail)+"|Phone:"+str(m))
                            with open(searchWord+'_personData.csv', 'a', encoding='UTF8') as f:
                                writer = csv.writer(f)
                                
                                writer.writerow(data)
                        except NoSuchElementException:        
                            print("Oops! no more result #########################################################")
                            break
                        
                    try:
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        driver.find_element(By.XPATH, "//*[@id=\"botstuff\"]/div/div[3]/table/tbody/tr/td["+str(i_p+4)+"]/a").click()
                    except NoSuchElementException:        
                     print("Oops! no more click #########################################################")
                    
                     break
                    
           

            # -- Post - Condition --
            # to close the browser
            driver.close()
        #movies = ['123']
        
            print(movies)
        else:
         movies = ['']
       
    return render(request, "movies/home.html", {'movies': movies })