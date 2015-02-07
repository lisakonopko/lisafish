class bcolors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

fish = """                                                  
                                                        
                       ,.   
                    ,-'.:\                
                 _/'.:'_:'`._    .-._                
            _.-''        ```-`.,'.::.`-._                
         _.'                    ``-..:.:.`-.             
       ,'          ____               `-:.:,'      _..-'|
     ,',.      ),''    ```--...___        `-.__..'':..  |
    / (O )   \  `.  ___....-----..``-...___      \::.   |
   /_' `'  /  )  /,'::::::._:.-'           ````-.-'- .-'|
   ,-`'. ,' ,'  /  ):::._,'             __...--../::.   |
   `.        _,'   `--''            _.''           `-.._|
     `''-..''_                   _.'.:`. SSt
              ``.  ..--....___.-' `:_.::/
                 \ .:`.              `-.\
                  \:::|
                   \_,'
"""

fish2 = """
   _.-=-._     .-, 
 .'       "-.,' / 
(          _.  <
 `=.____.="  `._\
                   HI LISA
"""

fish3 = """
                 |   
                 |     
                ,|.     
               ,\|/.     
             ,' .V. `.      
            / .     . \      
           /_`       '_\      
          ,' .:     ;, `.      
          |@)|  . .  |(@|                 
     ,-._ `._';  .  :`_,' _,-.             
    '--  `-\ /,-===-.\ /-'  --`           
   (----  _|  ||___||  |_  ----)         
    `._,-'  \  `-.-'  /  `-._,'       
             `-.___,-' ap              
"""

import os
import time
clear = lambda : os.system('tput reset')

def show_fish(fishy, delay=2):
  clear()
  print bcolors.OKBLUE + fishy + bcolors.ENDC
  time.sleep(delay)

while True:
  show_fish(fish)
  show_fish(fish2)
  show_fish(fish3)
