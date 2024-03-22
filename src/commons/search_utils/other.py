from playwright.sync_api import Page
from commons.constants.queries import CLEAR_SEARCH_QUERY
from config import UNIVERSAL_TIMEOUT
    
def clear_search(page: Page):
    clear_button = page.wait_for_selector(CLEAR_SEARCH_QUERY, timeout=UNIVERSAL_TIMEOUT)
    if(clear_button):
        clear_button.click()
        return True
    else:
        return False