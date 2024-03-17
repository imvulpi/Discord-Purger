import math
from playwright.sync_api import Page
from commons.constants import DELETE_MESSAGE_QUERY, RANDOM_MESSAGES_DELETION_DELAYS, get_message_query
from commons.screenshots import screenshot_custom
from commons.search_utils import get_message_amount, next_page
from config import MESSAGE_DELETION_SPEED, NEXT_PAGE_DELAY, SCREENSHOTS_PATH

def delete_message(page: Page, number: int):
    if(number > 24 | number < 0):
        print("Number must be in range of 0-24")
        return False
    
    message_query = get_message_query(number)
    message = page.wait_for_selector(message_query)
    if(message is not None):
        page.wait_for_timeout(MESSAGE_DELETION_SPEED)
        message.click(button="right")
        delete_message_button = page.wait_for_selector(DELETE_MESSAGE_QUERY)
        if(delete_message_button is not None):
            delete_message_button.click(modifiers=["Shift"])
        else:
            raise BaseException(f"Could not find {DELETE_MESSAGE_QUERY} element.\nAre you an admin or owner of the message?")
    else:
        raise BaseException(f"Could not find {message_query} element")
    
def calculate_deletion_estimate(deletion_speed: int, page_load_speed: int, messages_amount: int):
    pages_amount = math.ceil(messages_amount/25)
    return (messages_amount * (deletion_speed + RANDOM_MESSAGES_DELETION_DELAYS)) + (pages_amount * page_load_speed)

def message_delete_loop(page: Page):
    messages_amount = get_message_amount(page)
    if(not messages_amount):
        raise BaseException("Could not find total result, Was search executed?\nSearch needs to be executed before executing this method")
    
    messages_deleted = 0
    current_message = 0
    print(f' | Messages amount: {messages_amount} | Rough estimate: {calculate_deletion_estimate(MESSAGE_DELETION_SPEED, NEXT_PAGE_DELAY, messages_amount)/1000}s')
    while(messages_amount > messages_deleted):
        if(current_message > 24):
            screenshot_custom(page, SCREENSHOTS_PATH+"page.png")
            next_page(page)
            current_message = 0

        print(f"Deleting message: {current_message}")
        delete_message(page, current_message)       

        current_message+=1
        messages_deleted+=1

    print(f"\n\nSTATISTICS: \nmessages deleted = {messages_deleted}")