import selenium.webdriver
import pickle

#comment the line below this and add the selenium.webdriver.Firefox() i need to do this for geckodriver to work
driver = selenium.webdriver.Firefox(executable_path='/Users/anonymous/Desktop/zoom-whatsapp-adhesive/geckodriver')
driver.get("http://web.whatsapp.com")
input("press enter")

#comment this later when u have added cookies once
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
#comment above line
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

elements = driver.find_elements_by_class_name("_22Msk")
print(len(elements))

messages=[]
for i in range(len(elements)):
    print(elements[i].text)
    messages.append(elements[len(elements)-i-1].text) 
    input()

#print(messages)
info=[]
def get_content(message):
    msg=message.split()
    #print(msg)
    
    i=0
    name=''
    while (msg[i] != "Join" and msg[i] != "is" ):
        name=name+msg[i]+' '
        if msg[i] == "Ma'am":
            break
        i+=1
        if i >= len(msg):
            break
        
    print("Name:", name)
    
    
    i=0
    time=''
    while(msg[i] != 'Time:' ):
        i+=1
        if i >= len(msg):
            break
    i+=1        
    if i < len(msg):
                       
        while msg[i] != 'Join' :
            time= time+ msg[i] + ' '
            if msg[i]=='India' :
                break
            i+=1
            if i >= len(msg):
                break
            
    print("time:", time)
    
    
    
    i=0
    link=''
    has_link=False
    
    while(i < len(msg)):
        if (msg[i].startswith('https')):
            has_link=True
            link=msg[i]
        i+=1    
        
    print("link:", link)
        
    
        
    print("\n")
    '''{"teacher": get_teacher(message),
                 "link" : get_link(message),
                 "time_meet" : get_time(message),
                 "id" : get_id(message),
                 "pass" : get_pass(message)
                }'''
def update_info(messages):
    info=[]
    for message in messages:
        get_content(message)

        
update_info(messages)
