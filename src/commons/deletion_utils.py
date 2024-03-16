import math
from playwright.sync_api import Page
from commons.constants import DELETE_MESSAGE_QUERY, RANDOM_MESSAGES_DELETION_DELAYS, get_message_query
from commons.search_utils import get_message_amount
from config import MESSAGE_DELETION_SPEED

def delete_message(page: Page, number: int):
    if(number > 24 | number < 0):
        print("Number must be in rande of 0-24")
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
            print(f"Could not find {DELETE_MESSAGE_QUERY} element.\nAre you an admin or owner of the message?")
            return False
    else:
        print(f"Could not find {message_query} element")
        return False
    
def calculate_deletion_estimate(deletion_speed: int, page_load_speed: int, messages_amount: int):
    pages_amount = math.ceil(messages_amount/25)
    return (messages_amount * (deletion_speed + RANDOM_MESSAGES_DELETION_DELAYS)) + (pages_amount * page_load_speed)

def message_delete_loop(page: Page):
    messages_amount = get_message_amount(page)
    if(not messages_amount):
        raise BaseException("Could not find total result, Was search executed?\nSearch needs to be executed before executing this method")
    
    messages_deleted = 0
    current_page_deletion = 0
    print(f' | Messages amount: {messages_amount} | Rough estimate: {messages_amount * (MESSAGE_DELETION_SPEED + 20)/1000}s')
    while(messages_amount > messages_deleted):
        if(current_page_deletion > 24):
            # TODO: implement next page iteration
            break

        print(f"Deleting message: {current_page_deletion}")
        deletion_status = delete_message(page, current_page_deletion)
        
        if(deletion_status == False):
            print(f"Deletion of message {current_page_deletion} - failed")

        current_page_deletion+=1
        messages_deleted+=1