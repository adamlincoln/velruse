import time

from lettuce import step
from lettuce import world

import lettuce_webdriver.webdriver

def wait_for_elem(browser, xpath):
    elems = []
    while not elems:
        elems = browser.find_elements_by_xpath(xpath)
        if not elems:
            time.sleep(0.2)
    return elems


@step('I go to the velruse login page')
def login_page(step):
    world.browser.get(world.login_page)


@step('I have no cookies')
def no_cookies(step):
    world.browser.delete_all_cookies()


@step('I am logged into Facebook')    
def logged_into_facebook(step):
    step.given('I have no cookies')
    step.given('I go to "http://www.facebook.com/"')
    step.given('I should see "Sign Up"')
    step.given('I fill in "Email" with "%s"' % world.facebook_email)
    step.given('I fill in "Password" with "%s"' % world.facebook_password)
    step.given('I press "Login"')
    step.given('I should see "News Feed"')

@step('I have authorized the Facebook app')
def authorized_facebook_app(step):
    step.given('I go to "http://www.facebook.com/settings/?tab=applications"')

@step('I have not authorized the Facebook app')
def not_authorized_facebook_app(step):
    b = world.browser
    b.get('http://www.facebook.com/settings/?tab=applications')
    elems = b.find_elements_by_xpath('//span[contains(., "Velruse App")]')
    if elems:
        elems[0].click()
        wait_for_elem(b, '//a[contains(., "Remove app")]')[0].click()
        wait_for_elem(b, '//input[@type="button"][@value="Remove"]')[0].click()
        wait_for_elem(b, '//input[@type="button"][@value="Okay"]')[0].click()
