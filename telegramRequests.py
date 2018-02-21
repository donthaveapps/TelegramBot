import requests
chatId = "*id of your chat or group*"
botToken = "*key of your bot*"
msgText = "hello world"
r = requests.get("https://api.telegram.org/bot"+botToken+"/sendMessage?chat_id="+chatId+"&text="+str(msgText))
