# Riot API Basics: Using the Riot API to get Doublelift's Encrypted Summoner ID
Lets talk about the Riot API. Basically, Riot is awesome and they have given us an API that lets developers get data related to League of Legends.

Want to get all of the games that Faker lost in SoloQ? Want to make op.gg? Want to automatically text your friend to "get gud" when she is on a losing streak? Want to create a Discord Bot that you and your friends can use to see who's won the most ranked games this week?

This is all possible with the Riot API :).

Lets hop in!

## Riot API Key
In order to use the Riot API, you need a *key*. This is how Riot secures access to their API so a bunch of crazy people can't use their API like a billion times a second to DDoS them and bring down their servers.

Head over to https://developer.riotgames.com/.

Login with your League of Legends account.

You will be taken to your Riot Developer Dashboard. Scroll down. See on the left where it says "DEVELOPMENT API KEY". Click the red "Show" button. That's your API Key! Copy it and save it somewhere.

***Important Note**: This key expires every 24 hours. That means very 24 hours you will need to regenerate your key by clicking the big red "Regenerate API Key" button at the bottom of the dashboard. If you don't do this, you'll get an error when trying to use the Riot API.*

## Riot API Documentation
The Riot API does A LOT of stuff. I want you to spend *at least 5-10 minutes* browsing through the Riot API documentation. I want you to focus mainly on `Summoner-V4` and `League-V4` (located on the left menu) which are the pieces of the API we're going to be using to get your rank!

Just click around. Click some buttons. Read some stuff. Be curious.

https://developer.riotgames.com/apis

## The Encrypted Summoner ID
So, how the Riot API works is it uses this thing called an `encryptedSummonerId` everywhere. This is just a bunch of letters and numbers that represent a persons summoner name. 

OK.

So the very first thing we need if we want to get Doublelift's rank is his `encryptedSummonerId`.

How the heck do we get that...?

Go to the the documentation [here](https://developer.riotgames.com/apis#summoner-v4) for the route `/lol/summoner/v4/summoners/by-name/{summonerName}`. 

You'll see that right at the beginning it tells you what this API route will return. It says: *Return value: SummonerDTO*. If you scroll down more you can see this big table that tells you *exactly* what *SummonerDTO* is and descriptions of everything as well. 

Very convenient :). We get back stuff like `profileIconId`, `summonerLevel`, and `id`. 

In this case, pay close attention to the description of `id`: *"Encrypted summoner ID. Max length 63 characters"*. 

That's exactly what we need!

Cool. So now we know this is the right Riot API route we want to use. How do we actually use it?

## Get Doublelift's Encrypted Summoner ID
Within the documentation for `/lol/summoner/v4/summoners/by-name/{summonerName}`, scroll down to "Path Parameters". 

Here Riot tells you exactly what it needs for this API route. This route requires you to give it a `summonerName`. Go ahead and type in `Doublelift` in the box. 

*Note: For "Select Region to Execute Against" be sure `NA1` is chosen since Doublelift is an NA player.*

Then, click the big red "Execute Request" button. Lets see if it worked!

Scroll down. Under "Response Code", you should see `200`. This means everything went well :).

Scroll down to "Response Body". Here you should see the values for a bunch of stuff like `profileIconId` and `summonerLevel`. Also, right there next to `id` we can see what Doublelift's encrypted summoner id is! Note this down somewhere.


## The URL

Scroll back up to where you can see the "Request URL". It'll look like this:
`https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Doublelift`

I really want you to understand this URL. First, lets understand the "domain" which is `na1.api.riotgames.com`. Riot uses different domains for different regions. For example, if you wanted to get data for a user playing on the Korean servers, you'd use the domain `kr.api.riotgames.com`. In this case we use `na1` since Doublelift plays on NA servers. 

Then we have `/lol/summoner/v4/summoners/by-name/`. This is the route, also sometimes called the path. Riot's API has *many* different paths that do many different things. This is the path that lets us pass a persons summoner name and get back some basic data, like their `encryptedSummonerId`!

## Get the Encrypted Summoner ID w/ Python
Time for the easy part :).

Open up VSCode and run this code:

    import requests
    summoner_name = "Doublelift"
    riot_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    my_api_key = "INSERT_YOUR_API_KEY_HERE"

    response = requests.get(riot_url + summoner_name, params={"api_key": my_api_key})
    riot_json = response.json()
    print(riot_json)

This code will hit the Riot API and print out the response from the API.

This code is actually not very easy to understand for someone new to coding. But, I think if you go through it slowly line by line, you'll start to *sorta* understand it and that's good enough :).

At the end of program, try adding this line as well and see what it prints out!

    print("Just the encryptedSummonerId", riot_json['id])






