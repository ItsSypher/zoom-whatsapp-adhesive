import os

#unused func opens directly zoom link in linux not tested anywhere else
def join_link(link):
    confno=pwd_hash=''
    
    i=3
    while not (link[i-3:i]=='/j/' ):
        i+=1
        
        if i >= len(link):
            break
            
    while(link[i].isnumeric()):
        confno=confno+link[i]
        i+=1
        
        if i >= len(link):
            break
            
    
    #print("cong",confno)
    pwd_hash=link[-32:]
    link= "\'zoommtg://zoom.us/join?confno=" + confno + "&pwd=" + pwd_hash + "&zc=0&browser=firefox&uname=Shabd\'"
    #print(link)
    os.system('xdg-open ' + link)
#mlink="https://us04web.zoom.us/j/2401307052?pwd=OGhOR2d2OFJCZ1BkeCtRSXdJcUcxQT09"
#join_link(mlink)
