from playwright.sync_api import sync_playwright, Page
from commons.screenshots import take_screenshot
from config import SCREENSHOTS_PATH
from removal.search import messages_search
from removal.user_data import UserData

def messages_url_deleter(user_data: UserData):
    screenshot_id = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(user_data.url)

        screenshot_id = take_screenshot(page, SCREENSHOTS_PATH, screenshot_id)
        print(user_data.url, user_data.email, user_data.password, user_data.search)
        attempt_to_login(user_data, page, screenshot_id)
        page.wait_for_timeout(5000)
        screenshot_id = take_screenshot(page, SCREENSHOTS_PATH, screenshot_id)

        print("Trying to get messages search")
        messages_search(user_data.search, page)
        page.wait_for_timeout(5237)
        screenshot_id = take_screenshot(page, SCREENSHOTS_PATH, screenshot_id)

        browser.close()

def attempt_to_login(data: UserData, page: Page, screenshot_id):
    if(data.email != None and data.password != None):
        standard_login(page, data.password, data.email)
    else:
        page.wait_for_selector('[class^="qrCode_"]')
        screenshot_id = take_screenshot(page, SCREENSHOTS_PATH, screenshot_id)
        print(f"No email and password input, you will need to scan the discord QR code. Please scan the QR in screenshot named: \"image{screenshot_id-1}.png\"")
        input("Press any key to continue | Press only after scanning the QR code")


def standard_login(page: Page, password: str, email: str):
    password_field = page.wait_for_selector('[name="password"]')
    email_field = page.wait_for_selector('[name="email"]')

    if(password_field and email_field):
        password_field.click()
        password_field.type(password)
        email_field.click()
        email_field.type(email)

        login_button = page.query_selector('[type="submit"]')
        if(login_button):
            login_button.click()
        else:
            raise BaseException("Could not login | login button doesnt exist")
    else:
        raise BaseException("Could not login | password_field or email_field doesnt exist")
