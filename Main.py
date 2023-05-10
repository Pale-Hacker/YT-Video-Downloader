import os 
from pytube import YouTube 

# --- # 

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Banner():
    Clear()
    print("""__     _________           __      ___     _                       _____                      _                 _           
\ \   / /__   __|          \ \    / (_)   | |                     |  __ \                    | |               | |          
 \ \_/ /   | |     ______   \ \  / / _  __| | ___  ___    ______  | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
  \   /    | |    |______|   \ \/ / | |/ _` |/ _ \/ _ \  |______| | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
   | |     | |                \  /  | | (_| |  __/ (_) |          | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
   |_|     |_|                 \/   |_|\__,_|\___|\___/           |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                                                                            
Created By : Pale-Hacker\n""")

def DownloadV():
    print("\nVideo Is Being Downloading .. ")
    YV = YT.streams.get_highest_resolution()
    YV.download()
    print("Video Successfully Downloaded ! ")

# --- # 

try:
 Banner()
 
 VLink = input("Enter Video Link : ")
 YT = YouTube(VLink)
 
 # --- # 
 
 Banner()
 print("Title : ", YT.title)
 print("Views : ", YT.views)
 print("Video Rating : ", YT.rating)
 print("Age Restricted : ", YT.age_restricted)
 print("Author : ", YT.author)
 
 
 # --- # 
 
 DownloadV()
 input("\n\nPress \"Enter\" To Exit ! ")
 
 # --- # 
except:
   print("Error !")
   exit()
