# coding: utf-8 
# Introduce wallpaper for your
import random 
import requests

class SimpleDesktop(object):
    def __init__(self):
        self.url = "http://simpledesktops.com/browse/"+random.randint(1,50)+"/"
    
    def create_reply(self):
        r = requests.get(self.url,verify=False)
        html = r.text
        soup = BeautifulSoup(html,'html.parser')
        try:
            imgs = soup.find_all('img')
            img_url = img[random.randint(0,len(imgs))]['src']
            text = re.search('(http://static.simpledesktops.com/uploads/desktops/\d+/\d+/\d+/(.*?png)).*?png',img_url)
            new_img_url = text.group(1)
            img_content = requests.get(new_img_url,verify=False)
            img_name = text.group(2)
            path = "images/"+ img_name
            with open(path,'rb') as f:
                f.write(img_content.content)
            
        except Exception as e:
            path = None
        
        return path 

