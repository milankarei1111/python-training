import requests

# HTTP請求-存取Cookie , 傳參屬性:cookies 
url = "http://httpbin.org/cookies"
cookies = dict(name="Mike Wang")
response = requests.get(url, cookies=cookies)
print(response.text)
"""
{
  "cookies": {
    "name": "Mike Wang"
  }
}
"""

print("---------------取得回應內容的cookie-------------")
## 建立 Session物件
session = requests.Session()
rAge= session.get("http://httpbin.org/cookies/set/age/18")
print(rAge.text)
rSex = session.get("http://httpbin.org/cookies/set/sex/Male")
print(rSex.text)
"""
{
  "cookies": {
    "age": "18",
    "sex": "Male"
  }
}
"""

## 取得存放的cookie資訊，呼叫get_dict()轉換成字典，取得cookie資料
dictList = session.cookies.get_dict()
print(dictList) # {'age': '18', 'sex': 'Male'}


# HTTP請求-自訂標頭, 傳參屬性:headers 
print("---------------自訂標頭-------------")

url = "http://httpbin.org/user-agent"
response = requests.get(url)
print(response.text) # { "user-agent": "python-requests/2.28.1"}
url_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
response = requests.get(url, headers=url_headers)
print(response.text)
"""
{
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
}
"""

# HTTP請求-RESTful API

print("---------------RESTful API-------------")
url = "https://www.googleapis.com/books/v1/volumes"

url_params = {'q': 'Python',
              'maxResults': 3, 
              'projection': 'lite'}
response = requests.get(url, params=url_params)
#print(response.json()) # 因回傳值為JSON格式，使用json()解析

# HTTP請求-指定timeout時間, 傳參屬性:timeout
try:
    response = requests.get(url, timeout=0.03)
    print(response.text)
except requests.exceptions.Timeout as ex:
    print("錯誤: HTTP請求timeout...\n" + str(ex))

"""
錯誤: HTTP請求timeout...
HTTPSConnectionPool(host='www.googleapis.com', port=443): Read timed out. (read timeout=0.03)
"""