from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
  
    # Visit visitcostarica.herokuapp.com
    url = "https://visitcostarica.herokuapp.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    # @TODO: YOUR CODE HERE!
    # Removed from website

    # Get the min avg temp
    # @TODO: YOUR CODE HERE!
    paragraphs = soup.find("div", id="weather")
    strongs = paragraphs.find_all("strong")
    min_temp = strongs[0].text
    
    # Get the max avg temp
    # @TODO: YOUR CODE HERE!
    max_temp = strongs[1].text

    # BONUS: Find the src for the sloth image
    # @TODO: YOUR CODE HERE!
    relative_path = soup.find_all("img")[2]['src']
    sloth_img = url + relative_path

    # Store data in a dictionary
    costa_data = {
        "sloth_img": sloth_img,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    # Quite the browser after scraping
    browser.quit()

    # Return results
    return costa_data

# print(scrape_info())

 


