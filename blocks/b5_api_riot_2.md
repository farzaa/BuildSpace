# Riot API: Make A Program to Get Your Rank
*Note: At this point you should have a Riot API key and understand how to call the Riot API from Python. If you don't, check out previous blocks!*

## Get your Encrypted Summoner ID
Okay. So, first thing we'll need is your personal `encryptedSummonerId`. We already did this in previous block for Doublelift. Now, we'll just need to adjust the code a little for you!

Here was the code from the previous block. Go ahead and run it:

    import requests
    summoner_name = "Doublelift"
    riot_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    my_api_key = "INSERT_YOUR_API_KEY_HERE"

    response = requests.get(riot_url + summoner_name, params={"api_key": my_api_key})
    riot_json = response.json()
    print("Just the encryptedSummonerId", riot_json["id"])

## Some Adjustments
We actually only need to change two things here. The first thing is `summoner_name`. Instead `"Doublelift"`, put your summoner name here.

The second thing is the region. In this case we use `na1.api.riotgames.com` since Doublelift is an NA player. Depending on your server, you need to change this. Here are all the options:

    br1	    br1.api.riotgames.com
    eun1	eun1.api.riotgames.com
    euw1	euw1.api.riotgames.com
    jp1	    jp1.api.riotgames.com
    kr	    kr.api.riotgames.com
    la1	    la1.api.riotgames.com
    la2	    la2.api.riotgames.com
    na1	    na1.api.riotgames.com
    oc1	    oc1.api.riotgames.com
    tr1	    tr1.api.riotgames.com
    ru	    ru.api.riotgames.com

For example, if you play on Brazil's servers you'd use `br1.api.riotgames.com`.

Once you make the adjustments, run the code and get your `encryptedSummonerId` :).

## Get Your Rank
Often the hardest part about using the Riot API is actually figuring out what route to use because there are like 50 routes. 

In this case, I'll help you out! The path we're going to be using to get someone's rank is `/lol/league/v4/entries/by-summoner/{encryptedSummonerId}`. Read the documentation for it [here](https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntriesForSummoner). 

Spend some time reading the documentation for this path. What does it need as input? What does it output?

Spent a little bit of time reading the docs?

Okay cool. Scroll down to "Path Parameters". You'll see that this route needs an `encryptedSummonerId`. You have that! Copy paste it here. Then, be sure to change the region under "Select Region to Execute Against" to the region your account is in. Then click "Execute Request". If you see `200` under "Response Code", it worked! Scroll down to "Response Body" to check out your data :).

## Get Your Rank in Python
Delete all the code you have right now. We need to restructure our code a lot for this or else things are going to get super messy.

In order us to get our rank here's what we need to do:

1. Make a request to `lol/summoner/v4/summoners/by-name/{summonerName}`.
2. Parse this response and get the `encryptedSummonerId` and save it to a variable.
3. Make a request to `/lol/league/v4/entries/by-summoner/{encryptedSummonerId}`.
3. Parse the response and get the `rank`.

Let me show you how it's done :)! First, lets set things up with some variables:

    import requests

    my_region_code = "INSERT_YOUR_REGION_CODE_HERE"
    my_summoner_name = "INSERT_YOUR_SUMMONER_NAME_HERE"
    my_api_key = {"api_key": "INSERT_YOUR_API_KEY_HERE"}

*Please* be sure that you enter your region code correctly here. Scroll up where I listed all of them to double check that you wrote it properly!

Next, lets make some more variables for the two paths we're going to be using.

    import requests

    my_region_code = "INSERT_YOUR_REGION_CODE_HERE"
    my_summoner_name = "INSERT_YOUR_SUMMONER_NAME_HERE"
    my_api_key = {"api_key": "INSERT_YOUR_API_KEY_HERE"}

    path_to_get_encrypted_id = "lol/summoner/v4/summoners/by-name/"
    path_to_get_rank = "/lol/league/v4/entries/by-summoner/"

Now lets neatly create the full URL that will get our rank. 
    import requests

    my_region_code = "INSERT_YOUR_REGION_CODE_HERE"
    my_summoner_name = "INSERT_YOUR_SUMMONER_NAME_HERE"
    my_api_key = {"api_key": "INSERT_YOUR_API_KEY_HERE"}

    path_encrypted_id = "lol/summoner/v4/summoners/by-name/"
    path_rank = "lol/league/v4/entries/by-summoner/"

    full_url_to_get_encrypted_id = 
    "https://" + my_region_code + ".api.riotgames.com/" + path_encrypted_id + my_summoner_name

Okay this looks a little complex and I promise it's not. So, we created a new variable called `full_url_encrypted_id` and I *built up the URL* by using a bunch of variables. You'll see why in a moment!

First, lets go ahead and get our `encryptedSummonerId`.

    import requests

    my_region_code = "INSERT_YOUR_REGION_CODE_HERE"
    my_summoner_name = "INSERT_YOUR_SUMMONER_NAME_HERE"
    my_api_key = "INSERT_YOUR_API_KEY_HERE"

    path_encrypted_id = "lol/summoner/v4/summoners/by-name/"
    path_rank = "lol/league/v4/entries/by-summoner/"

    full_url_to_get_encrypted_id = 
    "https://" + my_region_code + ".api.riotgames.com/" + path_encrypted_id + my_summoner_name

    response = requests.get(full_url_to_get_encrypted_id, params=my_api_key)

    my_encrypted_id = response.json()["id"]
    print("Got my encrypted id:", my_encrypted_id)

Okay, nothing new here. Now lets create the URL to get your rank.

    import requests

    my_region_code = "INSERT_YOUR_REGION_CODE_HERE"
    my_summoner_name = "INSERT_YOUR_SUMMONER_NAME_HERE"
    my_api_key = "INSERT_YOUR_API_KEY_HERE"

    path_encrypted_id = "lol/summoner/v4/summoners/by-name/"
    path_rank = "lol/league/v4/entries/by-summoner/"

    full_url_to_get_encrypted_id = 
    "https://" + my_region_code + ".api.riotgames.com/" + path_encrypted_id + my_summoner_name

    response = requests.get(full_url_to_get_encrypted_id, params=my_api_key)

    my_encrypted_id = response.json()["id"]
    print("Got my encrypted id:", my_encrypted_id)

    full_url_to_get_rank = "https://" + my_region_code + ".api.riotgames.com/" + path_rank + my_encrypted_id

Notice how I used `my_encrypted_id` to create `full_url_to_get_rank`. Now, lets get your rank:

    import requests

    my_region_code = "INSERT_YOUR_REGION_CODE_HERE"
    my_summoner_name = "INSERT_YOUR_SUMMONER_NAME_HERE"
    my_api_key = {"api_key": "INSERT_YOUR_API_KEY_HERE"}

    path_encrypted_id = "lol/summoner/v4/summoners/by-name/"
    path_rank = "lol/league/v4/entries/by-summoner/"

    full_url_to_get_encrypted_id = 
    "https://" + my_region_code + ".api.riotgames.com/" + path_encrypted_id + my_summoner_name

    response = requests.get(full_url_to_get_encrypted_id, params=my_api_key)

    my_encrypted_id = response.json()["id"]
    print("Got my encrypted id:", my_encrypted_id)

    full_url_to_get_rank = "https://" + my_region_code + ".api.riotgames.com/" + path_rank + my_encrypted_id

    response = requests.get(full_url_to_get_rank, params=my_api_key)
    my_rank = response.json()['rank']

    print("My rank is:", my_rank)


That's it! Run it :).








