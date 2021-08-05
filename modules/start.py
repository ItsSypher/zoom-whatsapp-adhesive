import chromedriver_autoinstaller 
import selenium.webdriver
import time
import os
import platform

chromedriver_autoinstaller.install(True)

#unsused func to start browser problem:driver becomes local
def start_browser():
    options = selenium.webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=.chrome")
    driver = selenium.webdriver.Chrome(options=options)
    return driver

#this is used as global
if platform.system() == 'Darwin' or platform.system() == 'Linux':
    directory = (f"{os.getcwd()}/.chrome")
elif platform.system() == 'Windows':
    directory = (f"{os.getcwd()}\\.chrome")
print(directory)
options = selenium.webdriver.ChromeOptions()
options.add_argument(r"user-data-dir={0}".format(directory))
driver = selenium.webdriver.Chrome(options=options)

#unused opens links yet to add support to switch and switch back
def open_link(link,new_tab=False,switch_back=True):
    if new_tab:
        driver.execute_script("window.open('www.youtube,com', 'secondtab');")
    driver.get(link)

#be defaults waits untill whatsapp is open else returns false
def is_open_wait(wait):
    pg_loaded=False
    while pg_loaded == False:
        try:
            driver.find_element_by_class_name("_1vPMT")
            pg_loaded = True
        except:
            if wait:
                time.sleep(2)
                continue
            else:
                pg_loaded=False
                break;
    return pg_loaded

# goes to clas
def goto_clas(clas):
    class_grp=driver.find_element_by_xpath("//span[@title='" + clas + "']")
    class_grp.click()

