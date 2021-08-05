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

    pwd_hash=link[-32:]
    link= "\'zoommtg://zoom.us/join?confno=" + confno + "&pwd=" + pwd_hash + "&zc=0&browser=firefox&uname=Shabd\'"
    os.system('xdg-open ' + link)
