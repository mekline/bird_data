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
    # Open website window 
    driver.get("https://ebird.org/species/" + bird)
    driver.maximize_window()
    time.sleep(1)

    # Save full screenshot
    driver.save_screenshot('img/' + bird + '.png')

    # Crop to image!
    image = Image.open('img/' + bird + '.png')

    # Code smells - precise location of the main image on the ebirds page
    left = 685
    top = 115
    right = left + 860
    bottom = top + 620

    image = image.crop((left, top, right, bottom)) # defines crop points
    image.save('img/' + bird + '.png')
    image.show()