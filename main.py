import requests
from bs4 import BeautifulSoup


def main():
    # the target we want to open
    url = "http://filii.be/pledgeboard/ranking.php"

    # open with GET method
    resp = requests.get(url)

    # http_respone 200 means OK status
    if resp.status_code == 200:
        print("Successfully opened the web page")
        print("The ranking is as following:-\n")

        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, "html.parser")

        # l is the list which contains all the text i.e news
        l = soup.find("table")

        # now we want to print only the text part of the anchor.
        # find all the elements of a, i.e anchor
        for i in l.findAll("a"):
            print(i.text)
    else:
        print("Error")


if __name__ == "__main__":
    main()
