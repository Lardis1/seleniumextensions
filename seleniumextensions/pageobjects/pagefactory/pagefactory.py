from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class PageFactory(object):
    
    def __getattr__(self, __name: str):
        pass

    # region Page Factory Helper Methods

    def unpack_parent_element(self, __parent: str):
        pass

    def unpack_element_type(self, __indicator: str):
        pass

    def find_extended_web_element(self, __locator: str):
        pass

    # endregion Page Factory Helper Methods
