# Load packages
from selenium import webdriver
from PIL import Image
import sys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Get list of bird codes from our selection process (data_ebirds)
birds = pd.read_csv("data_ebird/common_birds_in_USA.csv")

#Make little for testing!
birds = birds[1:10]

# Set up Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for bird in birds.species_code:
    # Open website window and click to first image!
    driver.get("https://ebird.org/species/" + bird)
    showcase = driver.find_element_by_id("MediaFeed-showcase")
    showcase.click()
    driver.maximize_window()

    # Cycle thrugh images!
    for i in range(3):
        if i > 0:
            nextbutton = driver.find_element_by_css_selector("div.Lightbox-nav button:last-of-type")
            nextbutton.click()
        
        # Wait for load and take screenshot
        time.sleep(1)
        driver.save_screenshot('img/' + bird + '_' + str(i) + '.png')


        # Reopen image to edit
        image = Image.open('img/' + bird + '_' + str(i) + '.png')

        # Code smells - precise location of the main image on the ebirds page
        left = 425
        top = 0
        right = left + 1070
        bottom = top + 805

        image = image.crop((left, top, right, bottom)) # defines crop points
        image.save('img/' + bird + '_' + str(i) + '.png')
        image.show()


# Library of snow goose images
# https://macaulaylibrary.org/catalog?searchField=species&taxonCode=snogoo