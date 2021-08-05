import os
import platform
from plyer import notification

def notifer(msg_info, index):
    class_info = msg_info[index]
    if class_info["has_name"]:
        teacher = class_info["teacher"]
    if class_info["has_time"]:
        timeofclass = class_info["time"]
    message = f'Class Starting Shortly By {teacher} At {timeofclass}'
    title = f'CLASS STARTING'

    plt = platform.system()

    if plt == 'Linux':
        command = f'''osascript -e 'display notification "{message}" with title "{title}"'
        '''
        try:
            os.system(command)
        except:
            print("cannot notify")
            pass
    
    elif plt == 'Darwin':
        command = f'''notify-send "{title}" "{message}"
		'''
        try:
            os.system(command)
        except:
            print("cannot notify")
            pass
    
    elif plt == 'Windows':
        try:
            notification.notify(
                title=title,
                message=message,
                app_icon=None,
                timeout=10,
            )
        except:
            print("cannot notify")
            pass
    
    else:
        print("Cannot determine operating system so no notifications for you :)")