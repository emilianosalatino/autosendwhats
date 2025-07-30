# Auto Send for WP.
A simple Python Script to send texts via WhatsApp automatically. 

I made it because everything else is too complex, or dependency heavy... I just needed to send texts. Also, this doesn't mess with opening and closing browser tabs as WP Web is suuuper slow when loading in new tabs or windows. 

It is **SLOW**... first of all... like 5 messages a minute. The sleep times are there for whatsapp web to load data. 

Basically it emulates keyboard shortcuts. 

IF a number is not found, it now verifies, and logs the number in a list, and hops to next number. It prints the list out at the end. 

It is written for Python 3.9.7, and easiest to use with Visual Studio Code.

Check Dependencies. You **MUST** be logged into your whatsapp already in Edge. One you run it in say VS Code, there's a 5 second gap for you to click on the browser's  whatsapp window and it works from there. 

WORKS IN EDGE BROWSER, SHOULD WORK IN OTHERS

pyperclip license notice:
Copyright (c) 2014, Al Sweigart
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the {organization} nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.
