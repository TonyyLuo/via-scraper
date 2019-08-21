from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time

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
date1.send_keys("08/21/2019")

date2 = driver.find_element_by_id("txtDateTo")
date2.clear()
date2.send_keys("08/22/2019")

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


# for route in routes:
#
#     num = route.find("div",class_="left column column-train-number").text
#     print(num)
#
#     schedule = route.find_all("span",class_="schedule-info")
#     departure = schedule[0].text
#     arrival = schedule[1].text
#     print(departure)
#     print(arrival)
#
#     duration = route.find("div",class_="schedule-info-duration left column").text
#     print(duration)
#
#     escape = route.find("div",class_="column column-special-fare").text
#     print(escape)
#
#     economy = route.find("div",class_="column column-economy-fare column-economy-discounted-fare").text
#     print(economy)
#
#     economyPlus = route.find("div",class_="column column-economy-fare column-economy-regular-fare").text
#     print(economyPlus)
#
#     business = route.find("div",class_="column column-business-fare column-business-discounted-fare").text
#     print(business)
#
#     businessPlus = route.find("div",class_="column column-business-fare column-business-regular-fare").text
#     print(businessPlus)


# extracted_records = []
# for route in routes:
#     title = route.find("span",class_="schedule-info")
#     url = link['href']
#     #There are better ways to check if a URL is absolute in Python. For sake simplicity we'll just stick to .startwith method of a string
#     # https://stackoverflow.com/questions/8357098/how-can-i-check-if-a-url-is-absolute-using-python
#     if not url.startswith('http'):
#         url = "https://reddit.com"+url
#     # You can join urls better using urlparse library of python.
#     # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin
#     record = {
#         'title':title,
#         'url':url
#         }
#     extracted_records.append(record)
# print(extracted_records)





# # Instead of using requests.get, we just look at .page_source of the driver
# driver.page_source
#
# # We can feed that into Beautiful Soup
# doc = BeautifulSoup(driver.page_source, "html.parser")
#
# # It's a tricky table, but this grabs the linked names inside of the A
# #rows = doc.select("#datagrid_results tr")
# rows = doc.find('table', id='datagrid_results').find_all('tr', attrs={'class': None})
#
# doctors = []
# for row in rows:
#     # print(row.attrs)
#     # Find the ones that don't have 'style' as an attribute
#     if 'style' in row.attrs:
#         # Skip it! It's a header or footer row
#         pass
#     else:
#         cells = row.find_all("td")
#         doctor = {
#             'name': cells[0].text,
#             'number': cells[1].text,
#             'profession': cells[2].text,
#             'type': cells[3].text,
#             'status': cells[4].text,
#             'city': cells[5].text,
#             'state': cells[6].text
#         }
#         doctors.append(doctor)
#
# print(doctors)
