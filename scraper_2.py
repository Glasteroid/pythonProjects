import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Sony-Full-frame-Mirrorless-Interchangeable-Lens-ILCE7M3K/dp/B07B45D8WV/ref=sr_1_3?crid=3UZ7TCSX6RNIP&dib=eyJ2IjoiMSJ9.xNZSddm1Xv1MRMQT25XCSTSblLyqSlywKLyKO5q51-uNhW7mX5FAAq1qi2Pc86VQhkNYEDjvc4ElGVKHJRbXdiL7e94TXLYfPMbpmwkfeOdh6BRcoiOrD2loYtplgtlceoUMm6Db7WMHFLOHYyZ0OtqsVdwofSc44AUXnsxHpyW-c86M4OuaRvavPRVbzjVoUjyQBLG2Jox2c2b9xDsIkx1FKdSau5TA9hNPlqraZCA.idZph8wkBLukNkYazVKEE1yAgNAN2TGNGIoD6ZpQXT8&dib_tag=se&keywords=sony+a7&qid=1711413387&sprefix=sony+a7%2Caps%2C164&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()

print(title.strip())