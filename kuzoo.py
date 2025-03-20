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
