from playwright.sync_api import sync_playwright, Page
from commons.screenshots import take_screenshot
from config import SCREENSHOTS_PATH
from removal.user_data import UserData

def messages_search(query: str, page: Page):
    search_input = page.wait_for_selector('[class^="search__"]')
    if(search_input is not None):
        search_input.click()
        search_input.type(query)
        search_input.press("Enter")
    else:
        raise BaseException("Search Input not found")