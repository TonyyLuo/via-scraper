from django.shortcuts import render

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time

def output(request):
    #Initialize a Firefox webdriver
    driver = webdriver.Firefox(executable_path=r'C:\Users\Tony Luo\Downloads\geckodriver.exe')

    #Grab the web page
    driver.get("https://reservia.viarail.ca/")

    # You'll use selenium.webdriver.support.ui.Select
    # that we imported above to grab the Seelct element called
    # t_web_lookup__license_type_name, then select Acupuncturists

    # We use .find_element_by_name here because we know the name
    loc1 = driver.find_element_by_id("cmbStationsFrom")
    loc1.send_keys("Ottawa")
    time.sleep(1)
    loc1.send_keys(Keys.ENTER)

    loc2 = driver.find_element_by_id("cmbStationsTo")
    loc2.send_keys("Toronto")
    time.sleep(1)
    loc2.send_keys(Keys.ENTER)

    date1 = driver.find_element_by_id("txtDateFrom")
    date1.clear()
    date1.send_keys("11/21/2019")

    date2 = driver.find_element_by_id("txtDateTo")
    date2.clear()
    date2.send_keys("11/22/2019")

    search_button = driver.find_element_by_id("Gtm_Retail_Search_SearchBtn")
    search_button.click()

    doc = BeautifulSoup(driver.page_source, "html.parser")

    price_table = doc.find("div", attrs={'id':'fare-matrix'})

    routes = price_table.find_all("div",class_="train-route-container")


    schedules = []
    for route in routes:
        trainNum = route.find("div",class_="left column column-train-number").text
        schedule_times = route.find_all("span",class_="schedule-info")
        departure = schedule_times[0].text
        arrival = schedule_times[1].text
        duration = route.find("div",class_="schedule-info-duration left column").text
        escape = route.find("div",class_="column column-special-fare").text
        economy = route.find("div",class_="column column-economy-fare column-economy-discounted-fare").text
        economyPlus = route.find("div",class_="column column-economy-fare column-economy-regular-fare").text
        business = route.find("div",class_="column column-business-fare column-business-discounted-fare").text
        businessPlus = route.find("div",class_="column column-business-fare column-business-regular-fare").text

        schedule = {
            'trainNum': trainNum.strip(),
            'departure': departure.strip(),
            'arrival': arrival.strip(),
            'duration': duration.strip(),
            'escape': escape.strip(),
            'economy': economy.strip(),
            'economyPlus': economyPlus.strip(),
            'business': business.strip(),
            'businessPlus': businessPlus.strip()
        }
        schedules.append(schedule)

    print(schedules)

    data = schedules
    return render(request,'home.html',{'data':data})


def button(request):
    return render(request,'home.html')
