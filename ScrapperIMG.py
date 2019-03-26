from selenium import webdriver
import os
import urllib
import urllib.request


def init_file(researched):
    path = os.getcwd()
    path += "/out/"

    os.makedirs(path, exist_ok=True)

    path += researched + "/"

    if os.path.isdir(path):
        cmd = "rm -rf " + path
        os.popen(cmd + ' 2>&1', 'r')

    os.makedirs(path, exist_ok=True)
    return path


def scrapper(nbImage, researched, path):
    chrome_options = webdriver.ChromeOptions
    #chrome_options.add_argument("headless")
    #driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome('/usr/bin/chromedriver')

    i = 0
    page = 1
    while i < int(nbImage):
        url = 'https://www.shutterstock.com/fr/search/' + researched + '?site=image&page=' + str(page)
        print("Search on : " + url)
        driver.get(url)
        images = driver.find_elements_by_tag_name('img')
        if images.__len__() < 2:
            if i == 0:
                print("World not recognize.")
                if os.path.isdir(path):
                    cmd = "rm -rf " + path
                    os.popen(cmd + ' 2>&1', 'r')
                driver.close()
                return
            else:
                print("Only " + str(i) + "have been found.")
                driver.close()
                return

        for image in images:
            #print(str(i) + " " + str(nbImage))
            if i > int(nbImage)-1:
                driver.close()
                return
            i += 1
            print("image " + str(i) + " --> " + image.get_attribute('alt') + ", link : " + image.get_attribute('src'))
            urllib.request.urlretrieve(image.get_attribute('src'),
                                   path + image.get_attribute('alt')[:26] + image.get_attribute('src')[-4:])
        page += 1

    driver.close()


researched = input("Entrer le thème des images rechercher (défaut : chien) : \n")
nbImage = input("Entrer le nombre d'image rechercher (défaut : 10) : \n")
path = init_file(researched)

if researched == "":
    researched = "chien"

if nbImage == "":
    nbImage = "10"
scrapper(nbImage, researched, path)
