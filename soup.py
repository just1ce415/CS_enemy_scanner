from bs4 import BeautifulSoup
import requests
import cloudscraper


def site_parsing(link: str):
    """"""
    site = requests.get(link)
    scraper = cloudscraper.create_scraper()
    with open(
        "site.html",
        "wb",
    ) as file:
        file.write(scraper.get(link).content)
    with open("site.html") as file:
        soup = BeautifulSoup(file, features="html.parser")
    return soup


def get_nickname(soup: object):
    """"""
    title_lst = str(soup.title).split(" ")
    nickname = " ".join(title_lst[15:-12])  # CONSTANT NUMBER
    return nickname


def get_rank(soup: object):
    """"""
    rank_str = str(list(soup.find_all("img"))[1])
    rank = rank_str.split("/")[5]
    if rank == "images":
        rank_str = str(list(soup.find_all("img"))[2])
        rank = rank_str.split("/")[5][:2]
    else:
        rank = rank[:2]
    if rank[-1] == ".":
        rank = rank[0]
    return rank


def get_kd_adr(soup: object):   # ANOTHER FUNCTION FOR KD, ADR
    """"""
    info_str = str(soup.find_all("meta", property="og:description"))
    info = info_str.split(">")[0].split(" ")[1:-1]    # CONSTANT CHAR
    win_rate = info[0][-3:]
    kpd = info[1][-4:]    # 46, 47, 48 ???
    hltv_kpd = info[2][-4:]
    hs_rate = info[3][-3:]
    adr = ""
    param = 0
    for i in range(len(info[4])):
        if (info[4][i] == ":") and (not param):
            param = 1
        elif info[4][i] == "\\":
            break
        elif param:
            adr += info[4][i]
    return (win_rate, kpd, hltv_kpd, hs_rate, adr)


def most_kills(soup: object):
    """"""
    info_str = str(soup.find_all("tr", "p-row"))
    pass


if __name__ == "__main__":
    link_1 = "https://csgostats.gg/player/76561198880579276"
    link_2 = "https://csgostats.gg/player/76561198138567105"
    link_3 = "https://csgostats.gg/player/76561198342173972"
    link_4 = "https://csgostats.gg/player/76561198161618188"

    print(get_nickname(site_parsing(link_1)))
    print(get_rank(site_parsing(link_1)))
    print(get_kd_adr(site_parsing(link_1)))
    print(most_kills(site_parsing(link_1)))

    print(get_nickname(site_parsing(link_2)))
    print(get_rank(site_parsing(link_2)))
    print(get_kd_adr(site_parsing(link_2)))
    print(most_kills(site_parsing(link_2)))

    print(get_nickname(site_parsing(link_3)))
    print(get_rank(site_parsing(link_3)))
    print(get_kd_adr(site_parsing(link_3)))
    print(most_kills(site_parsing(link_3)))

    print(get_nickname(site_parsing(link_4)))
    print(get_rank(site_parsing(link_4)))
    print(get_kd_adr(site_parsing(link_4)))
    print(most_kills(site_parsing(link_4)))
