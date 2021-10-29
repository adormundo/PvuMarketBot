import requests
from pandas import json_normalize
import webbrowser
import time
import os
import pandas as pd

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))


def start():
    print(""" ______     ___   _ __  __    _    ____  _  _______ _____ """)
    print("""|  _ \ \   / / | | |  \/  |  / \  |  _ \| |/ / ____|_   _|""")
    print("""| |_) \ \ / /| | | | |\/| | / _ \ | |_) | ' /|  _|   | | """)
    print("""|  __/ \ V / | |_| | |  | |/ ___ \|  _ <| . \| |___  | |  """)
    print("""|_|     \_/   \___/|_|  |_/_/   \_\_| \_\_|\_\_____| |_|  """)
    print("""                            by: ( ͡❛ᴗ ͡❛) Walffoaruzineo\n""")
    time.sleep(2)


def navegador():
    print('Which browser to use? ')
    print('[y] - Microsoft Edge ')
    print('[n] - Default Browser \n')
    navega = input('Inform option (y/n): ').lower()
    os.system('cls')
    if navega == 'y' or navega == 'n':
        return navega
    else:
        os.system('cls')
        navegador()
    return navega


def blocodenotas(text):
    if os.path.isfile(text):
        arquivo = open(text, "r")
        token = arquivo.readlines()
        token = token[0]
        arquivo.close()
        return token
    else:
        arquivo = open(text, "w")
        arquivo.write(input('Insert your token: '))
        token = arquivo
        arquivo.close()
        return token


def mytoken():
    tokenk = tokenpass
    os.system('cls')
    headers = {
        'authority': 'backend-farm.plantvsundead.com',
        'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Bearer Token: {tokenk}',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://marketplace.plantvsundead.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://marketplace.plantvsundead.com/',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'if-none-match': 'W/"143e-1Xi4LOEJ7ai9FCe/iMzph/A+FTY"',
    }

    params = (
        ('offset', '0'),
        ('limit', '10'),
        ('type', '1'),
    )

    responsetest = requests.get('https://backend-farm.plantvsundead.com/get-plants-filter-v2', headers=headers,
                                params=params)

    if responsetest.status_code == 200:
        print('Connection made successfully!\n')
        teste = json_normalize(responsetest.json())
        plantstotal = pd.DataFrame(teste['total'])
        plantstotal = plantstotal.loc[0].at['total']
        return tokenk, plantstotal
    else:
        print('Failed server not response')
        time.sleep(3)
        os.system('exit')


def defineplants():
    print('How many plants to search?')
    print('[y] - Max')
    print('[n] - Choose\n')
    defineqntplant = input('Inform option (y/n): ').lower()
    os.system('cls')
    if defineqntplant == 'y':
        os.system('cls')
        return getjson(inicio[0], inicio[1])
    elif defineqntplant == 'n':
        mychoose = int(input('Set your quantity: '))
        os.system('cls')
        return getjson(inicio[0], mychoose)
    else:
        os.system('cls')
        defineplants()


def getjson(token, qnt):
    headers = {
        'authority': 'backend-farm.plantvsundead.com',
        'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Bearer Token: {token}',
        'sec-ch-ua-mobile': '?0',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50",
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://marketplace.plantvsundead.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://marketplace.plantvsundead.com/',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'if-none-match': 'W/"143e-1Xi4LOEJ7ai9FCe/iMzph/A+FTY"',
    }

    params = (
        ('offset', '0'),
        ('limit', f'{qnt}'),
        ('type', '1'),
    )

    response = requests.get('https://backend-farm.plantvsundead.com/get-plants-filter-v2', headers=headers,
                            params=params)
    market_json = json_normalize(response.json()["data"])
    if response.status_code == 200:
        os.system('cls')
        print(f'Found in store {qnt}')
        market_pvu = pd.DataFrame(market_json)
        market_pvu = market_pvu.rename(columns={'id': 'ID', 'config.stats.type': 'TYPE', 'startingPrice': 'PRICE',
                                                'config.farm.le': 'LE', 'config.farm.hours': 'HOURS',
                                                'config.stats.damagePhysics': 'D.PHY',
                                                'config.stats.damageMagic': 'D.MAG',
                                                'config.stats.damagePure': 'D.PURE'})
        market_pvu['DAY'] = market_pvu['HOURS'] / 24
        market_pvu['LE/H'] = market_pvu['LE'] / market_pvu['HOURS']
        market_pvu = market_pvu.loc[0:market_pvu.shape[0], ['ID', 'TYPE', 'D.PHY', 'D.MAG', 'D.PURE', 'PRICE', 'LE',
                                                            'HOURS', 'DAY', 'LE/H']]
        return filtro(market_pvu)
    else:
        print('Failed server not response')
        time.sleep(3)
        os.system('exit')


def filtro(market_pvu):
    print('Filter by plant and a maximum price?')
    print('[y] - Plant and Price')
    print('[n] - Plant')
    print('[yn] - Price')
    filterinit = input('Inform option (y/n/yn): ')
    os.system('cls')
    if filterinit == 'y':
        print('Type Plants:')
        print('[Dark] [Electro] [Fire] [Ice] [Light] [Parasite] [Metal] [Water] [Wind]')
        plantopc = str(input('Which plant?: ')).lower()
        pricerange = int(input('What maximum price?: '))
        os.system('cls')
        market_pvu = market_pvu.loc[market_pvu['ID'] <= 9999999999]
        market_pvu = market_pvu.sort_values(['LE/H'], ascending=False)
        market_pvu = market_pvu.loc[(market_pvu['PRICE'] <= pricerange) & (market_pvu['TYPE'] == plantopc)]
        if market_pvu.empty != True:
            print(market_pvu.head(20).to_string())
            return compra(market_pvu, escolhe)
        else:
            os.system('cls')
            return defineplants()
    elif filterinit == 'n':
        print('[Dark] [Electro] [Fire] [Ice] [Light] [Parasite] [Metal] [Water] [Wind]')
        plantopc = str(input('Which plant?: '))
        os.system('cls')
        market_pvu = market_pvu.loc[market_pvu['ID'] <= 9999999999]
        market_pvu = market_pvu.sort_values(['LE/H'], ascending=False)
        market_pvu = market_pvu.loc[market_pvu['TYPE'] == plantopc]
        print(market_pvu.head(20).to_string())
        return compra(market_pvu, escolhe)
    elif filterinit == 'yn':
        pricerange = int(input('What maximum price?: '))
        os.system('cls')
        market_pvu = market_pvu.loc[market_pvu['ID'] <= 9999999999]
        market_pvu = market_pvu.sort_values(['LE/H'], ascending=False)
        market_pvu = market_pvu.loc[market_pvu['PRICE'] <= pricerange]
        print(market_pvu.head(20).to_string())
        return compra(market_pvu, escolhe)
    else:
        defineplants()


def compra(market_pvu, param2):
    compra = str(input("Buy (y/n) ")).lower()
    if compra == 'y':
        webbrowser.get('edge').open(f'https://marketplace.plantvsundead.com/#/plant/{market_pvu["ID"].iloc[2]}')
        webbrowser.get('edge').open(f'https://marketplace.plantvsundead.com/#/plant/{market_pvu["ID"].iloc[1]}')
        webbrowser.get('edge').open(f'https://marketplace.plantvsundead.com/#/plant/{market_pvu["ID"].iloc[0]}')
        indexplant = int(input("Insert plant index: "))
        plantid = market_pvu.loc[indexplant]['ID']
        if param2 == 'y':
            webbrowser.get('edge').open(f'https://marketplace.plantvsundead.com/#/plant/{plantid}')
        if param2 == 'n':
            webbrowser.open(f'https://marketplace.plantvsundead.com/#/plant/{plantid}')
        answer = (input('Refresh (y/n): ')).lower()
        if answer == 'y':
            os.system('cls')
            defineplants()
    else:
        answer = (input('Refresh (y/n): ')).lower()
        if answer == 'y':
            os.system('cls')
            defineplants()
        else:
            os.system('exit')


if __name__ == '__main__':
    start()
    tokenpass = blocodenotas("token.txt")
    escolhe = navegador()
    inicio = mytoken()
    market_pvu = defineplants()
