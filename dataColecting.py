import requests
from bs4 import BeautifulSoup


def get_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    list2 = soup.find_all("div", {"class": "col-lg-6"})
    for i in list2:
        for link in i.findAll("a"):
            my_link = link.get("href") + "\n"
            new_link = "{}{}".format('https://milligazete.com.tr/' + my_link)

            with open("links.txt", "a", encoding="uft-8") as file:
                file.write(new_link)

def get_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    category = soup.find("container", {"class": "breadcrumb_link text-dark"}).getText("a")
    date = soup.find("time", {"class": "fw-bold"}).getText("time")
    date = date.split("-")[0]

    title = soup.find("h1").getText("h1")

    content = soup.find_all("div", {"class": "article-text container-padding"}).find_all("p")
    conText = ""
    for p in content:
        conText += p.getText()

    print(date)
    print(title)
    print(url)
    print(conText)
    last = "{} ; {} ; {} ; {} ; {}".format(url, category, date, title, conText)

    with open("Contents.txt", "a", encoding="uft-8") as file:
        file.write(last + "\n")

    f = open("links.txt")
    for i in range(8):
        try:
            link = f.readline()
            get_content(link.strip())
        except:
            pass
