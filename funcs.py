import selenium.webdriver
import time


def start_browser():
    options = selenium.webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=.chrome")
    driver = selenium.webdriver.Chrome(executable_path=r'chromedriver', options=options)
    return driver


options = selenium.webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=.chrome")
driver = selenium.webdriver.Chrome(executable_path=r'chromedriver', options=options)


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


def get_messages():
    #driver.execute_script("window.scrollTo(0, 0);")
    #goto_clas(clas)
    
    
    elements = driver.find_elements_by_class_name("_22Msk")
    print(len(elements))
    
    
    messages=[]
    for i in range(len(elements)):
        #print(elements[i].text)
        messages.append(elements[len(elements)-i-1].text) 
        #input()
    return messages

#print(messages)

def get_content(message):
    msg=message.split()
    #print(msg)
    
    i=0
    name=''
    has_name=False
    while (msg[i] != "Join" and msg[i] != "is" ):
        name=name+msg[i]+' '
        has_name=True
        if msg[i] == "Ma'am" or msg[i]=="Sir" or msg[i]=="Mam":
            break
        i+=1
        if i >= len(msg):
            break
        
    #print("Name:", name)
    
    
    i=0
    time=''
    has_time=False
    while(msg[i] != 'Time:' ):
        i+=1
        if i >= len(msg):
            break
    i+=1        
    if i < len(msg):
                       
        while msg[i] != 'Join' :
            time= time+ msg[i] + ' '
            has_time=True
            if msg[i]=='India' :
                break
            i+=1
            if i >= len(msg):
                break
            
    #print("time:", time)
    
    
    
    i=0
    link=''
    has_link=False
    
    while(i < len(msg)):
        if (msg[i].startswith('https')):
            has_link=True
            link=msg[i]
        i+=1    
        
    #print("link:", link)
    
    if(has_link and has_time and False):
        print("name:", name)
        print("time:", time)
        print("link:", link)
        print("\n")
    
    mid=''
    passwd=''
    has_id=False
    has_passwd=False
    i=0
    while(msg[i]!="ID:"):
        i+=1
        if i >= len(msg):
            break
    i+=1
    while( i < len(msg) and msg[i]!="Passcode:" ):
        mid=mid+msg[i]
        has_passwd=has_id=True
        i+=1
    if(i< len(msg)):
        passwd=msg[i+1]
    
    
    
    info={"teacher": name,
          "has_name" : has_name,
         "time" : time,
          "has_time" : has_time,
         "link" : link,
          "has_link" : has_link,
         "id" : mid,
          "has_id" : has_id,
         "pass" : passwd}
    
    return info



    '''{"teacher": get_teacher(message),
                 "link" : get_link(message),
                 "time_meet" : get_time(message),
                 "id" : get_id(message),
                 "pass" : get_pass(message)
                }'''
def update_info(messages):
    info=[]
    for message in messages:
        info.append(get_content(message))
    return info
        
def describe_info(messages):
    extracted_info=update_info(messages)
    for info in extracted_info:
        if (info["has_name"] and info["has_time"] and info["has_link"]):
            for value in info:
                print(value, ":", info[value])
            print("\n")    
            
def describe_clas(msg_info, index):
    for value in msg_info[index]:
        print(value, ":", msg_info[index][value])
    print("\n")    

import time
from datetime import date

def get_time():
    t = time.localtime()
    #print(type(t))
    time_str = time.strftime("%H:%M", t)
    time_rn=(int(time_str.split(":")[0]),int(time_str.split(":")[1]))
    today = date.today()
    return time_rn, int(today.strftime("%d"))

times=times_raw={}
def which_class_rn(info):
    is_clas_rn=False
    index_clas_rn=-1
    for index, clas in enumerate(info):
        timern, date = get_time()
        if (clas["has_time"]):
            
            #print(index, clas["time"])
            this_time_raw=clas["time"].split()[3:5]    
            date_clas=int(clas["time"].split()[1][:-1])
            #print(date)
            hours = this_time= int(this_time_raw[0].split(":")[0])  
            minutes= int(this_time_raw[0].split(":")[1])
            
            if(this_time_raw[1]=='PM' and hours != 12):
                this_time= (hours+12,minutes) 
            else:
                this_time= (hours,minutes) 
                #times_raw[index]=this_time_raw
            
            #for testing
            #timern=(10,10)
            #date=29
            
            time_diff=((this_time[0]-timern[0])*60 + this_time[1]-timern[1])
            #print(time_diff)
            if(time_diff <= 10 and time_diff >= -10 and date==date_clas):
                is_clas_rn=True
                index_clas_rn=index
            times[index]=this_time
    #print(times_raw)
    #print(times)
    #print(is_clas_rn, index_clas_rn)
    return is_clas_rn, index_clas_rn
    
#which_class_rn(msg_info)
#get_time()

