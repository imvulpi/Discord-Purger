from playwright.sync_api import Page
from commons.constants.messages import DELETION, ERROR, ERROR_COULD_NOT_DELETE, FAILED, NUMBER_BETWEEN_0_24
from commons.constants.queries import DELETE_MESSAGE_QUERY, get_message_query, get_message_with_id_query
from config import ID_DELETION_TIMEOUT, MESSAGE_DELETION_SPEED, NORMAL_DELETION_TIMEOUT

def delete_message(page: Page, number: int):
    if(number > 24 or number < 0):
        print(NUMBER_BETWEEN_0_24)
        return False
    
    message_query = get_message_query(number)
    try:
        message = page.wait_for_selector(message_query, timeout=NORMAL_DELETION_TIMEOUT)
        if(message is not None):
            message.click(button="right")
            delete_message_button = page.wait_for_selector(DELETE_MESSAGE_QUERY, timeout=NORMAL_DELETION_TIMEOUT)
            if(delete_message_button is not None):
                delete_message_button.click(modifiers=["Shift"])
    except:
        print(f"{DELETION} {FAILED} (NORMAL)")
        return False

def handle_normal_deletion(website_page: Page, current_message: int):
    try:
        result = delete_message(website_page, current_message)
        if(result == False):
            return result  
        website_page.wait_for_timeout(MESSAGE_DELETION_SPEED)
    except:
        print(f"{ERROR} - {ERROR_COULD_NOT_DELETE}")

def delete_message_with_id(page: Page, message_id: str):   
    message_query = get_message_with_id_query(message_id)
    try:
        message = page.wait_for_selector(message_query, timeout=ID_DELETION_TIMEOUT)
        if(message is not None):
            message.click(button="right")
            delete_message_button = page.wait_for_selector(DELETE_MESSAGE_QUERY, timeout=ID_DELETION_TIMEOUT)
            if(delete_message_button is not None):
                delete_message_button.click(modifiers=["Shift"])
    except:
        print(f"{ERROR} - {ERROR_COULD_NOT_DELETE} (ID)")
        return False