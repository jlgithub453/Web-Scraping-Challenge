#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[43]:

def init_browser():
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

# In[3]:

def scrape():
    browser = init_browser()
    print(browser)
    listings = {}
# URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'


# In[4]:


    browser.visit(url)


# In[5]:


# Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# In[6]:


    news_title = soup.find('div', class_="content_title").find('a').text


# In[7]:


    print(news_title)


# In[8]:


    news_p=soup.find('div', class_="article_teaser_body").text
    print(news_p)


# In[9]:


    url_2='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


# In[10]:


    browser.visit(url_2)


# In[11]:


    browser.find_by_id('full_image').first.click()


# In[12]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# In[13]:


    image_url=soup.find('a', class_="fancybox")['data-fancybox-href']


# In[14]:


    print(image_url)


# In[15]:


    base_url='https://www.jpl.nasa.gov'


# In[16]:


    featured_image_url=base_url+image_url


# In[23]:


    print(featured_image_url)


# In[20]:


    url_3='https://twitter.com/marswxreport?lang=en'


# In[21]:


    browser.visit(url_3)


# In[22]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# In[23]:


    mars_weather=soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text


# In[24]:


    print(mars_weather)


# In[26]:


    url_4='https://space-facts.com/mars/'


# In[27]:


    tables = pd.read_html(url_4)



# In[38]:


    df=tables[0]



# In[40]:


    html_table = df.to_html()



    listings["news_title"] = news_title;
    listings["news_p"] = news_p;
    listings["featured_image_url"] = featured_image_url;
    listings["mars_weather"] = mars_weather;
    listings["html_table"] = html_table;


    return listings
