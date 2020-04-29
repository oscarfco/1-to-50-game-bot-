from selenium import webdriver
from time import sleep

# For other use, select the location of chromedriver within your own computer.
driver = webdriver.Chrome("C:/Users/Oscar/Desktop/chromedriver.exe")

driver.get("http://zzzscore.com/1to50/en/?ts=1585942088831")


# Looks at the xpath links in the HTML to determine which square corresponds to number
# sorts the numbers in an array for easy clicking later on.
def get_elements(n):
    grids = [None] * 25
    for i in range(1, 26):
        i = str(i)
        link = "//*[@id=\"grid\"]/div[" + i + "]/span"
        el = driver.find_element_by_xpath(link)
        z_value = int(el.value_of_css_property("z-index"))
        grids[n-z_value] = el

    return grids

grids = get_elements(99)
for element in grids:
    element.click()

sleep(0.01)

new_grids = get_elements(74)
for new_element in new_grids:
    new_element.click()

sleep(20)
driver.close()