from playwright.sync_api import Page
from commons.constants.queries import SEARCH_INPUT_QUERY, TOTAL_RESULTS_QUERY, get_message_query
from config import GET_MESSAGE_ID_DELAY, MESSAGE_ID_DELAY

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
            try:
                return int(split_text[0])
            except:
                return 0
        else:
            print(f'Text does not exist on {TOTAL_RESULTS_QUERY} element')
            raise BaseException("Could not find text on total result")
    else:
        print(f'{TOTAL_RESULTS_QUERY} element does not exist')
        raise BaseException("Could not find total result, Was search executed?\nSearch needs to be executed before executing this method")

def get_message_id(page: Page, number: int):
    try:
        message = page.wait_for_selector(get_message_query(number), timeout=GET_MESSAGE_ID_DELAY)
        return message.get_attribute("aria-labelledby").split("search-result-")[1]
    except Exception as e:
        print("Error: ", e)
        return False
    
def get_message_ids(page: Page):
    message_ids = {}
    current_message = 0

    while(current_message < 25):
        id = get_message_id(page, current_message)
        if(id):
            message_ids[id] = False
        elif(id == False):
            print(f"Error, could not get {current_message} id.")
        current_message+=1
        page.wait_for_timeout(MESSAGE_ID_DELAY)
    return message_ids