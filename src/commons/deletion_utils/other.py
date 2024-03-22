import math

def calculate_deletion_estimate(deletion_speed: int, page_load_speed: int, messages_amount: int):
    pages_amount = math.ceil(messages_amount/25)
    return (messages_amount * deletion_speed) + (pages_amount * page_load_speed)

def calculate_page_to_delete(deleted_messages_amount: int, current_messages_amount: int, initial_messages_amount):
    print(f"DEBUG: deleted messages: {deleted_messages_amount} initial: {initial_messages_amount} current_messages_amount: {current_messages_amount} calculated deleted: {deleted_messages_amount - (initial_messages_amount - current_messages_amount)}")
    deleted_messages_amount -= initial_messages_amount - current_messages_amount
    #page_to_delete = math.ceil(deleted_messages_amount/25)
    page_to_delete = deleted_messages_amount/25
    if(page_to_delete > 0 and initial_messages_amount == current_messages_amount):
        print(f"Page: {page_to_delete+1} (CALCULATED PAGE)")
        return math.ceil(page_to_delete+1)
    elif(page_to_delete > 0):
        print(f"Page: {page_to_delete} (CALCULATED PAGE)")
        return math.floor(page_to_delete)
    else:
        print(f"Page 1")
        return 1