from urllib import response
import requests
from pystyle import Colorate, Colors, Center
from discord import Webhook, RequestsWebhookAdapter
import colorama
from os import system
from colorama import Fore
import threading
from time import sleep

response = requests.get("https://discord.com/api/webhooks/1")
status_code = response.status_code


colorama.init()
def WebHook():
 print(Colorate.Horizontal(Colors.purple_to_blue, f"[{Fore.MAGENTA}?{Fore.WHITE}] Webhook URL ↓"))
 url = input(f"{Fore.MAGENTA}")
 print(Colorate.Horizontal(Colors.purple_to_blue, f"[{Fore.MAGENTA}?{Fore.WHITE}] message ↓"))
 message = input(f"{Fore.MAGENTA}")
 print(f"{Fore.RED}After 30 messages the tool gets rate limited. Just leave it open and after 50 seconds it will return spamming.")
 sleep(4)
 threading.Thread(target=WebHook).start()
 while True:
  webhook = Webhook.from_url(f"{url}", adapter=RequestsWebhookAdapter())
  webhook.send(f"{message}")
  print(f"{Fore.GREEN}[!] Sent {message}")
  try:
      if response.status_code == 204 or response.status_code == 200:
          print(f"{Fore.GREEN}Message sent{Fore.RESET}")
      elif response.status_code == 429:
          print(f"{Fore.YELLOW}Rate limited ({response.json()['retry_after']}ms){Fore.RESET}")
          sleep(response.json()["retry_after"] / 1000)
        
      sleep(.01)
  except KeyboardInterrupt:
        break
def Delete():
 boucle1 = True
 while boucle1:
    system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, f"[{Fore.MAGENTA}?{Fore.WHITE}] Webhook URL ↓"))
    webhook_url = input(f"{Fore.MAGENTA}")
    if webhook_url.startswith("https://"):
        try:
            system('cls')
            requests.delete(webhook_url.rstrip())
            print(f"{Fore.GREEN}Webhook deleted !")
            sleep(3)
        except:
            system('cls')
            print(f"[{Fore.MAGENTA}!{Fore.WHITE}] Error on deleting the webhook.")
            sleep(2)
    else:
            system('cls')
            print(f"[{Fore.MAGENTA}!{Fore.WHITE}] Please insert a valid link.")
            sleep(2)
print(f"""
{Fore.MAGENTA}╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═  ╔═╗╔═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗
{Fore.MAGENTA}║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗  ╚═╗╠═╝╠═╣║║║║║║║╣ ╠╦╝
{Fore.MAGENTA}╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩  ╚═╝╩  ╩ ╩╩ ╩╩ ╩╚═╝╩╚═
{Fore.WHITE}By {Fore.MAGENTA}seltox#8888 {Fore.WHITE}and {Fore.MAGENTA}$olar#6666{Fore.WHITE}

                        [{Fore.MAGENTA}1{Fore.WHITE}] WebHook Spammer
                        [{Fore.MAGENTA}2{Fore.WHITE}] WebHook Deleter
""")
print(Colorate.Horizontal(Colors.purple_to_blue, f"[{Fore.MAGENTA}?{Fore.WHITE}] choice ↓"))
allah = input(f"{Fore.MAGENTA}")
if allah == '1': 
 WebHook()
if allah == '2': 
 Delete()

