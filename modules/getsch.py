#print(messages)

#main algorithm of the data extraction returns feature dictionary of the individual msg pass
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
    time_str=time
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
    
    
    sent_time=(0,0)
    sent_time_raw=msg[-2:]    
    #print("sent time", sent_time_raw)
    hours = int(sent_time_raw[0].split(":")[0])  
    minutes = int(sent_time_raw[0].split(":")[1])
    
    if(sent_time_raw[1]=='PM' and hours != 12):
        sent_time= (hours+12,minutes) 
    else:
        sent_time= (hours,minutes) 
    #times_raw[index]=this_time_raw
    #print("sent time", sent_time)
    
    
    #print(index, clas["time"])
    if has_time:
        this_time_raw=time.split()[3:5]
        #print("this_time_raw:", this_time_raw)
        date_clas=int(time.split()[1][:-1])
        #print(date)
        hours = int(this_time_raw[0].split(":")[0])  
        minutes= int(this_time_raw[0].split(":")[1])

        if(this_time_raw[1]=='PM' and hours != 12):
            this_time= (hours+12,minutes) 
        else:
            this_time= (hours,minutes) 
            #times_raw[index]=this_time_raw
        time=(this_time,date_clas)
    else:
        time=((0,0),0) #time doesnt exist
        
    #time=((11,20),2)
    
    
    # dict details
    info={"teacher": name,
          "has_name" : has_name,
         "time" : time,
          "has_time" : has_time,
         "link" : link,
          "has_link" : has_link,
         "id" : mid,
          "has_id" : has_id,
         "pass" : passwd,
         "sent_time" : sent_time}
    
    return info



    '''{"teacher": get_teacher(message),
                 "link" : get_link(message),
                 "time_meet" : get_time(message),
                 "id" : get_id(message),
                 "pass" : get_pass(message)
                }'''

#calls get_content iteratively over all msgs and adds it to a list
def update_info(messages):
    info=[]
    for message in messages:
        info.append(get_content(message))
    return info


#describes the list of dicts getted from update info
def describe_info(all_info):
#    extracted_info=update_info(messages)
    for info in all_info:
        if (info["has_name"] and info["has_time"] and info["has_link"]):
            for value in info:
                print(value, ":", info[value])
            print("\n")    

#describes individual class by index            
def describe_clas(msg_info, index):
    for value in msg_info[index]:
        print(value, ":", msg_info[index][value])
    print("\n")   



#testing
#driver.get("https://web.whatsapp.com")
#input()
#goto_clas("11A Official 2021-22")
#describe_info(get_messages())
