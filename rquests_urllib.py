# requests

# download and read data
# pip install requests

import requests

r = requests.get("https://github.com/Bob-Gohardani/RestFullAPI/blob/master/.gitattributes")
print(r)  # 200 response means ok

print(r.text)  # use beautifulsoup to parse it

# ==============================
# download and save image with request
r = requests.get("https://s3-us-east-2.amazonaws.com/aws2-gray-wp01-s3/appleholler-graydientlabs-net/wp-content/uploads/2018/07/03140233/359x217-apple-picking.png")

if r.ok:
    with open("./Files/apple.png", "wb") as f:
        f.write(r.content)
    else:
        print("there was an error downloading the file")


r = requests.get("https://s3-us-east-2.amazonaws.com/aws2-gray-wp01-s3/appleholler-graydientlabs-net/wp-content/uploads/2018/07/03140233/359x217-apple-picking.png")
print(r.status_code)
print(r.ok)
print(r.headers)

# ==========================
# instead of writing the parameters for the url in the string, you can write them in a dictionary and send it to url as params

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)    # https://httpbin.org/get?page=2&count=25

# =====================
# Post

payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.url)
r_dict = r.json() # # since response is json, we download it in json format instead of text
r_dict.keys()

# =========================
# Basic-Auth

r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
print(r.text)
print(r)

# =====================
# timeout: if the result doesnt comeback after 3 seconds throws an error

try:
    r = requests.get('https://httpbin.org/delay/5', timeout=3)
    print(r)
except requests.exceptions.ReadTimeout:
    print("Took more than 3 seconds to read the data")

# ==============================

# urllib
# download file from web with request and assign it a random name

import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'

    urllib.request.urlretrieve(url, full_name)  # (urlAdress, saveOfFileToBeSaved)

download_web_image('https://i5.walmartimages.ca/images/Large/428/5_r/6000195494285_R.jpg')

# ==============================
# download and read CSV files from web and save it as a CSV file

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=10&e=27&f=2014&g=d&a=2&b=27&c=2014&ignore=.csv'

def download_stock_data(csv_url):
    response = urllib.request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    # turn the file into a list of rows
    lines = csv_str.split("\\n")
    # name of the file to be saved
    dest_url = r'goog.csv'
    # open file in wrtinig mode
    fx = open("Files/"+ dest_url, "w")
    # write to it row by row
    for line in lines:
        fx.write(line + "\n")
    # close the file
    fx.close()

download_stock_data(goog_url)






