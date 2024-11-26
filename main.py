from requests import *
import requests

headers = []
#URL: "https://cdn77-vid-mp4.xnxx-cdn.com/c5Kel2cjO5zPrqEtoF2izw==,1731329827/videos/mp4/d/9/1/xvideos.com_d91acdf929d8b11e5ff4b3de0dc9ac9b.mp4?download=XNXX__-_alex_adams_360p.mp4"

s= requests.session()
data = {"LOGGED":'false',
        "EMAIL_VERIFIED":'true',
        "MP4HD_AVAILABLE":'false',
        "MP4_4K_AVAILABLE":'false',
        "URL": 'true',
        "URL_LOW": 'true'
      }


url = 'https://www.xnxx-ru5.com/video-vfel50d/_-_alex_adams'
r = s.get(url, json=data)
print(r.status_code)
print(r.content)78974331



