def mars_dict():

    from splinter import Browser
    from bs4 import BeautifulSoup
    import re
    import pandas as pd
    import time

    executable_path = {'executable_path': 'c:/bin/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    url = 'http://mars.nasa.gov/news/'
    browser.visit(url)

    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=10)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    article_title = soup.find('ul', class_ = 'item_list').find('li', class_ = 'slide').find('div', class_ = 'content_title').find('a').text
    article_paragraph = soup.find('div', class_='article_teaser_body').text

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_html = soup.find('div', class_ = 'carousel_container').find('div', class_ = 'carousel_items').find('article')['style']

    url = re.sub("background-image: url\('", "", image_html)
    url = re.sub("'\);", "", url)

    #return space_image_url
    space_image_url = 'https://www.jpl.nasa.gov' + url


    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    tables = pd.read_html(url)

    mars_html_table = tables[0]
    mars_html_table = mars_html_table.set_index([0])
    mars_html_table = mars_html_table.rename(columns={1: 'Mars data value'})
    mars_html_table = mars_html_table.rename_axis("Mars data description")
    mars_html_table = mars_html_table.to_html()
    #return mars_html_table


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    listed = soup.find_all('div', class_ = 'item')
    hemisphere_image_urls = []

    for item in listed:
        image_url = item.find('a')['href']
        title = item.find('div', class_ = 'description').find('a').find('h3').text
        image_url = 'https://astrogeology.usgs.gov' + image_url
        browser.visit(image_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        lg_image = soup.find('div', class_ = 'downloads').find('ul').find('li').find('a')['href']
        hemisphere_image_urls.append({'title': title, 'img_url': lg_image})
        
    hemisphere_image_urls
    #return hemisphere_image_urls

    browser.quit()

    web_dict = {
                'article_title': article_title, 
                'article_paragraph': article_paragraph,
                'mars_image': space_image_url,
                'mars_data_table': mars_html_table,
                'hemisphere_image_urls': hemisphere_image_urls}

    return web_dict
