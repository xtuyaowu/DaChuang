import os
import urllib.request
from static.py.sse import getUrls


def getpdf():
    urls = getUrls.getUrls('2018-3-1', '2018-3-30', 5)
    for url in urls:
        file_name = url.split('/')[-1]
        u = urllib.request.urlopen(url)
        path = '../../report/sse/' + file_name
        if not os.path.exists(path):
            f = open(path, 'wb')
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break
                f.write(buffer)
            f.close()
            print("Sucessful to download" + " " + file_name)

getpdf()
