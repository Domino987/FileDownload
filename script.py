from urllib.request import urlopen
from urllib.request import Request
import pathlib
from bs4 import BeautifulSoup as bs
import re
import os


def download_file(dir, url):
    file_name = url.split('/')[-1]

    pathlib.Path('./downloads/'+dir).mkdir(parents=True, exist_ok=True)

    my_file = pathlib.Path('./downloads/'+dir+"/"+file_name)
    if my_file.is_file() or file_name.endswith("txt"):
        print ("Skip: "+file_name)
    else:
        print("Download: "+dir + "/"+file_name)
        try:            
            filedata = urlopen(url)
            datatowrite = filedata.read()
            with open('./downloads/'+dir+"/"+file_name, 'wb') as f:
                f.write(datatowrite)
            pass
        except:
            pass
    return


pathlib.Path('./downloads').mkdir(parents=True, exist_ok=True)

req = Request(
    'https://fsbio.rwth-aachen.de/service/downloads/fach/biotechnologie-msc')
req.add_header(
    'Cookie'
html_page = urlopen(req)

soup = bs(html_page)

links = []
for link in soup.findAll('a', attrs={'href': re.compile("^/service/downloads/fach/")}):
    links.append(link.get('href'))

for link in links:
    req = Request('https://fsbio.rwth-aachen.de'+link)
    print('https://fsbio.rwth-aachen.de'+link)
    req.add_header(
        'Cookie', 'has_js=1; SESS9208fb201b178189fd366303dff7a5d6=rrgllcdssj2tsrvve9v8vqcl84')
    download_html_page = urlopen(req)
    soup = bs(download_html_page)
    for downloadLink in soup.findAll('a', attrs={'href': re.compile("^http://www.fsbio.rwth-aachen.de/sites/default/files/download_files/")}):
        download_file(link.split('/')[-1], downloadLink.get('href'))
