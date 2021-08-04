# Import Spliter, BeautifulSoup, Webdriver and Pamdas
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_all():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_para = mars_news(browser)

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_para,
        "featured_image": featured_image(browser),
        "facts": mars_facts(browser),
        "hemispheres": hemispheres(browser)
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data



def mars_news(browser):
    # Go to MARS Planet Scince website https://redplanetscience.com
    url = "https://redplanetscience.com/"
    browser.visit(url)
    time.sleep(1)

    # Get the full html from the page & convert in to a soup object
    html = browser.html
    news_soup = bs(html, 'html.parser')

    # Get the required div, the tags by inspecting the website
    tags = news_soup.select_one('div.list_text')

    # Save the title & the body to variables
    news_title = tags.find('div', class_='content_title').get_text()
    news_p = tags.find('div', class_='article_teaser_body').get_text()

    return news_title, news_p


def featured_image(browser):
    # Go to MARS images website https://spaceimages-mars.com
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    time.sleep(1)

    # Get the full html from the page & convert in to a soup object
    html = browser.html
    images_soup = bs(html, 'html.parser')

    # Get the required div, the tags by inspecting the website
    tags = images_soup.select('div.header')

    # get image and append the main url
    image = images_soup.find('img', class_='headerimage fade-in').get('src')
    featured_image_url = url + image

    return featured_image_url


def mars_facts(browser):
    # Go to MARS facts website https://galaxyfacts-mars.com/
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)
    time.sleep(1)

    # Get the full html from the page & convert in to a soup object
    html = browser.html
    images_soup = bs(html, 'html.parser')

    # read table 1 in to a dataframe
    mars_facts_df =  pd.read_html(url)[0]

    # clean up the heading
    mars_facts_df.columns=['Description','Mars','Earth']
    mars_facts_clean_df = mars_facts_df.iloc[1:]

    return mars_facts_clean_df.to_html()



def hemispheres(browser):
    # ### Mars Hemispheres
    # base url
    url = "https://marshemispheres.com/"

    # ##### cerberus
    # Go to MARS facts website https://marshemispheres.com/cerberus.html
    cerberus_url = url + "cerberus.html"
    browser.visit(cerberus_url)
    time.sleep(1)

    # Get the full html from the page & convert in to a soup object
    html = browser.html
    images_soup = bs(html, 'html.parser')

    # get image and append to base url
    image = images_soup.find('img', class_='wide-image').get('src')
    cerberus_image_url = url + image


    # ##### Schiaparelli
    # Go to MARS facts website https://marshemispheres.com/schiaparelli.html
    schiaparelli_url = url + "schiaparelli.html"
    browser.visit(schiaparelli_url)
    time.sleep(1)

    # Get the full html from the page & convert in to a soup object
    html = browser.html
    images_soup = bs(html, 'html.parser')

    # get image and append to base url
    image = images_soup.find('img', class_='wide-image').get('src')
    schiaparelli_image_url = url + image


    # ##### Syrtis Major
    # Go to MARS facts website https://marshemispheres.com/syrtis.html
    syrtis_url = url + "syrtis.html"
    browser.visit(syrtis_url)
    time.sleep(1)

    # Get the full html from the page & convert in to a soup object
    html = browser.html
    images_soup = bs(html, 'html.parser')

    # get image and append to base url
    image = images_soup.find('img', class_='wide-image').get('src')
    syrtis_image_url = url + image


    # ##### Valles Marineris
    # Go to MARS facts website https://marshemispheres.com/valles.html
    valles_url = url + "valles.html"
    browser.visit(valles_url)
    time.sleep(1)

    # Get the full html from the page & convert in to a soup object
    html = browser.html
    images_soup = bs(html, 'html.parser')

    # get image and append to base url
    image = images_soup.find('img', class_='wide-image').get('src')
    valles_image_url = url + image


    # #### Create a dictionary for the image urls
    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": cerberus_image_url },
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_image_url },   
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_image_url },    
        {"title": "Valles Marineris Hemisphere", "img_url": valles_image_url }
    ]

    return hemisphere_image_urls