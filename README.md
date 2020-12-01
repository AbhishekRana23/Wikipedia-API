# Wikipedia-API


Api URL = "https://v1wikipediaapi.herokuapp.com/"

Api Supports Two Ways of Interacting with the Api

1) Search with a Term

Api URL = "https://v1wikipediaapi.herokuapp.com/{search_term}"

For The search_term "Youtube"
Api Returns
```json
{
  "Summary": "YouTube is an American online video-sharing platform ......",
  "Wikipedia_URL": "https://en.wikipedia.org/wiki/YouTube",
  "query": "youtube",
  "title": "YouTube"
}
```
2)Search in A Particular Language

Api URL = "https://v1wikipediaapi.herokuapp.com/{language-code}/{search_term}"

For The search_term "Youtube" and language-code "de"

Api Returns 
```json
{
  "Language": "de",
  "Summary": "YouTube (Aussprache [ˈjuːtuːb oder ˈjuːtjuːb]) ist ein 2005 gegründetes Videoportal des US-amerikanischen Unternehmens ....",
  "query": "youtube",
  "title": "YouTube"
}
```

This Was My First Api And Though To Keep It Simple At Start and As i Improvise My Coding Knowledge I Will ComeUp With More Api's And Useful Stuff


### **Installation**:

Clone this repository using
```sh
$ git clone https://github.com/AbhishekRana23/Wikipedia-API
```
Enter the directory and install all the requirements using
```sh
$ pip3 install -r requirements.txt
```
Run the app using
```sh
$ python3 app.py
```
Navigate to 127.0.0.1:5000 to see the Homepage


#### You can fork the repo and deploy on VPS or deploy it on Heroku :3

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cyberboysumanjay/JioSaavnAPI/tree/master)


---
