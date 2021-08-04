import time
from datetime import date


#returns time tuple(hour, minutes) and date
def get_time():
    t = time.localtime()
    #print(type(t))
    time_str = time.strftime("%H:%M", t)
    time_rn=(int(time_str.split(":")[0]),int(time_str.split(":")[1]))
    today = date.today()
    return time_rn, int(today.strftime("%d"))


#checks for if class rn by comparing class time and time right now
times=times_raw={}
def which_class_rn(info):
    is_clas_rn=False
    index_clas_rn=-1
    for index, clas in enumerate(info):
        timern, date = get_time()
        
        if (clas["has_time"]):
            
#             #print(index, clas["time"])
#             this_time_raw=clas["time"].split()[3:5]    
#             date_clas=int(clas["time"].split()[1][:-1])
#             #print(date)
#             hours = int(this_time_raw[0].split(":")[0])  
#             minutes= int(this_time_raw[0].split(":")[1])
            
#             if(this_time_raw[1]=='PM' and hours != 12):
#                 this_time= (hours+12,minutes) 
#             else:
#                 this_time= (hours,minutes) 
#                 #times_raw[index]=this_time_raw
            
            #for testing
            #timern=(11,20)
            #date=29
            
            this_time=clas["time"][0]
            this_date=clas["time"][1]
            print("this_time")
            time_diff=((this_time[0]-timern[0])*60 + this_time[1]-timern[1])
            #print(time_diff)
            if(time_diff <= 10 and time_diff >= -10 and date==this_date):
                is_clas_rn=True
                index_clas_rn=index
            times[index]=this_time
    #print(times_raw)
    #print(times)
    #print(is_clas_rn, index_clas_rn)
    return is_clas_rn, index_clas_rn
    
#which_class_rn(msg_info)
#get_time()
