######################## BeautifulSoup ########################
# given a url, download every link available on that page
from PIL import Image
import operator
import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://mihandownload.com/page/" + str(page)
        # makes connection to the page and stores the results in the variable
        source_code = requests.get(url)
        # .text gets all of the text out of the source code.(gets rid of javascript/meta/css/...)
        plain_text = source_code.text
        # change the source code to a BeautifulSoup object
        soup = BeautifulSoup(plain_text)
        # soup.findAll  finds an element with a specific attribute inside the object.
        for link in soup.findAll('a', {'rel': 'bookmark'}):
            # .get('href')  gets what is inside the href element
            href = link.get('href')
            # .string gets what is inside the a tag (the text that is inside it)
            title = link.string
            # print(title)
            # print(href)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    # for item_name in soup.findAll('img', {'class': 'aligncenter'}):
    # img_src = item_name.get('src')
    #  print(img_src)
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)


# trade_spider(3)
get_single_item_data("http://mihandownload.com/2014/11/displayfusions-pro.php")

# download text from a web page and get all actual words from that tex
# operator class lets you to work with data types in python.


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class': 'post-title'}):
        content = post_text.string
        # .lower() = lower cases all of the words.
        # .split() = splits all words by space.
        words = content.lower().split()
        # loop through words and save it's items in a list.
        ''' each "words" is list of each_word in each sentence.
         but at the end the words_list becomes a big loop of all of each_words in all "words". (here we have two for loops) '''
        for each_word in words:
            word_list.append(each_word)
    clean_words(word_list)


def clean_words(word_list):
    clean_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_-+='';:\"{}[].,<>|?/"
        for i in range(0, len(symbols)):
            # replace() function replaces something with other thing in a string.
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_list.append(word)
    create_dic(clean_list)


def create_dic(clean_list):
    # dictionary
    word_count = {}
    for word in clean_list:
        # if the word is already available in the word_count.
        if word in word_count:
            # word_count[key] = value.
            word_count[word] += 1
        else:
            word_count[word] = 1
    # sorting the dictionary based on numerical values, we loop through our dic.
    ''' sorted() gets what we want to sort, here it is the dictionary items and second parameter is name key
    (different with key,value)that get the way we want to sort out(by key items or value items). operator.itemgetter(0)
    sorts by key and operator.itemgetter(1) sorts by value. '''
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, " : ", value)


start("https://www.thenewboston.com/forum/")

# PIL library to work with pictures in python :
# how to open a image and save it in an Image class object.
img = Image.open("bobby.jpg")
# img.size = width and height of the image in a topple (w, h).
print(img.size)
# img.format = format of the image.
print(img.format)
# shows the image in your
img.show()
