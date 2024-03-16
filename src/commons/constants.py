# These might change in future

DELETE_MESSAGE_QUERY = '[id="message-delete"]'
SEARCH_INPUT_QUERY = '[class^="search__"]'
TOTAL_RESULTS_QUERY = '[class^="totalResults__"] [class="text-md-normal__4afad"]'
QRCODE_QUERY = '[class^="qrCode_"]'
PASSWORD_INPUT_QUERY = '[name="password"]'
EMAIL_INPUT_QUERY = '[name="email"]'
SUBMIT_LOGIN_QUERY = '[type="submit"]'
RANDOM_MESSAGES_DELETION_DELAYS = 30

def get_message_query(id: int):
    return f'[class^="container__"] [id="search-results-{id}"]'