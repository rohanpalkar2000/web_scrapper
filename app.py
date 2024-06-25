# pip install Flask beautifulsoup4 requests

from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data (example: all paragraphs)
    data = soup.find_all('p')
    paragraphs = [p.text for p in data]

    return render_template('result.html', paragraphs=paragraphs)

if __name__=="__main__":
    app.run(host="0.0.0.0")