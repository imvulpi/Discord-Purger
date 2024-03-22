from commons.constants.messages import DELETION_COMPLETED_STATUS, DELETION_LOOP_STATUS, LOGIN_ERROR_TROUBLESHOOTING, LOGIN_STATUS, SEARCH_STATUS, VERIFYING_DELETION_STATUS
from commons.deletion_utils.message_delete_loop import message_delete_loop
from commons.login_utils import attempt_to_login
from commons.screenshots import screenshot_custom
from commons.search_utils.messages import get_message_amount, messages_search
from removal.user_data import UserData, get_neccesary_data
from playwright.sync_api import sync_playwright, Page
from commons.search_utils.other import clear_search
from config import PAGE_LOAD_DELAY, SCREENSHOTS_PATH, VERIFYING_DELETION_DELAY

def removal_handler(arguments: list[str]):
    delete_arguments = get_neccesary_data(arguments)    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(delete_arguments.url)

        handle_login(delete_arguments, page)
        handle_search(delete_arguments.search, page)
        handle_deletion(page, delete_arguments.search)
    
def handle_login(user_data: UserData, website_page: Page):
    print(LOGIN_STATUS)
    try:
        attempt_to_login(user_data, website_page)
        website_page.wait_for_timeout(PAGE_LOAD_DELAY)
    except:
        print(LOGIN_ERROR_TROUBLESHOOTING)
        exit(0)

def handle_search(search: str, website_page: Page):
    print(SEARCH_STATUS)
    messages_search(search, website_page)
    website_page.wait_for_timeout(PAGE_LOAD_DELAY)

def handle_deletion(website_page: Page, search: str):
    print(DELETION_LOOP_STATUS)
    messages_amount = get_message_amount(website_page)
    while(messages_amount > 0):
        message_delete_loop(website_page)
        print(VERIFYING_DELETION_STATUS)
        website_page.wait_for_timeout(VERIFYING_DELETION_DELAY)
        search_cleared = clear_search(website_page)
        if(search_cleared):
            handle_search(search, website_page)
        else:
            break
        messages_amount = get_message_amount(website_page)
        if(messages_amount <= 0):
            break

    print(DELETION_COMPLETED_STATUS)
    screenshot_custom(website_page, SCREENSHOTS_PATH+"final.png")