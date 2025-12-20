import requests

cookies = {
    'PHPSESSID': '28402afbf01b480543145b0d41bcbbbd',
}

headers = {
    'authority': 'yhkkmb.btcnmt.my.id',
    'accept': 'text/plain, /; q=0.01',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=28402afbf01b480543145b0d41bcbbbd',
    'origin': 'https://yhkkmb.btcnmt.my.id',
    'referer': 'https://yhkkmb.btcnmt.my.id/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
data = {
    'email': 'Jangan nipu anak sekolahan bro',
    'sandi': 'Internet tidak seindah itu',
    'login': 'Saya akan proses ini sampe nemu titik terang',
}

while True:
    response = requests.post('https://yhkkmb.btcnmt.my.id/data.php', cookies=cookies, headers=headers, data=data)

    print('Status code:', response.status_code)
    if response.status_code != 200:
        print("Terjadi masalah dengan permintaan, keluar dari loop.")
        break