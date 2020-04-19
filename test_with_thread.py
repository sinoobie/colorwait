from threading import Thread

import warna
from warna import pelangi

t1=Thread(target=pelangi, args=("LOADING",None,2))
t1.start()

def do():
        import requests
        r=requests.get('https://nuubi.herokuapp.com') #do something
        warna.stop=True
        return r
run=do()
print(run)
