from playwright.sync_api import Page
from commons.constants.queries import INPUT_WRAPPER_QUERY, JUMP_TO_PAGE_QUERY, NEXT_PAGE_QUERY, PAGES_BUTTONS_QUERY
from config import NEXT_PAGE_DELAY

def next_page(page: Page):
    try:
        next_page_button = page.wait_for_selector(NEXT_PAGE_QUERY)
        if(next_page_button):
            next_page_button.click()
            page.wait_for_selector('[id=search-results]')
            page.wait_for_timeout(NEXT_PAGE_DELAY)
        else:
            raise BaseException(f"Could not find {NEXT_PAGE_QUERY} element")
    except:
        return False
    
def get_jump_to_page_handle(website_page: Page):
    try:
        jump_to_page = website_page.query_selector(JUMP_TO_PAGE_QUERY)
        if(jump_to_page):
            jump_to_page.click()
            jump_page_input = website_page.wait_for_selector(INPUT_WRAPPER_QUERY, timeout=5000)
            if(jump_page_input != None):
                return jump_page_input
            else:
                return None
        else:
            jump_page_input = website_page.wait_for_selector(INPUT_WRAPPER_QUERY, timeout=5000)
            if(jump_page_input):
                return jump_page_input
            else:
                return None

    except:
        return None

def move_to_page(website_page: Page, page_number: int):
    try:
        jump_to_page = get_jump_to_page_handle(website_page)
        print(page_number)
        if(jump_to_page != None):
            jump_to_page.click()
            jump_to_page.type(str(page_number))
            jump_to_page.press("Enter")
        else:
            page_navigation_buttons = website_page.query_selector_all(PAGES_BUTTONS_QUERY)
            if(len(page_navigation_buttons) > 0):
                for button in page_navigation_buttons:
                    if(button.text_content() == str(page_number)):
                        button.click()
        website_page.wait_for_timeout(NEXT_PAGE_DELAY)
    except Exception as e:
        print("ERROR in page: ", page_number, e)
        return False