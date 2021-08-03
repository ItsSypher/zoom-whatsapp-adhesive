from chromedriver_autoinstaller import install
import selenium.webdriver
import time

"""
def start_browser():
    options = selenium.webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=.chrome")
    driver = selenium.webdriver.Chrome(options=options)
    return driver
"""
install()
options = selenium.webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=.chrome")
driver = selenium.webdriver.Chrome(options=options)

def open_link(link,new_tab=False,switch_back=True):
    if new_tab:
        driver.execute_script("window.open('www.youtube,com', 'secondtab');")
        #driver.switch_to.window("secondtab")
    driver.get(link)
    #if switch_back:
        #add code to switch back
        
        
#open("link_text")    returns nothing    
    
def is_open_wait(wait):
    pg_loaded=False
    while pg_loaded == False:
        try:
            driver.find_element_by_class_name("_1vPMT")
            pg_loaded = True
        except:
            if wait:
                time.sleep(5)
                continue
            else:
                pg_loaded=False
                break;
    return pg_loaded

#is_open(link,wiat) return true if open false if not


def goto_clas(clas):
    class_grp=driver.find_element_by_xpath("//span[@title='" + clas + "']")
    class_grp.click()

