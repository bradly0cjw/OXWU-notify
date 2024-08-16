import datetime
import re
# import os
import json
# from dotenv import load_dotenv
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
from time import sleep
import time
import concurrent.futures
import socket

# import asyncio
# load_dotenv()

def scan():
    try:
        with open('report.json', mode='r', encoding='UTF8') as jfile:
            jdate = json.load(jfile)
            curt= time.time_ns()
            deltatime=curt-jdate['time']
            jdate['time'] = curt
            # print(deltatime)
            # 10 seconds
            if deltatime > 10000000000:
                jdate['report'] = 1
                with open('report.json', mode='w', encoding='UTF8') as jfile:
                    json.dump(jdate, jfile, ensure_ascii=False, indent=4)
            else:
                jdate['report']=int(jdate['report'])+1
                with open('report.json', mode='w', encoding='UTF8') as jfile:
                    json.dump(jdate, jfile, ensure_ascii=False, indent=4)
        return {
            'num':jdate['report'],
            'time':jdate['time']
            }
    except:
        print('error')
        with open('report.json', mode='w', encoding='UTF8') as jfile:
            jdate = {
                'time': time.time_ns(),
                'report': 1
            }
            json.dump(jdate, jfile, ensure_ascii=False, indent=4)
        return {
            'num':jdate['report'],
            'time':jdate['time']
            }
    
rep_config=scan()    

platform = socket.gethostname()

countdown = True

def load_config():
    with open('env.json', mode='r', encoding='UTF8') as jfile:
        jdata = json.load(jfile)
    return {
        'webhook_url': [temp['url'] for temp in jdata['WEBHOOK_URL']],
        'webhook_threshold': [temp['threshold'] for temp in jdata['WEBHOOK_URL']],
        'city': jdata['CITY'],
        'area': jdata['AREA'],
        'line_token': [temp['token'] for temp in jdata['ACCESS_TOKEN']],
        'line_threshold': [temp['threshold'] for temp in jdata['ACCESS_TOKEN']],
    }
    
config = load_config()

         

with open('file.json', mode='r', encoding='UTF8') as jfile:
    jdate1 = json.load(jfile)

intensity = re.sub(r"(\d)$", "\\1級", jdate1["1"]).replace("-", "弱").replace("+", "強")
intensity_calc = re.sub(r"(\d)$", "\\1", jdate1["1"]).replace("-", ".0").replace("+", ".5")
sec = int(jdate1["2"])


def lineNotifyMessage(line_token,line_threshold, sec, city, Area, intensity):
    if float(line_threshold)>float(intensity_calc) or float(line_threshold) < 0:
        return
    linecontent = f"\n【地震速報】第{rep_config['num']}報\n倒數{sec}秒後抵達!" + '\n' + f"{city} {Area} {intensity}"+'\n'+"發布時間: "+datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S\n%Z')+'\n發送裝置: '+platform
    headers = {
        'Authorization': f'Bearer {line_token}',
    }
    requests.post('https://notify-api.line.me/api/notify', headers=headers, data={'message': linecontent})
    # if int(intensity[0]) >= 4:
    #     requests.post('https://notify-api.line.me/api/notify', headers=headers, data={'message': '\n震度較大 注意安全'})


def discordNotifyMessage(Webhook_URL,threshold, sec, city, Area, intensity, countdown):
    if float(threshold)>float(intensity_calc) or float(threshold) < 0:
        return
    threshold = re.sub(r"^([5-6])$", "\\1弱", str(threshold))
    threshold = re.sub(r"^(\d)$", "\\1級", str(threshold)).replace(".0", "弱").replace(".5", "強")
    webhook = DiscordWebhook(url=Webhook_URL, username="地牛Wake UP!",
                             avatar_url="https://cdn.discordapp.com/attachments/825307887219114034/902494942352519168/FB_IMG_1635241955969.jpg",
                             content=f'@everyone \n# 倒數{sec}秒抵達!')
    # if int(intensity[0]) >= 4:
    #     embed = DiscordEmbed(title=':rotating_light:【地震速報】', description='慎防搖晃(預估震度)', color='ff0000')
    # else:
    #     embed = DiscordEmbed(title=':rotating_light:【地震速報】', description='慎防搖晃(預估震度)', color='4DFD4D')
    embed = DiscordEmbed()
    embed.set_title(':rotating_light:【地震速報】第'+str(rep_config['num'])+'報')
    embed.set_description("慎防搖晃")
    embed.add_embed_field(name='警報秒數', value=str(sec)+'秒', inline=True)
    embed.add_embed_field(name='預估震度', value=intensity, inline=True)
    embed.add_embed_field(name='發布時間', value=datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S` \n`%Z"), inline=True)
    embed.add_embed_field(name='預警地區', value=city+' '+Area, inline=True)
    embed.add_embed_field(name='預警閾值', value=threshold, inline=True)
    match (float(intensity_calc)):
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
        case 5.0:
            embed.set_color('fb9330')
        case 5.5:
            embed.set_color('f6642c')
        case 6.0:
            embed.set_color('ff1920')
        case 6.5:
            embed.set_color('ce0000')
        case 7:
            embed.set_color('6e30a1')
        
    embed.set_author(name='Powered by 地牛Wake UP!',
                     icon_url='https://cdn.discordapp.com/attachments/825307887219114034/902494942352519168/FB_IMG_1635241955969.jpg')
    embed.set_footer(text='發送裝置\n'+platform)
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    # if countdown == False:
    #     webhook.content=f'@everyone \n倒數{sec}秒抵達!\n***倒數已停止***'
    #     embed.set_color('ff0000')
    #     webhook.edit()
    #     return
    if sec == 0:
        webhook.content = f'@everyone \n***已抵達!***'
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
        secret= zip(config['line_token'], config['line_threshold'])
        [executor.submit(lineNotifyMessage(x[0], x[1], sec, config['city'], config['area'], intensity)) for x in secret]
    pass

    # if len(Webhook_URL) !=1:
    # countdown = False

    with concurrent.futures.ThreadPoolExecutor() as executor:
        secret= zip(config['webhook_url'], config['webhook_threshold'])
        [executor.submit(discordNotifyMessage(x[0], x[1], sec, config['city'], config['area'], intensity, countdown)) for x in secret]
        pass
    pass


main()