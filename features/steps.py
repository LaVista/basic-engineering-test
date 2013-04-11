# -*- coding: utf-8 -*-
from lettuce import *
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_brower():
    world.browser = webdriver.Firefox()

@after.all
def teardown_browser(total):
    world.browser.close()
