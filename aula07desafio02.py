import requests

url = 'http://pudim.com.br/'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print('Site acessível')
    else:
        print(f'Site inacessível')
except:
    print(f'Site inacessível')
