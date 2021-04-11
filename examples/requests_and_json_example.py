import requests
import json

def get_data_from_steam(profile_link: str) -> object:
    """
    """
    base_url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/"
    api_key = "YOUR_KEY"
    appid = 730
    playerid = profile_link.split("/")[-2]
    search_url = f"{base_url}?appid={appid}&key={api_key}&steamid={playerid}&format=json"
    response = requests.get(search_url)
    json_response = response.json()
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(json_response, file, indent=4)
    return json_response

if __name__ == "__main__":
    get_data_from_steam("https://steamcommunity.com/profiles/76561198880579276/")
