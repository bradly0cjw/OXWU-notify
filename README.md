# This is a modify version of orginal code
---
# Difference
1. Support Line ***Multiply*** Notification
2. Support Discord ***Multiply*** Webhooks
3. Fix Count Down Function

# Usage
> [!NOTE]   
> Only list diffence between mod and orginal Version

> [!TIP]    
> There is lot of tutoriel about how to get Discord Webhook URL and Line Acces Token.

> [!WARNING]
> Due to EULA of OX-WakeUP, This notify system is only for personal use. Do not use this for commercial use or use this to provide service to others.

> [!CAUTION]
> Count Down Feature is for reference only, it may not be accurate due to network delay, different devices, etc.
> Repository owner and autuor are not responsible for any loss caused by this feature.
> Use at your own risk.

## Install

> [!WARNING]    
> If you got any error, please check if you have installed python3.

* double click ```Install.bat``` and done.
> [!TIP]    
> If you are using linux, use ```Install.sh``` instead.

## enviroment setup
* rename `env.json.sample` to `env.json`<br>
in `env.json` modify

> [!IMPORTANT]  
> You need some basic knowledge about json file.

```py
{
    "WEBHOOK_URL": [
        {
            "name": "optional", #name (optional)
            "enabled": true, #enable this entry (boolean)
            "url": "Your Webhook URL" #Discord Webhook URL
        },
        {
            "name": "optional",
            "enabled": false,
            "url": "Your Webhook URL"
        }
        #add here
    ],
    "CITY": "Your City", #Your City
    "AREA": "Your Area", #Your Area
    "ACCESS_TOKEN": [
        {
            "name": "optional", #name (optional)
            "enabled": false, #enable this entry (boolean)
            "token": "Your Access Token" #Line Access Token
        },
        {
            "name": "optional",
            "enabled": false,
            "token": "Your Access Token"
        }
        #add here
    ]
}
``` 

> [!TIP]    
> If you want to add multiple instance, add following code at the end of the entry.

```py
Disocrd
        ,{
            "name": "optional",
            "enabled": false,
            "url": "Your Webhook URL"
        }

Line 
        ,{
            "name": "optional",
            "enabled": false,
            "token": "Your Access Token"
        }
```
---
## Discription Below is original part of readme.md  
### 猴子程式交流會[![Discord](https://discord.com/api/guilds/808241076657717268/widget.png)](https://discord.gg/rCZeuaucjf)
# 地牛Wake UP!連動 Discord-Webhook-EEW

# 安裝Python
Python的部分，使用官網或微軟商店安裝。
* 建議安裝3.7以上 3.10以下(3.10以上無法正常使用)
![image](https://cdn.discordapp.com/attachments/829731415435903018/902558511806943252/unknown.png)
# 安裝套件

> [!CAUTION]  
> This part is deprecated

開啟`Install.bat`，輸入`1`並按下Enter後就會開始安裝。
![image](https://cdn.discordapp.com/attachments/829731415435903018/902556564878164059/unknown.png)
![image](https://cdn.discordapp.com/attachments/829731415435903018/909467601082646548/unknown.png)

# 修改資料

> [!CAUTION]  
> This part is deprecated

在 `.env` 裡
```py
WEBHOOK_URL=YOUR_Webhook_URL #你的Webhook網址,取代掉YOUR_Webhook_URL
CITY=YOUR_CITY #你要顯示的縣、市 例:台北市,取代掉YOUR_CITY
AREA=YOYR_AREA #你要顯示的區 例:松山區,取代掉YOYR_AREA
```
# `地牛Wake UP!`軟體設定
將`speech.bat`設定為連動的軟體 (示意圖)
(記得勾選`僅執行一次`)
![image](https://cdn.discordapp.com/attachments/829731415435903018/902568066133680158/2021-10-26_224139.png)

> [!TIP]    
> If you are using linux, use ```speech.sh``` instead.

# 開發人員
特別感謝`Eric101201`，都他寫的🛐