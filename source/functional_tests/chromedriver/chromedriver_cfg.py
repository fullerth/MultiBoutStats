
import os

#Relative to the path of the base functional test class
relative_chromedriver_path = "chromedriver/chromedriver"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

chromedriver_path = os.path.join(BASE_DIR, relative_chromedriver_path)
