from helium import *
from selenium import webdriver
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import xlsxwriter

#req_proxy = RequestProxy()
#proxies = req_proxy.get_proxy_list()
#proxies[0].get_address()
#PROXY = proxies[0].get_address()
#proxies[0].country

#webdriver.DesiredCapabilities.CHROME['proxy']={
#    "httpProxy":'35.223.114.70:3127',
#    "ftpProxy":'35.223.114.70:3127',
#    "sslProxy":'35.223.114.70:3127',
#    "proxyType":"MANUAL",
#}

#driver = webdriver.Chrom()



zip = "27608"
year = ["1985","1990","1995","2000"]
gender = ["Male"]
smoker = ["No"]
health = ["Preferred          (Excellent)","Preferred Plus  (Exceptional)","Regular Plus     (Above Average)","Regular             (Average)"]
term = ["5 Year Level Term","10 Year Level Term","15 Year Level Term","20 Year Level Term","25 Year Level Term","30 Year Level Term"]
coverage = ["$250,000","$500,000","$750,000","$1,000,000"]

#start_chrome("term4sale.com")
i=0
n=0
start_chrome("term4sale.com", headless=True)

for x1 in year: 
    workbook = xlsxwriter.Workbook('comps {}.xlsx'.format(x1))
    worksheet = workbook.add_worksheet()
    n=0
    for x2 in gender:
        for x3 in smoker:
            for x4 in health:
                for x5 in term:
                    for x6 in coverage:
                        i=n
                        print ("row = ",i)
                        print("chrome loaded for",x1,", ",x2,", ",x3,", ",x4,", ",x5,", ",x6)
                        write(zip, into="U.S. Zip Code")
                        select(ComboBox("1976"),x1)
                        click(x2)
                        click(x3)
                        select(ComboBox("Describe Your Health"),x4)
                        select(ComboBox("Type of Insurance"),x5)
                        select(ComboBox("Amount of Insurance"),x6)
                        click("Compare Now")
                        print("Go to page 2")
                        try:
                            wait_until(S(".text-company-name").exists,timeout_secs=5)
                        except:
                            print("no results for ",x1,", ",x2,", ",x3,", ",x4,", ",x5,", ",x6)
                        carrier_cells = find_all(S(".text-company-name"))
                        carriers = [cell.web_element.text for cell in carrier_cells]
                        for item in carriers:
                            worksheet.write(i,0,str(item))
                            i=i+1
                        #years
                        i=n
                        for item in carriers:
                            worksheet.write(i,1,x1)
                            i=i+1
                        #gender
                        i=n
                        for item in carriers:
                            worksheet.write(i,2,x2)  
                            i=i+1
                        #health
                        i=n
                        for item in carriers:
                            worksheet.write(i,3,x4) 
                            i=i+1
                        #term
                        i=n
                        for item in carriers:
                            worksheet.write(i,4,x5)
                            i=i+1
                        #coverage
                        i=n
                        for item in carriers:
                            worksheet.write(i,5,x6)
                            i=i+1
                        #smoker
                        i=n
                        for item in carriers:
                            worksheet.write(i,9,x3)
                            i=i+1

                        product_cells = find_all(S(".text-result-list"))
                        products = [cell.web_element.text for cell in product_cells]
                        i=n
                        for item in products:
                            worksheet.write(i,6,str(item))
                            i=i+1

                        price_cells = find_all(S(".text-prem"))
                        prices = [cell.web_element.text for cell in price_cells]
                        i=n
                        x=7
                        for item in prices:
                            worksheet.write(i,x,str(item))
                            if x==8:
                                i=i+1
                            if x==7:
                                x=8
                            else:
                                x=7
                        n=i
                        helium.go_to("term4sale.com")
                        #click("Modify Your Quote")
    workbook.close()
