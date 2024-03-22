SCREENSHOTS_PATH = "./.screenshots/" # Your desired path where you want to save screenshots with a '/' at the end

MESSAGE_DELETION_SPEED = 250 # I recommend to use 200+, otherwise you are gonna get rate limited a lot
RATE_LIMITED_MESSAGE_DELETION_SPEED = 400

UNIVERSAL_DELAY = 200
NEXT_PAGE_DELAY = 3000
GET_MESSAGE_ID_DELAY = 1000
VERIFYING_DELETION_DELAY = 60000 # I recommend using 60000ms because it takes discord time to reindex, with 30000ms I found issues
MESSAGE_ID_DELAY = 20
PAGE_LOAD_DELAY = 5000

RATE_LIMITED_TIMEOUT = 10000
NORMAL_DELETION_TIMEOUT = 100
ID_DELETION_TIMEOUT = 100
UNIVERSAL_TIMEOUT = 1000


DELETION_FAIL_PER_PAGE_MAX = 24