For using on the linux OS, you should install pip3 and download api of vk

    sudo apt install pip3
    pip3 install vk

Set the tokens:

the app user token from the https://vkhost.github.io/   -> KateMobile  
https://oauth.vk.com/blank.html#access_token=&(THERE IS WILL BE YOUR TOKEN)&expires_in=0&user_id=&(your user id)  
Example: user_token = '123456789qwertyuiop'  

If your need service token:  

the app service token     https://vk.com/editapp?id=&(app id)&section=options  

Set the chat id:  

Open in the browser chat, for example: https://vk.com/im?sel=c1  
The chat id is after 'sel=c'  
Then change the id in the program  
chat_id = 1  

Then u can interpreting the python file  

    python3 vkParser.py  
