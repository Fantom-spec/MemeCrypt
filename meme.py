import requests
import random

def memegetter():
    meme_keywords = [
    # Classic Memes
    "dank", "trollface", "rage comic", "pepe", "doge", "troll",
    "lolcat", "me gusta", "forever alone", "success kid", "grumpy cat", "bad luck brian",

    # Trending & Internet Culture
    "sus", "skibidi", "rizz", "gyat", "Ohio", "NPC", "sigma", "devious lick",
    "sigma male", "beta", "chad", "girl dinner", "grimace shake", "goofy ahh",
    "you fell off", "brokeboi", "dripped out",

    # Pop Culture
    "baby yoda", "shrek", "marvel", "barbenheimer", "cillian murphy", "breaking bad",
    "walter white", "spiderman", "anime", "naruto", "one piece", "netflix",

    # Meme Phrases
    "hard to swallow pills", "no thoughts head empty", "why are you booing me",
    "modern problems require modern solutions", "change my mind", "hold up wait a minute",
    "is this a pigeon", "I understood that reference", "they don’t know", "guess I’ll die",

    # Intellectual/Ironic
    "crab rave", "galaxy brain", "stonks", "math meme", "engineers",
    "dark humor", "introvert", "anti-joke"]
    while True:
        x=random.choice(meme_keywords)
        url = f"https://api.apileague.com/retrieve-random-meme?keywords={x}"
        api_key = "940d9a5e22c14b0db2bc9446d63dc9b6"
        headers = {
            'x-api-key': api_key
            }
        response = requests.get(url, headers=headers)
        data=response.json()
        link=data.get('url')
        t=data.get('type')
        s=t.split('/')
        if s[0]=="image":
            break

    if response.status_code == 200: 
        if link:
            imgresponse=requests.get(link)
            if imgresponse.status_code==200:
                with open(f"{x}.{s[-1]}","wb") as f:
                    f.write(imgresponse.content)
    return f"{x}.{s[-1]}"