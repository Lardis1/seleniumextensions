from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


BY = 0
SEARCH_VALUE = 1

class PageFactory(object):
    """Page Factory Implementation For Page Objects

    Searches for element locator values in 'elements'
    dictionary used to return selenium web elements.
    
    Locators Dictionary
    -------------------
    
    locators = {
        "element_name": (
            'selector key', #determines By type
            'search_value', #query to work alongside By type
            'parent', #string reference to parent element
            ElementType, #element type indicator
            *args, #any additional arguments used to initialize element
        )
    }
    >>> See locators guide for defining elements in elements dictionary
    """
    BY_TYPES = {
        'css': By.CSS_SELECTOR,
        'class': By.CLASS_NAME,
        'id': By.ID,
        'link_text': By.LINK_TEXT,
        'partial_link_text': By.PARTIAL_LINK_TEXT,
        'name': By.NAME,
        'tag': By.TAG_NAME,
        'xpath': By.XPATH,
    }
    def __getattr__(self, __name: str):
        if __name in self.elements.keys():
            request = __name
            by = PageFactory.BY_TYPES[self.elements[request][BY]]
            search_value = self.elements[request][SEARCH_VALUE]
            
            try:
                driver: WebDriver = self.driver
            except AttributeError:
                raise AttributeError('Page Objects Must Have A Driver Attribute')
            
            return driver.find_element(by, search_value) 
        
        raise AttributeError(__name)

    # region Page Factory Helper Methods

    def unpack_parent_element(self, __parent: str):
        pass

    def unpack_element_type(self, __indicator: str):
        pass

    def find_extended_web_element(self, __locator: str):
        pass

    # endregion Page Factory Helper Methods
