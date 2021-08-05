from modules.start import *
#doesnt work when excuted individuall then remove modules.
#gets all messages as a list of strings
def get_messages():    
    elements = driver.find_elements_by_class_name("_22Msk")
    print(len(elements))
    messages=[]
    for i in range(len(elements)):
        messages.append(elements[len(elements)-i-1].text) 
    return messages