import requests
url = 'https://od.moi.gov.tw/api/v1/rest/datastore/A01010000C-001277-053'
requests = requests.get(url, verify=False)
print(requests)