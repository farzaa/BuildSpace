import requests

my_region_code = "na1"
my_summoner_name = "a wildturtle"
my_api_key = {"api_key": "RGAPI-9360f237-4f81-4017-84b1-f3b1ea0f234c"}

path_encrypted_id = "lol/summoner/v4/summoners/by-name/"
path_rank = "lol/league/v4/entries/by-summoner/"

full_url_to_get_encrypted_id = "https://" + my_region_code + ".api.riotgames.com/" + path_encrypted_id + my_summoner_name

response = requests.get(full_url_to_get_encrypted_id, params=my_api_key)

my_encrypted_id = response.json()["id"]
print("Got my encrypted id:", my_encrypted_id)

full_url_to_get_rank = "https://" + my_region_code + ".api.riotgames.com/" + path_rank + my_encrypted_id

response = requests.get(full_url_to_get_rank, params=my_api_key)
rank_data = response.json()
print(rank_data)