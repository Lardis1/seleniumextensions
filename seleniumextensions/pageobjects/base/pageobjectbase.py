from selenium.webdriver.remote.webdriver import WebDriver

class PageObject(object):
    """Page Object Base Class

    Used to manage Selenium Extensions Page Objects,
    Handle Arguments and Options, and provide additional 
    functionality to Page Objects.

    """
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def set_opts(self):
        # defined page object arguments here,
        # i.e. will pagefactories be used, ...
        pass    
