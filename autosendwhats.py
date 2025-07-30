# sending whatsapp text messages without closing and opening windows.i
# Emulates keyboard shortcuts. IF a numebr is not found, it screws everything up.. hopefully i can write an error catcher later.
# If the number is not correct of found, you must change window and hit ctrl+c in your console to stop the program, delete number from the list and restart.

import time
from webbrowser import open
import pyperclip    
from pyautogui import click, hotkey, press, size, typewrite

#numbers here in format areacode+number (10 digits only, ex: "0123456789","3214567898"  use quotes an commas to separate...)
numero = (" ")

#as soon as you run the script, you have 5 seconds to and click on the whatsappweb window.

time.sleep(5)
for i, number in enumerate(numero):
    #time.sleep(5)
    pyperclip.copy(number)
    time.sleep(1)
    hotkey('ctrl', 'alt', 'n')  # Opens a new chat in WhatsApp Web
    time.sleep(1)

    time.sleep(1)
    hotkey('ctrl','v')
    time.sleep(1)
    hotkey('enter')
#At this point the cursor is on the active chat's window for sending message. 

#THIS IS THE MESASGE you'll send. the "slash n" is a line break. the * is for bold text, ex: *this is bold* , will make those words bold face in WAPP. 
    
    pyperclip.copy(" This is an *example message. \n With a line break!!")
    
    #Paste and send message
    time.sleep(1)
    hotkey('ctrl', 'v')
    hotkey('enter')
    print ("mensaje enviado al numero: ",i, " ", number)
    time.sleep(2)
exit
