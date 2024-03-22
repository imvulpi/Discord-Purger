from playwright.sync_api import Page
from commons.constants.messages import NO_STANDARD_LOGIN, PRESS_ANY_CONTINUE_QR_CODE
from commons.constants.queries import EMAIL_INPUT_QUERY, PASSWORD_INPUT_QUERY, QRCODE_QUERY, SUBMIT_LOGIN_QUERY
from commons.screenshots import screenshot_custom
from config import SCREENSHOTS_PATH
from removal.user_data import UserData

def attempt_to_login(data: UserData, page: Page):
    if(data.email != None and data.password != None):
        standard_login(page, data.password, data.email)
    else:
        page.wait_for_selector(QRCODE_QUERY)
        screenshot_custom(page, SCREENSHOTS_PATH+"qrcode.png")
        print(NO_STANDARD_LOGIN)
        input(PRESS_ANY_CONTINUE_QR_CODE)


def standard_login(page: Page, password: str, email: str):
    password_field = page.wait_for_selector(PASSWORD_INPUT_QUERY)
    email_field = page.wait_for_selector(EMAIL_INPUT_QUERY)

    if(password_field and email_field):
        password_field.click()
        password_field.type(password)
        email_field.click()
        email_field.type(email)

        login_button = page.query_selector(SUBMIT_LOGIN_QUERY)
        if(login_button):
            login_button.click()
        else:
            raise BaseException(f"Could not find {SUBMIT_LOGIN_QUERY} element")
    else:
        if(not password_field and not email_field):
            raise BaseException(f"Could not find: \n1. {PASSWORD_INPUT_QUERY} and \n2. {EMAIL_INPUT_QUERY} \nelements")
        elif(not password_field):
            raise BaseException(f"Could not find \n{PASSWORD_INPUT_QUERY} \nelement")
        elif(not email_field):
            raise BaseException(f"Could not find \n{EMAIL_INPUT_QUERY} \nelement")
        else:
            raise BaseException(f"Weird unknown error")