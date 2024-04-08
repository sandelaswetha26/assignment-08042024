import requests
import re
from flask import Flask

url = 'https://time.com'

headline_pattern = re.compile(r'<h3 class="latest-stories__item-headline">(.*?)</h3>', re.DOTALL)
href_pattern = re.compile(r'<li class="latest-stories__item">\n              <a href=(.*?)>', re.DOTALL)

app = Flask(__name__)

def get_time_data():
    response = requests.get(url)
    headlines = headline_pattern.findall(response.text)
    links = href_pattern.findall(response.text)
    data = []
    for title, link in zip(headlines, links):
        data.append({'title': title, 'link': url + link.strip('"')})
    return data

@app.route('/getTimeStories', methods=['GET'])
def get_time_stories():
    return get_time_data()

if __name__ == '__main__':
    app.run(debug=True)
