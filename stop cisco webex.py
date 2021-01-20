import os
import time
taskname ='"'
taskname+='atmgr.exe'  #this is its name , the cisco pop up name
taskname+='"'
print(taskname +'will be terminated \n\n')
try:
    os.popen('taskkill /IM '+taskname+' /F')
except:
    print("task could not be terminated")
    
time.sleep(2)
