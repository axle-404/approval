import os
import sys
import requests
import time
from rich.console import Console
from rich.panel import Panel

# Clear Function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Approval Function (Exact Code as Requested)
def approval():
    uuid = str(os.geteuid()) + "DS" + str(os.geteuid())
    id = "WADE-SHARE-TOOL-" + "".join(uuid)
    clear()
    print(f"\033[1;37m[{chr(27)}[36m•] \033[0;32mYou Need Approval To Use This Tool\033[1;37m")
    print(f"\033[1;37m[{chr(27)}[36m•] \033[0;32mYour Key :\033[0;31m {id}")
    time.sleep(0.1)
    print("\033[0;37m──────────────────────────────────────────────────────────")
    try:
        httpCaht = requests.get("https://github.com/axle-404/approval/edit/main/approval").text
        if id in httpCaht:
            print("\033[0;32m >> Your Key Has Been Approved !!!")
            time.sleep(1)
        else:
            print("\033[0;32m >> Send Key on Facebook")
            time.sleep(0.1)
            input(" >> Click Enter To Send Your Key ")
            tks = "Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:" + id
            os.system("xdg-open https://www.facebook.com/61573982738672" + tks)
            approval()
            time.sleep(1)
            exit()
    except:
        print(" >> Unable To Fetch Data From Server ")
        time.sleep(2)
        exit()

approval()

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
    
    token = input("Enter your Facebook token: ")
    link = input("Enter the post link: ")
    shares = int(input("Enter number of shares: "))

    console = Console()
    for i in range(shares):
        try:
            post = requests.post(f"https://graph.facebook.com/me/feed?link={link}&access_token={token}")
            if post.status_code == 200:
                console.print(Panel(f"Shared {i+1}/{shares} - [green]SUCCESS[/green]", title="Share Panel", style="cyan"))
            else:
                console.print(Panel("Error in sharing!", title="Error", style="red"))
        except:
            console.print(Panel("Connection Error!", title="Error", style="red"))
        time.sleep(0.02)  # 50 shares per second

bot_share()
