#THIS IS MY CODE BY ARTEM
import subprocess
import os
import time


user = input("Enter the password:   ")

passw = '#here is your password'

devops = input("Welcome to admin panel here devops can control servers to use option just type a to start server, b to start network, c to delete world is danger, d to delete server, e to delete world in test server:   ")

def admin_panel():
    if user == passw:
        if devops == 'a':
            print("Compliting...")
            time.sleep(3)
            print("Completed start server 100%/100%")
            os.chdir("/home/#your directory")
            subprocess.run(["bash", "login_to_start_server.sh"])
        

        elif devops == 'b':
            print("Compliting...\n")
            time.sleep(3)
            os.chdir("/home/whoiam/devops/bash")
            print("Completed process of starting network bridge 100%/100%\n")
            subprocess.run(["bash", "brigde_login.sh"])
    
        elif devops == 'c':
            print("Compliting process...\n")
            time.sleep(4)
            print("Completed for 50%/100%\n")
            os.chdir("/home/#your directory")
            subprocess.run(["bash", "delete_world.sh"])
            print("Completed deleting world for 100%/100%\n")
        
        elif devops =='d':
            print("Compliting process...\n")
            time.sleep(4)
            print("Completed process for 50%/100%\n")
            os.chdir("/home/#your directory")
            subprocess.run(["bash", "delete_server.sh"])
            print("Completed deleting server 100%/100%\n")

        elif devops == 'e':
            print("Compliting process...\n")
            time.sleep(2)
            print("Completed process 50%/100%\n")
            os.chdir("/home/# your directory")
            subprocess.run(["bash", "delete_world_for_test.sh"])
            print("Process of deleting test world was finish\n")

        elif devops == 'f':
            print("Compliting process...\n")
            time.sleep(3)
            print("Process of deleting server for test was completed for 50%/100%\n ")
            os.chdir("/home/#your directory")
            subprocess(["bash", "delete_server_for_test.sh"])
            print("The process was completed")

        elif devops == 'g':
            print("Compliting process...\n")
            time.sleep(2)
            print("Process of backup world was completed for 50%")
            os.chdir("/home/#your directory")
            subprocess.run(["bash", "backup-world.sh"])
            print("Process of backup world was completed")
    else:
        print("access denied")

admin_panel()

