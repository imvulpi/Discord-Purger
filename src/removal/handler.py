from commons.deletion_utils import message_delete_loop
from commons.login_utils import attempt_to_login
from commons.screenshots import take_screenshot
from removal.user_data import UserData, get_neccesary_data
from playwright.sync_api import sync_playwright, Page
from commons.search_utils import messages_search
from config import SCREENSHOTS_PATH

def removal_handler(arguments: list[str]):
    delete_arguments = get_neccesary_data(arguments)
    screenshot_id = 0
    
    print(f"URL: {delete_arguments.url} | Search query: {delete_arguments.search}")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(delete_arguments.url)

        handle_login(delete_arguments, page, screenshot_id)
        handle_search(delete_arguments, page, screenshot_id)
        handle_deletion(page, screenshot_id)
    

def handle_login(user_data: UserData, page: Page, screenshot_id: int):
    print("STATUS: Login Attempt")
    attempt_to_login(user_data, page, screenshot_id)
    page.wait_for_timeout(5000)
    screenshot_id = take_screenshot(page, SCREENSHOTS_PATH, screenshot_id)

def handle_search(user_data: UserData, page: Page, screenshot_id: int):
    print("STATUS: Message Search Attempt")
    messages_search(user_data.search, page)
    page.wait_for_timeout(5000)
    screenshot_id = take_screenshot(page, SCREENSHOTS_PATH, screenshot_id)

def handle_deletion(page: Page, screenshot_id: int):
    print("STATUS: Deletion Loop Initiated")
    message_delete_loop(page)
    screenshot_id = take_screenshot(page, SCREENSHOTS_PATH, screenshot_id)