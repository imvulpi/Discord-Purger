# These might change in future
DELETE_MESSAGE_QUERY = '[id="message-delete"]'
SEARCH_INPUT_QUERY = '[class^="search__"]'
TOTAL_RESULTS_QUERY = '[class^="totalResults__"] [class="text-md-normal__4afad"]'
JUMP_TO_PAGE_QUERY = '[class^="defaultColor__"][aria-hidden^="true"][data-text-variant="heading-sm/semibold"]'
INPUT_WRAPPER_QUERY = '[class^="inputWrapper__"]'
JUMP_TO_PAGE_INPUT_CLASS = "jumpToPageInlineInput__"
PAGES_BUTTONS_QUERY = '[class^=roundButton__][role="button"][aria-label]'
QRCODE_QUERY = '[class^="qrCode_"]'
PASSWORD_INPUT_QUERY = '[name="password"]'
EMAIL_INPUT_QUERY = '[name="email"]'
SUBMIT_LOGIN_QUERY = '[type="submit"]'
NEXT_PAGE_QUERY = '[rel^="next"]'
MESSAGE_ID_QUERY = '[id^="message-devmode-copy-id-"]'
CLEAR_SEARCH_QUERY = '[class^="icon"][aria-label="Clear search"]'
MESSAGES_REQUEST_URL_SPLITTER = "messages/" # A piece of string that splits url into two parts: 1. unimportant, 2. message id, when deleting a message

def get_message_query(id: int):
    return f'[class^="container__"] [id="search-results-{id}"]'

def get_message_with_id_query(id: str):
    return f'[aria-labelledby="search-result-{id}"]'

def get_page_button_query(page_number: int):
    return f'[class^=roundButton__][role="button"][aria-label="Page {page_number}"]'