import shutil
import requests

class ImageGet():
    def __init__(self, url, name):
        self.image_url = url
        self.filename = name

    def Dowload(self):
        r = requests.get(self.image_url, stream = True)

        if r.status_code == 200:
            r.raw.decode_content = True
            
            with open(self.filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',self.filename)
        else:
            print('Image Couldn\'t be retreived')