import re
# import os
import json
# from dotenv import load_dotenv
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
from time import sleep
import concurrent.futures

# import asyncio
# load_dotenv()

countdown = True

def load_config():
    with open('env.json', mode='r', encoding='UTF8') as jfile:
        jdata = json.load(jfile)
    return {
        'webhook_url': [temp['url'] for temp in jdata['WEBHOOK_URL']],
        'webhook_enable': [temp['enabled'] for temp in jdata['WEBHOOK_URL']],
        'city': jdata['CITY'],
        'area': jdata['AREA'],
        'line_token': [temp['token'] for temp in jdata['ACCESS_TOKEN']],
        'line_enable': [temp['enabled'] for temp in jdata['ACCESS_TOKEN']],
    }
    
config = load_config()

with open('file.json', mode='r', encoding='UTF8') as jfile:
    jdate1 = json.load(jfile)

intensity = re.sub(r"(\d)$", "\\1級", jdate1["1"]).replace("-", "弱").replace("+", "強")
sec = int(jdate1["2"])


def lineNotifyMessage(line_token,line_enable, sec, city, Area, intensity):
    if not line_enable:
        return
    linecontent = f"\n倒數{sec}秒後抵達!" + '\n' + f"{city} {Area} {intensity}"
    headers = {
        'Authorization': f'Bearer {line_token}',
    }
    requests.post('https://notify-api.line.me/api/notify', headers=headers, data={'message': linecontent})
    if int(intensity[0]) >= 4:
        requests.post('https://notify-api.line.me/api/notify', headers=headers, data={'message': '\n震度較大 注意安全'})


def discordNotifyMessage(Webhook_URL,enable, sec, city, Area, intensity, countdown):
    if not enable:
        return
    webhook = DiscordWebhook(url=Webhook_URL, username="地牛Wake UP!",
                             avatar_url="https://cdn.discordapp.com/attachments/825307887219114034/902494942352519168/FB_IMG_1635241955969.jpg",
                             content=f'@everyone \n# 倒數{sec}秒抵達!')
    # if int(intensity[0]) >= 4:
    #     embed = DiscordEmbed(title=':rotating_light:【地震速報】', description='慎防搖晃(預估震度)', color='ff0000')
    # else:
    #     embed = DiscordEmbed(title=':rotating_light:【地震速報】', description='慎防搖晃(預估震度)', color='4DFD4D')
    embed = DiscordEmbed(title=':rotating_light:【地震速報】', description='慎防搖晃(預估震度)\n# 警報秒數: `'+str(sec)+'`秒')
    match (int(intensity[0])):
        case 0:
            embed.set_color('f4f9ff')
        case 1:
            embed.set_color('99dabb')
        case 2:
            embed.set_color('4cbe88')
        case 3:
            embed.set_color('00a355')
        case 4:
            embed.set_color('f0cc50')
        case 5:
            match (str(intensity[1])):
                case "弱":
                    embed.set_color('fb9330')
                case "強":
                    embed.set_color('f6642c')
        case 6:
            match (str(intensity[1])):
                case "弱":
                    embed.set_color('ff1920')
                case "強":
                    embed.set_color('ce0000')
        case 7:
            embed.set_color('6e30a1')
        
    embed.set_author(name='Powered by 地牛Wake UP!',
                     icon_url='https://cdn.discordapp.com/attachments/825307887219114034/902494942352519168/FB_IMG_1635241955969.jpg')
    embed.set_timestamp()
    embed.add_embed_field(name=f"{city}", value=f"{Area} {intensity}")
    webhook.add_embed(embed)
    webhook.execute()
    # if countdown == False:
    #     webhook.content=f'@everyone \n倒數{sec}秒抵達!\n***倒數已停止***'
    #     embed.set_color('ff0000')
    #     webhook.edit()
    #     return
    if sec == 0:
        webhook.content = f'@everyone \n已抵達!'
        # embed.set_color('03b2f8')
        webhook.edit()
        return

    while (sec and countdown):
        sec = sec - 1

        sleep(0.6)

        webhook.content = f'@everyone \n# 倒數{sec}秒後到達!'
        webhook.edit()

        if sec == 0:
            sleep(0.6)
            webhook.content = f'@everyone \n***已抵達!***'
            # embed.set_color('03b2f8')
            webhook.edit()
            break


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        secret= zip(config['line_token'], config['line_enable'])
        [executor.submit(lineNotifyMessage(x[0], x[1], sec, config['city'], config['area'], intensity)) for x in secret]
    pass

    # if len(Webhook_URL) !=1:
    # countdown = False

    with concurrent.futures.ThreadPoolExecutor() as executor:
        secret= zip(config['webhook_url'], config['webhook_enable'])
        [executor.submit(discordNotifyMessage(x[0], x[1], sec, config['city'], config['area'], intensity, countdown)) for x in secret]
        pass
    pass


main()
