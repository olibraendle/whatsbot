## all whatsapp api calls (send, receive)

from playwright.sync_api import sync_playwright

def start_browser():
    global _playwright, _browser
    _playwright = sync_playwright().start()
    _browser = _playwright.chromium.launch_persistent_context(
        user_data_dir="session",
        headless = False
    )
    page = _browser.new_page()
    page.goto("https://web.whatsapp.com")
    page.wait_for_selector('#side', timeout=60000)

    return page



