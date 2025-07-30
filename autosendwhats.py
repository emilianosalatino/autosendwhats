# This is Version 2...
# Sending whatsapp text messages without closing and opening windows. It can use emojis in VS Code
# It works by using keyboard shortcuts. 
# I added a number validation. IF a number is not found, or it isn't a whatsapp number, it now escapes a couple times and goes to a new chat box and also writes errors into variable and prints them out in console.
# This script requires the pyperclip and pyautogui libraries.
# Make sure you have WhatsApp Web open and logged in before running the script.

import time
#from webbrowser import open
import pyperclip    
from pyautogui import hotkey 

#numbers here in format areacode+number (10 digits only, ex: "0123456789","3214567898"  use quotes an commas to separate...). If from another country, it should be ok using the +countryareanumber with the plus sign. 
numero = ("","","","","")
message = (" THIS IS AN EXAMPLE MESSAGE 🤑🤑 🤑 \n TESTING... *TESTING*.. ....")
errores=[]

#IMPORTANT: As soon as you run the script, you have 5 seconds to and click on the whatsappweb window.

time.sleep(5)
for i, number in enumerate(numero):
    #time.sleep(5)
    pyperclip.copy(number)
    time.sleep(1)
    hotkey('ctrl', 'alt', 'n')  # Opens a new chat in WhatsApp Web
    time.sleep(1)
    
    #paste number
    hotkey('ctrl','v')
    time.sleep(1)
    hotkey('enter')
    
    #PASTE MESSAGE
    pyperclip.copy(message)
   # print(pyperclip.paste())
    hotkey('ctrl', 'v')
    time.sleep(1)

    #COPY NEW CHAT BOX CONTENT TO CLIPBOARD
    hotkey('ctrl','a')
    hotkey('ctrl','c')
    time.sleep(1)
   
    #CHECK IF NUMBER IS CORRECT (An error would be the number concatenated with the message if the number didn't exist and the script didn't jump to the text input box for the message).
    clip=pyperclip.paste()
    #print (clip)
    if clip != message:
        print("Number is incorrect: ",i," ", number)
        errores.append(number)
        #EREASE CONTENT OF NEW CHAT BOX
        hotkey('escape')
        hotkey('escape')            
        continue
        
    else:
        #SEND THE MESSAGE
        print("Number is correct: ",i, " ", number)
        hotkey('enter')
print (errores)
exit
