from bs4 import BeautifulSoup
import requests
import sys

url = sys.argv[1]
endstring = "user.php"
finished = False

while finished == False:

    result = requests.get(url)
    soup = BeautifulSoup(result.content,"html.parser")

    element_by_id = soup.find("a",{"id":"next_url"})
    
    if endstring in url:
        finished = True
    else:
        next_image = element_by_id.get("href")
        find_image = element_by_id.find("img")
        current_image = find_image.get("src")
        
    url = "https://imgsrc.ru"+next_image
    dl_image = "https:"+current_image

    if finished == True:
        break

    image_name = dl_image.split("/")[-1]

    response = requests.get(dl_image)
    if response.status_code:
        fp = open(image_name, 'wb')
        fp.write(response.content)
        fp.close()