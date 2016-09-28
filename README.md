# Overview
Project to display player stats across multiple bouts.

Currently displaying the number of jams participated in, positions played, total
jams played by player and total jams in the database.

# Required packages
### Pyvirtualdisplay
Pyvirtualdisplay is used to run selenium tests in a virtual window and requires 
`xvfb`

'''sudo apt-get install xvfb'''

### Chromedriver
Chromedriver is needed to run selenium tests with chrome. Customize the 
[chromedriver_cfg.py](source/functional_tests/chromedriver/chromedriver_cfg.py) 
with the local path to the chromedriver binary. See the 
[README.md](source/functional_tests/chromedriver/README.md) in chromedriver for
 more info.

# Project Templates
Both project and app templates for django-admin/manage.py are provided.

To create a project, from the root directory use:
`django-admin startproject --template project_template <project-name> source`

To create a new application with the template use:
`manage.py startapp --template <path-to-app-template> <app-name>`

# Virtual Environment
The project will ignore a virtual environment in `mbs_venv/`. 
