from modules.start import *
#doesnt work wen excuted individuall then remove modules.
# gets all messages as a list of strings
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

