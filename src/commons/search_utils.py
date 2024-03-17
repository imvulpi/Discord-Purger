from playwright.sync_api import Page
from commons.constants import NEXT_PAGE_QUERY, SEARCH_INPUT_QUERY, TOTAL_RESULTS_QUERY
from config import NEXT_PAGE_DELAY

def messages_search(search: str, page: Page):
    search_input = page.wait_for_selector(SEARCH_INPUT_QUERY)
    if(search_input is not None):
        search_input.click()
        search_input.type(search)
        search_input.press("Enter")
    else:
        raise BaseException("Search Input not found")
    
def get_message_amount(page: Page):
    search_result = page.wait_for_selector(TOTAL_RESULTS_QUERY)
    if(search_result is not None):
        text = search_result.text_content()
        if(text is not None):
            split_text = text.split(' ')
            return int(split_text[0])
        else:
            print(f'Text does not exist on {TOTAL_RESULTS_QUERY} element')
    else:
        print(f'{TOTAL_RESULTS_QUERY} element does not exist')

def next_page(page: Page):
    next_page_button = page.wait_for_selector(NEXT_PAGE_QUERY)
    if(next_page_button):
        next_page_button.click()
        page.wait_for_selector('[id=search-results]')
        page.wait_for_timeout(NEXT_PAGE_DELAY)
    else:
        raise BaseException(f"Could not find {NEXT_PAGE_QUERY} element")