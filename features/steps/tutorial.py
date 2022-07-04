from asyncio import sleep
from tkinter import BROWSE
from behave import given, when, then # type: ignore
from nturl2path import url2pathname
from selenium.webdriver import Firefox
import sys


@given('the website up')
def got_to_page(context):
 browser = Firefox()
 browser.get('https://www.oracle.com/br/index.html')
 # url2pathname = 'https://www.oracle.com/br/index.html'
 sys.exit()
  
@when('the devOps tab is open')
def open_devops(context):
    browser = Firefox()
    browser.get('https://www.oracle.com/br/index.html')
    Setores = browser.find_element_by_css_selector('.u30navul > li:nth-child(1) > button:nth-child(1)')
    Setores.click
    DevOps = browser.find_element_by_css_selector('#cloud-infrastructure > li:nth-child(12) > a:nth-child(1)')
    DevOps.click()

@then('some links will be clicked')
def step_impl(context):
    assert context.failed is False
    
