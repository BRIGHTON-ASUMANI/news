from flask import render_template
from . import main
from ..request import get_articles,get_sources,get_from_source,get_categories


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting articles and sources

    articles = get_articles('top-headlines')
    # print(get_articles)

    # sources = get_sources('sources')
    business = get_categories('business')
    general = get_categories('general')
    health = get_categories('health')
    sports = get_categories('sports')
    technology = get_categories('technology')
    science = get_categories('science')
    # print(get_sources)
    title = 'news'
    return render_template('index.html', title = title,articles = articles,sports = sports,business = business,general = general,health = health, ports = sports,technology = technology,science = science)

@main.route('/source/<src>')
def source(src):
    articles = get_from_source('top-headlines',src)
    # print(get_articles)
    sources = get_sources('sources')
    # print(get_sources)
    title = 'news'
    return render_template('news.html', title = title,articles = articles,sources = sources)



@main.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
