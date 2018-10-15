import os
import pathlib
import re
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as bs


def download_file(dir, url):
    file_name = url.split("/")[-1]

    pathlib.Path(f"./downloads/{dir}").mkdir(parents=True, exist_ok=True)

    my_file = pathlib.Path(f"./downloads/{dir}/" + file_name)
    if my_file.is_file() or file_name.endswith("txt"):
        print(f"Skip: {file_name}")
    else:
        print(f"Download:  {dir}/{file_name}")
        try:
            filedata = urlopen(url)
            datatowrite = filedata.read()
            with open(f"./downloads/{dir}/{file_name}", "wb") as f:
                f.write(datatowrite)
            pass
        except:
            pass
    return


pathlib.Path("./downloads").mkdir(parents=True, exist_ok=True)

req = Request("https://fsbio.rwth-aachen.de/service/downloads/fach/biotechnologie-msc")

req.add_header("Cookie", "")
html_page = urlopen(req)

soup = bs(html_page)


links = [
    link.get("href")
    for link in soup.findAll(
        "a", attrs={"href": re.compile("^/service/downloads/fach/")}
    )
]

for link in links:
    req = Request(f"https://fsbio.rwth-aachen.de{link}")
    print(f"https://fsbio.rwth-aachen.de{link}")
    req.add_header(
        "Cookie",
        "has_js=1; SESS9208fb201b178189fd366303dff7a5d6=rrgllcdssj2tsrvve9v8vqcl84",
    )
    download_html_page = urlopen(req)
    soup = bs(download_html_page)

    file_list = soup.findAll(
        "a",
        attrs={
            "href": re.compile(
                "^http://www.fsbio.rwth-aachen.de/sites/default/files/download_files/"
            )
        },
    )
    for downloadLink in file_list:
        download_file(link.split("/")[-1], downloadLink.get("href"))
