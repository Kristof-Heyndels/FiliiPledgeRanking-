import requests
from bs4 import BeautifulSoup

schachten = [
    "alex",
    "amber",
    "anna",
    "bram a",
    "bram b",
    "brecht",
    "fabio",
    "gijs",
    "glen",
    "jimmy",
    "katrien",
    "kobe",
    "kristof",
    "lies",
    "lode",
    "louis",
    "maja",
    "marie",
    "martijn",
    "michiel c",
    "michiel l",
    "nathan",
    "nicholas",
    "pieter",
    "pieter-jan",
    "jurre",
    "quinten",
    "robbe",
    "robin",
    "seppe",
    "sophie",
    "stan",
    "stef",
    "tom c",
    "tom g",
    "toon j",
    "toon l",
    "yarne",
]


def main():

    url = "http://filii.be/pledgeboard/index.php"
    resp = requests.get(url)

    # http_respone 200  == OK
    if resp.status_code == 200:
        print("FILII LAMBERTI schachten pledgeranking:-\n")

        soup = BeautifulSoup(resp.text, "html.parser")
        html = soup.find("div", {"id": "container"})

        score = 0
        for schacht in schachten:
            for i in html.findAll("a"):
                score += i.text.lower().count(schacht.lower())
            print(schacht + ": " + str(score))
            score = 0

    else:
        print("Error")


if __name__ == "__main__":
    main()
