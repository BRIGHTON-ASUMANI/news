**__SPECIFICATIONS__**
1. Python language used.**flask**
2. Creation on Ubuntu 16.04
3. Uses python tool called pip or pip3
4. This application uses the heroku master application structure
5. API-key and Base_url required for requesting
6. When pushing to heroku one is required to have an  account to heroku [heroku account](heroku.com)
7. Heroku CLI pages [HEROKU CLI](https://devcenter.heroku.com/articles/heroku-cli)
8. virtual environment installing ***sudo apt-get install pytho3.6-venv***
9. Gunicorn this helps in hosting our application to Heroku ***python3.6 -m  pip install gunicorn***
10. Two base urls used in the request:
            * CATEGORY_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
            * NEWS_API_BASE_URL ='https://newsapi.org/v2/{}?apiKey={}&language=en'



**__FEATURES__**
1. User is able to read latest news headlines... including the top headlines in each source
2. User is able to view various news sources like ABC, CNN, BBC etc. They can either visit the site or just view the top headlines
3. User is able to view top-headlines and articles.
4. Articles display images while sources are links

***__PLEASE CHECK OUT THE REQUIREMENTS IN THE REQUIREMENTS.TXT FILE__***
