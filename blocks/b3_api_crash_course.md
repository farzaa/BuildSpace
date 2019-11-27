# Crash Course on APIs + Python

An API is a thing that allows applications to communicate with each other.

Think about when you search for something on Google. Your browser is **Application #1**. Google's servers are **Application #2**. How does Application #1 communicate with Application #2?

Through an API :).

Basically, Google has given *everyone* access to their Search API. The Search API is Google's magic. It's the thing Google made that allows you to type in a search query and get back a bunch of results for websites!

**For example**, when you Google the word "Tesla", what happens? Well:
1. Your browser will take the word "Tesla" and send it to Google's Search API which lives on Google's servers.
2. Once we arrive on Google's servers, Google's Search API will take the word "Tesla" and scan it's database for websites that relate to the word "Tesla".
3. Once that's done, the Search API will send a message BACK to your browser saying "here you go, these are the websites that relate to Tesla". 
4. Your browser will take the results and display it for you. 


Read through that again if it didn't quite make sense.

## Python Setup for APIs
We are going to install a tool called `requests` which allows us to easily call an API from Python.

To do this, go to VS Code, go to your terminal, and within the terminal type in `pip install requests`. If it worked, you should see the words "Successfully installed" somewhere in there near the end. 

What did we do? Well, we installed a Python **package** called `requests`. This is always a weird thing to explain so I'm not going to right now. You'll see!

## Call an API
Lets call an API without writing any code. Go to your browser and go to this website:

`http://farza.party/ping`

You should see this on your screen

`{"response":"pong"}`

Okay. So what's happening here? You just talked to my API!

So, `http://farza.party` is my personal website. I've created a special route on the website called `/ping` that will automatically just return a `response` with the word `pong`. This is a super simple API.

Lets complicate it a little. 

Go to:

`http://farza.party/hello?name=Obama`

This gives us:

`{"response":"Hello Obama"}`

This is another route I made called `/hello`. It requires you to send a `name` along with your request. It'll take that `name` and say "Hello"! 

Try and go to:

`http://farza.party/hello`

You'll get an error! It requires you to send a `name`.

In this case, `name` is what we call a **query parameter**. This is important! A query parameter is like supporting data you send to an API so the API can do things that are more intresting.

Just going to `/ping` is pretty boring because it always gives back the same thing.

But, `/hello` is a but more interesting because it can actually take a `name` and actually use it!

## Call an API from Python
Go ahead and write this code:

    import requests
    my_query_parameters = {"name": "Obama"}
    r = requests.get("http://farza.party/hello", params=my_query_parameters)
    print(r.json())


Okay, so a lot is happening here.
1. Remember how we installed the `requests` package? Well, if we want to use it we need to `import` it.
2. Set up our query parameters with a variable called `my_query_parameters`.
3. Use `requests` to call the API. 
4. Print out the response.

When you run this you'll see in the terminal you get:

`{"response":"Hello Obama"}`

Congrats, you just called an API from Python :).

I want you to figure out whatever it is you think is confusing here. Wtf is `.json()`? How does `params=` work? Try breaking the program. Mess with it. Get errors. Google your questions. 

You can also join the Discord where I'll be happy to help!

