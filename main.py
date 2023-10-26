import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
PROVIDER = "https://bible-api.com"


@app.get("/")
def root():
    return "Go to /book/chapter/verse/ to get Scripture. eg: /john/3/16/"


@app.get("/{book}/{chapter}/{verse}/", response_class=HTMLResponse)
def read_verse(book: str, chapter: int, verse: str):
    url = f"{PROVIDER}/{book}+{chapter}:{verse}"
    response = requests.get(url)
    data = response.json()
    return """
    <html>
        <head>
            <title>Fast Bible</title>
        </head>
        <body>
            <h1>{verse}</h1>
        </body>
    </html>
    """.format(verse=data.get("text"))
