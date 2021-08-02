from funcs import *

#driver = start_browser()
open_link('https://web.whatsapp.com')
is_open_wait(True)

while True:
    #input("class, and now scroll")
    time.sleep(1)
    msg_raw=get_messages()
    msg_info=update_info(msg_raw)
    rnclas , rnindex = which_class_rn(msg_info)
    print("right now is class: ", rnclas)
    if(rnclas):
        #print("rnclas")
        describe_clas(msg_info,rnindex)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(msg_info[rnindex]["link"])
        time.sleep(5)
        driver.close()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
    print("looping ", get_time()[0] )
    time.sleep(300)
