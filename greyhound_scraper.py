from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time

#Initialize a Firefox webdriver
driver = webdriver.Firefox(executable_path=r'C:\Users\Tony Luo\Downloads\geckodriver.exe')

#Grab the web page
driver.get("https://www.greyhound.ca/")

# You'll use selenium.webdriver.support.ui.Select
# that we imported above to grab the Seelct element called
# t_web_lookup__license_type_name, then select Acupuncturists

# We use .find_element_by_name here because we know the name
loc1 = driver.find_element_by_id("ctl00_body_search_listOrigin_Input")
loc1.send_keys("Ottawa")
# time.sleep(1)
# loc1.send_keys(Keys.ENTER)

loc2 = driver.find_element_by_id("ctl00_body_search_listDestination_Input")
loc2.send_keys("Toronto")
# time.sleep(1)
# loc2.send_keys(Keys.ENTER)

time.sleep(1)
date1 = driver.find_element_by_id("ctl00_body_search_dateDepart_dateInput")
date1.clear()
date1.send_keys("11/21/2019")

# date2 = driver.find_element_by_id("txtDateTo")
# date2.clear()
# date2.send_keys("08/22/2019")

search_button = driver.find_element_by_id("ticketsSearchSchedules")
search_button.click()

doc = BeautifulSoup(driver.page_source, "html.parser")

# price_table = doc.find("table", attrs={'id':'tableDepart'})

route = doc.find('tr',{"align" : "right"})

# schedules = []
# for route in routes:
# departure = route.find("td",class_="ptStep2departCol").text
# print(departure)
arrival = route.find("td",class_="ptStep2arriveCol").text
print(arrival)
duration = route.find("td",class_="ptStep2travelTimeCol").text
print(duration)
transfers = route.find("td",class_="ptStep2transfersCol").text
print(transfers)
webFare = route.find("label", attrs={'for':'tableDepart_r0f1'}).text
print(webFare)
advancedFare = route.find("label", attrs={'for':'tableDepart_r0f2'}).text
print(advancedFare)
standardFare = route.find("label", attrs={'for':'tableDepart_r0f3'}).text
print(standardFare)
refundableFare = route.find("label", attrs={'for':'tableDepart_r0f4'}).text
print(refundableFare)

#     schedule = {
#         'departure': departure.strip(),
#         'arrival': arrival.strip(),
#         'duration': duration.strip(),
#         'transfers' : transfers.strip(),
#         'webFare': escape.strip(),
#         'advancedFare': economy.strip(),
#         'standardFare': economyPlus.strip(),
#         'refundableFare': business.strip(),
#     }
#     schedules.append(schedule)
#
# print(schedules)
