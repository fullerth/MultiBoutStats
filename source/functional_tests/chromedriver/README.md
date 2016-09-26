The (chromedriver_cfg.py)[chromedriver_cfg.py] file sets `chromedriver_path` 
with the path to the chromedriver binary. The 
(base functional test class)[functional_test.py] passes 
`executable_path=chromedriver_path` as an argument to `webdriver.Chrome()`.

The default project setting is to look for the chromedriver binary in this 
folder. Change the configuration variable to point to the local location of
the chromedriver binary. I don't keep chromedriver on my PATH, but I suspect 
this may override that setting, as the path is passed to the webdriver 
constructor. 

