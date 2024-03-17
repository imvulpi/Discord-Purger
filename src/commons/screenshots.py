from playwright.sync_api import Page

def take_screenshot(page: Page, path: str, screenshot_id: int):
    try:
        page.screenshot(path=f"{path}image{screenshot_id}.png")
        screenshot_id+=1
        return screenshot_id
    except:
        print("Screenshot attempt failed ;(")
        return screenshot_id
    
def screenshot_custom(page: Page, path: str):
    try:
        page.screenshot(path=f"{path}")
    except:
        print("Screenshot attempt failed ;(")