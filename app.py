from flask import Flask , jsonify
import wikipediaapi

app = Flask(__name__)
app.url_map.strict_slashes = False

def get_wiki_data(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')

    page_py = wiki_wiki.page(query)
    if page_py.exists():
        title = page_py.title
        wiki_url = page_py.fullurl
        summary = page_py.summary
    else:
        return query, None, "The Page Uh Looking for Doesn't Exists"
    return title, wiki_url, summary

def get_wiki_data_in_other_lang(lang, query):
    wiki_wiki = wikipediaapi.Wikipedia(lang)

    page_py = wiki_wiki.page(query)
    if page_py.exists():
        title = page_py.title
        wiki_url = page_py.fullurl
        summary = page_py.summary
    else:
        return query, None, "The Page Uh Looking for Doesn't Exists"
    return title, wiki_url, summary 

@app.route('/')
def home():
    return "Hey There! Wikipedia Api Is Functional"

@app.route('/<searchitem>')
def wiki(searchitem):
    title, url, summary = get_wiki_data(searchitem)
    return jsonify({"query": searchitem,"title": title, "Wikipedia_URL": url, "Summary": summary})

@app.route('/<lang>/<searchitem>')
def wiki_in_otherlang(lang, searchitem):
    title, url, summary = get_wiki_data_in_other_lang(lang, searchitem)
    return jsonify({"query": searchitem,"title": title, "Wikipedia_URL": url, "Summary": summary, "Language": lang})   

if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0",port=5000)    
