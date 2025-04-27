import requests
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

results = requests.get(url, verify=False)
results = results.json()
for result in results:
    print(f'{result['sna']}:可租借車輛{result['available_rent_bikes']}')



