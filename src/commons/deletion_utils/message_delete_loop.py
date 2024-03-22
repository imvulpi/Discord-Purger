from commons.constants.messages import AMOUNT, CHECKING_RATE_LIMIT, CURRENT, DELETED, DELETING_UNDELETED, DELETION_ERRORS_MAX_REACHED, ERROR_DELETING_MESSAGE, MESSAGE, MESSAGES
from commons.constants.queries import MESSAGES_REQUEST_URL_SPLITTER
from commons.deletion_utils.other import calculate_page_to_delete
from commons.deletion_utils.deletion import delete_message_with_id, handle_normal_deletion
from commons.search_utils.messages import get_message_amount, get_message_ids
from commons.search_utils.pages import move_to_page, next_page
from config import DELETION_FAIL_PER_PAGE_MAX, RATE_LIMITED_TIMEOUT, RATE_LIMITED_MESSAGE_DELETION_SPEED
from playwright.sync_api import Page, Request

all_messages_deleted = False
message_ids: dict
def message_delete_loop(website_page: Page):
    global message_ids, all_messages_deleted

    messages_amount = get_message_amount(website_page)
    message_ids = get_message_ids(website_page)
    messages_deleted = 0
    current_message_number = 0
    page_switched = 1
    deletion_failed = 0

    print(f' > {MESSAGES} {AMOUNT}: {messages_amount}')
    website_page.on("request", verify_deletion)
    while(messages_amount > messages_deleted or all_messages_deleted == False):
        if(deletion_failed > DELETION_FAIL_PER_PAGE_MAX):
            print(f"{DELETION_ERRORS_MAX_REACHED} {DELETION_FAIL_PER_PAGE_MAX}")
            break

        if(current_message_number > 24 and all_messages_deleted == True):
            handle_next_page(website_page, messages_deleted, messages_amount)
            message_ids = get_message_ids(website_page)
            all_messages_deleted = False
            current_message_number = 0
            deletion_failed = 0
            page_switched+=1
        elif(current_message_number > 24 and all_messages_deleted == False):
            print(CHECKING_RATE_LIMIT)
            delete_undeleted(website_page, page_switched)
        else:
            result = handle_normal_deletion(website_page, current_message_number)
            if(result != False):
                messages_deleted+=1
            else:
                deletion_failed+=1
            current_message_number+=1
        print(f"{CURRENT} {MESSAGE}: {current_message_number}, {DELETED}: {messages_deleted} {MESSAGES}")

    website_page.remove_listener("request", verify_deletion)

def handle_next_page(website_page: Page, deleted_messages_amount: int, initial_messages_amount: int):
    page_to_delete = calculate_page_to_delete(deleted_messages_amount, get_message_amount(website_page), initial_messages_amount)
    move_to_page(website_page, page_to_delete)

def delete_undeleted(website_page: Page, current_page: int):
    global message_ids
    undeleted_amount = check_deleted()
    if(undeleted_amount > 0):
        website_page.wait_for_timeout(RATE_LIMITED_TIMEOUT)
        print(DELETING_UNDELETED)
        for (key, value) in message_ids.items():
            if(value == False):
                is_deleted = delete_message_with_id(website_page, key)
                if(is_deleted == False):
                    print(f"{ERROR_DELETING_MESSAGE} | {key}, {current_page}")
                website_page.wait_for_timeout(RATE_LIMITED_MESSAGE_DELETION_SPEED)
        check_deleted()

def verify_deletion(request: Request) -> None:
    global all_messages_deleted
    request_message_id = request.url.split(MESSAGES_REQUEST_URL_SPLITTER)
    response_status = request.response().status
    if(len(request_message_id)>1 and request.response().ok or response_status == 404):
        message_ids[request_message_id[1]] = True
    check_deleted()

def check_deleted():
    global all_messages_deleted, message_ids
    is_all_deleted = True
    amount_of_undeleted = 0
    for value in message_ids.values():
        if(value == False):
            amount_of_undeleted += 1
            is_all_deleted = False

    all_messages_deleted = is_all_deleted
    return amount_of_undeleted