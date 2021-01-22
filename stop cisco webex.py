import os
import time
import subprocess
import time


taskname ='"'
taskname+='atmgr.exe'  #this is its name , the cisco pop up name
#taskname+='NOTEPAD.exe'  #troubleshooting code
taskname+='"'
while(True):
    try:
        #(os.popen('taskkill /IM '+taskname+' /F')) 
        st = str(subprocess.check_output('taskkill /IM '+taskname+' /F',shell = True).decode('utf-8'))
    except:
        print("\nall instances terminated ; exiting program....")
        time.sleep(2)
        exit()
        
    else :

        print(taskname +' terminated ')
    

