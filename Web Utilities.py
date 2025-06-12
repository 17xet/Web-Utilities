import requests
import os
import threading
import base64
import json
from datetime import datetime
from pystyle import Colorate, Colors, Center
from colorama import Fore

class mainfuncs:
    def clear():
        os.system("cls") if os.name == "nt" else os.system("clear")

    def title(args=None):
        os.system("title Web utils") if args == None else os.system(f"title Web utils {args}")

    def convert_image_to_base64(path):
        with open(path, 'rb') as f:
            data = base64.b64encode(f.read()).decode('utf-8')
            return data
ascii_art_title = """
 █     █░▓█████  ▄▄▄▄       █    ██ ▄▄▄█████▓ ██▓ ██▓     ██▓▄▄▄█████▓ ██▓▓█████   ██████ 
▓█░ █ ░█░▓█   ▀ ▓█████▄     ██  ▓██▒▓  ██▒ ▓▒▓██▒▓██▒    ▓██▒▓  ██▒ ▓▒▓██▒▓█   ▀ ▒██    ▒ 
▒█░ █ ░█ ▒███   ▒██▒ ▄██   ▓██  ▒██░▒ ▓██░ ▒░▒██▒▒██░    ▒██▒▒ ▓██░ ▒░▒██▒▒███   ░ ▓██▄   
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀     ▓▓█  ░██░░ ▓██▓ ░ ░██░▒██░    ░██░░ ▓██▓ ░ ░██░▒▓█  ▄   ▒   ██▒
░░██▒██▓ ░▒████▒░▓█  ▀█▓   ▒▒█████▓   ▒██▒ ░ ░██░░██████▒░██░  ▒██▒ ░ ░██░░▒████▒▒██████▒▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒   ░▒▓▒ ▒ ▒   ▒ ░░   ░▓  ░ ▒░▓  ░░▓    ▒ ░░   ░▓  ░░ ▒░ ░▒ ▒▓▒ ▒ ░
  ▒ ░ ░   ░ ░  ░▒░▒   ░    ░░▒░ ░ ░     ░     ▒ ░░ ░ ▒  ░ ▒ ░    ░     ▒ ░ ░ ░  ░░ ░▒  ░ ░
  ░   ░     ░    ░    ░     ░░░ ░ ░   ░       ▒ ░  ░ ░    ▒ ░  ░       ▒ ░   ░   ░  ░  ░  
    ░       ░  ░ ░            ░               ░      ░  ░ ░            ░     ░  ░      ░  
                      ░                                                                   
"""
mainfuncs.clear()
mainfuncs.title()
print(Colorate.Vertical(Colors.purple_to_blue, ascii_art_title))
hook = input("| ~ $ > Webhook: ")

while True:
    r = requests.get(hook)
    decode = r.json()
    name = decode.get("name")
    id = decode.get("id")
    mainfuncs.clear()
    print(Colorate.Vertical(Colors.purple_to_blue, ascii_art_title))
    options = f"""
~ > Patched in as {name} | {id} < ~

| {Fore.LIGHTBLACK_EX}~{Fore.RESET} > [01] : Webhook Spammer    | {Fore.LIGHTBLACK_EX}~{Fore.RESET} > [04] : Webhook Sniffer
| {Fore.LIGHTBLACK_EX}~{Fore.RESET} > [02] : Webhook Deleter    | {Fore.LIGHTBLACK_EX}~{Fore.RESET} > [05] : Webhook PFP
| {Fore.LIGHTBLACK_EX}~{Fore.RESET} > [03] : Webhook Renamer    | {Fore.LIGHTBLACK_EX}~{Fore.RESET} > [06] : Webhook looks

~ > Run #change [newhook] to change hook < ~
    """
    print(options)

    user_input = str(input(f"DC-RAPE@{os.getlogin()} ~ $ "))
    print()

    if user_input == "1":
        use_preset = input("| ~ $ > Use preset [y/n] : ")
        if use_preset.lower() == "y":
            with open("Data/Config.json") as f:
                config = json.load(f)
                for n in config:
                    print(f"[ {Fore.YELLOW}CONFIG{Fore.RESET} ] Config: {n}")
                c = input("| ~ $ > Config: ")
                content = config.get(c).get("message")
                embed_ask = config.get(c).get("embed")
                title = config.get(c).get("embed-data").get("title")
                desc = config.get(c).get("embed-data").get("desc")
                field_name = config.get(c).get("embed-data").get("field-name")
                message = config.get(c).get("embed-data").get("content")
                th = config.get(c).get("threading")
                thread_count = config.get(c).get("thread-count")

        else:
            content = input("| ~ $ > Message: ")


            embed_ask = input("| ~ $ > Embed? [y/n] : ")
            th = input("| ~ $ > Threaing? [y/n] : ")
            if th.lower() == "y":
                thread_count = int(input("| ~ $ > Thread count: "))
            if embed_ask.lower() == "y":
                title = input("| ~ $ > Embed title: ")
                desc = input("| ~ $ > Embed desc: ")
                field_name = input("| ~ $ > Field name: ")
                message = input("| ~ $ > Field message: ")
        if embed_ask.lower() == "y":
            data = {
                'content' : content,
                'embeds' : [{
                    'title' : title,
                    'description' : desc,
                    'fields' : [{
                        'name' : field_name,
                        'value' : message,
                        'inline' : False
                    }]
                }]
            }
        else:
            data = {'content' : content}
        def send_data():
            while True:
                r = requests.post(hook, json=data)
                if r.status_code == 204:
                    print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.GREEN} SUCCESS {Fore.RESET}] | {r.status_code}")
                else:
                    print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.RED} RFAILED {Fore.RESET}] | {r.status_code}")

        if th.lower() == "y":

            threads = []



            for i in range(int(thread_count)):
                t = threading.Thread(target=send_data)
                t.daemon = True
                t.start()
                threads.append(t)

            for thread in threads:
                thread.join()

        else:
            send_data()
    elif user_input == "2":
        r = requests.get(hook)
        decode = r.json()
        if 'name' in decode:
            id = decode['id']
            webhook_token = decode['token']
            r = requests.delete(f"https://discord.com/api/v9/webhooks/{id}/{webhook_token}")
            if r.status_code == 204:
                print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.GREEN} SUCCESS {Fore.RESET}] | {r.status_code}")
                input()
            else:
                input()
                print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.RED} RFAILED {Fore.RESET}] | {r.status_code}")
        else:
            print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.RED} RFAILED {Fore.RESET}] | {r.status_code}")
            input()

    elif user_input == "3":
        name = input("| ~ $ > New name: ")
        r = requests.get(hook)
        decode = r.json()
        if 'name' in decode:
            id = decode.get('id')
            data = {
                'name' : name
            }

            r = requests.patch(hook, json=data)
            if r.status_code == 200:
                print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.GREEN} SUCCESS {Fore.RESET}] | {r.status_code}")
                input()
            else:
                print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.RED} RFAILED {Fore.RESET}] | {r.status_code}")
                input()
        else:
            print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.RED} RFAILED {Fore.RESET}] | {r.status_code}")
            input()

    elif user_input == "4":
        r = requests.get(hook)
        decode = r.json()

        #  |<~~>| Hook Data |<~~>|

        appid = decode.get('application_id')
        hookavatar = decode.get('avatar')
        channelid = decode.get('channel_id')
        guildid = decode.get('guild_id')
        hookid = decode.get('id')
        name = decode.get('name')
        type = decode.get('type')
        token = decode.get('token')

        #  |<~~>| User Data |<~~>|
        
        id = decode.get('user').get('id')
        username = decode.get('user').get('user')
        avatar = decode.get('user').get('avatar')
        pub_flags = decode.get('user').get('public_flags')
        flahs = decode.get('user').get('flags')
        banner = decode.get('user').get('banner')
        accent_color = decode.get('user').get('accent_color')
        global_name = decode.get('user').get('global_name')
        avatar_dec_data = decode.get('user').get('avatar_decoration_data')
        ban_col = decode.get('user').get('banner_color')


        user_data = f"""
[ {Fore.YELLOW}USER{Fore.RESET} ] Username: {username}
[ {Fore.YELLOW}USER{Fore.RESET} ] ID: {id}
[ {Fore.YELLOW}USER{Fore.RESET} ] Avatar: {avatar}
[ {Fore.YELLOW}USER{Fore.RESET} ] Public flags: {pub_flags}
[ {Fore.YELLOW}USER{Fore.RESET} ] Flags: {flahs}
[ {Fore.YELLOW}USER{Fore.RESET} ] Banner: {banner}
[ {Fore.YELLOW}USER{Fore.RESET} ] Accent color: {accent_color}
[ {Fore.YELLOW}USER{Fore.RESET} ] Global name: {global_name}
[ {Fore.YELLOW}USER{Fore.RESET} ] Avatar decoration data: {avatar_dec_data}
[ {Fore.YELLOW}USER{Fore.RESET} ] Banner color: {ban_col}
    """

        hook_data = f"""
[ {Fore.YELLOW}HOOK{Fore.RESET} ] Application ID: {appid}
[ {Fore.YELLOW}HOOK{Fore.RESET} ] Avatar: {hookavatar}
[ {Fore.YELLOW}HOOK{Fore.RESET} ] Channel ID: {channelid}
[ {Fore.YELLOW}HOOK{Fore.RESET} ] Guild ID: {guildid}
[ {Fore.YELLOW}HOOK{Fore.RESET} ] Hook ID: {hookid}
[ {Fore.YELLOW}HOOK{Fore.RESET} ] Name: {name}
[ {Fore.YELLOW}HOOK{Fore.RESET} ] Type: {type}
[ {Fore.YELLOW}HOOK{Fore.RESET} ] Token: {token}
    """

        print(hook_data, user_data)
        input()

    elif user_input == "5":
        image = input("| ~ $ > Image: ")

        base64_data = mainfuncs.convert_image_to_base64(image)

        r = requests.get(hook)
        decode = r.json()
        id = decode.get('id')
        token = decode.get('token')

        data = {
            'avatar' : f"data:image/jpeg;base64,{base64_data}"
        }

        r = requests.patch(f"https://discord.com/api/v9/webhooks/{id}/{token}", json=data)

        if r.status_code == 200:
            print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.GREEN} SUCCESS {Fore.RESET}] | {r.status_code}")
            input()
        else:
            print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.RED} RFAILED {Fore.RESET}] | {r.status_code}")
            input()
    elif user_input == "6":
        with open(f"Data/Style.json") as f:
            config = json.load(f)
            for n in config:
                image_file = config.get(n).get("image")
                username = config.get(n).get("username")
                data = f"\n[ {Fore.YELLOW}CONFIG{Fore.RESET} ] ~ Config ~\n[ {Fore.YELLOW}CONFIG{Fore.RESET} ] Name: {n}\n[ {Fore.YELLOW}CONFIG{Fore.RESET} ] Image File: {image_file}\n[ {Fore.YELLOW}CONFIG{Fore.RESET} ] Username: {username}\n"
                print(data)
            c = input("| ~ $ > Config: ")
            image_file = config.get(c).get("image")
            username = config.get(c).get("username")
        base64_data = mainfuncs.convert_image_to_base64(image_file)
        data = {
            'avatar' : f"data:image/jpeg;base64,{base64_data}",
            'name' : f"{username}"
        }
        r = requests.patch(hook, json=data)
        if r.status_code == 200:
            print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.GREEN} SUCCESS {Fore.RESET}] | {r.status_code}")
            input()
        else:
            print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} [{Fore.RED} RFAILED {Fore.RESET}] | {r.status_code}")
            input()
    elif "#change " in user_input:
        hook = user_input.split(" ")[1]
        input(f"[ {Fore.LIGHTMAGENTA_EX}EDIT{Fore.RESET} ] Hook changed")