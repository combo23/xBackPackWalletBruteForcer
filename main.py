import requests
import uuid
from datetime import datetime
from discord_webhook import *
from utils import get_proxy, webhook

headers = {
    'authority': 'invites.xnfts.dev',
    'accept': '*/*',
    'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-backpack-waitlist-id': '',
}

def log(code, message):
    print(f"{datetime.now()} | {code} | {message}")


def checkifavaible():
    try:
        code = uuid.uuid4()
        headers['x-backpack-invite-code'] = str(code)
        url = f"https://invites.xnfts.dev/check/{code}"
        check = requests.get(url, headers=headers, proxies=get_proxy(), timeout=10)
        if check.status_code == 200:
            log(code, f"FOUND! [{check.text}]")
            webhook(code)
        else:
            log(code, f"Failed [{check.status_code}] [{check.text}]")
    except Exception as e:
        log(e, "ERROR")

if __name__ == '__main__':
    while True:
        checkifavaible()