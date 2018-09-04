## :grin: __Application name: :computer: NEWSHIGHLIGHT  :computer:__ :grin:

## __Author: BRIGHTON ASUMANI__


### __HOW THE APPLICATION WORKS__
1. The user to install the virtual environment.Our application has to be created inside our application please [plase read more on the environment](http://flask.pocoo.org/docs/1.0/installation/)
2. We use pip or pip3 to install all the flask modules like eg ***pip install flask***
3. if you want to push it on github please consider ignoring the virtual and python files e.g. virtual/ and \*pyc
4. the application might have alot of erros while creating it:
                * urllib error. this can be either your routing or your requests
                * Bad Request 400
                * 401 an authorized check on your api_key and secret key
                * 404 file will not be found... so you check your routing
                * 500 internal server error. check on your manage.py if it has a problem
5. to run the application you can use python3.6 manage.py server or ./start
    > ***python3.6 manage.py server*** you have to be exporting the secret key and the api_key each time you run this command. so since this can be hectic i prefer you copy the API_KEY and the SECRET_KEY to the ***start.sh*** file and also add  ***python3.6 manage.py server*** and use __./start.sh__.
    > **You have to activate this by running the following command in CL __chmod a+x start.sh__**

### __DESCRIPTION__
> News highlights is a simple flask  application that allows the
> users to see top-headlines, everything and sources.
> A user is able to read the displayed headlines.
> A user can also click any of the preferred choices of the sources e.g. ABC-NEWS,BBC SPORT, BBC NEWS etc.
> The application helps one to read the top headlines of any sources selected
> if one is not satisfied he can click on the ***view site*** button to go to the main site

***



### __TECHNOLOGIES USED__
> 1. PYTHON3.6.6
> 2. HTML 5
> 3. CSS
> 4. JAVASCRIPT
> 5. FLASK
> 6. BOOTSTRAP



### __SCALABILITY__
> For future purposes the application will be able to create an account
        > * create a profile to that account
        > * comment on the news
        > * post his/her on news


***
### __DEPLOYMENT TO HEROKU__
1. heroku create <name-of-app>
2. heroku config:set MOVIE_API_KEY=<YOUR MOVIE API>
3. heroku config:set SECRET_KEY=<YOUR SECRET KEY>
4. git add .
5. git commit -m "deployment to heroku"
6. git push heroku master

***__PLEASE CHECK OUT THE REQUIREMENTS IN THE REQUIREMENTS.TXT FILE__ AND THE SPECS.MD FOR MORE DETAILS TO THIS APPLICATION***
