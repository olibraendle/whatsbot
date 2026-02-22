## all whatsapp api calls (send, receive)

from playwright.sync_api import sync_playwright
from config import PHONE_NUMBER


_playwright = None
_browser = None


def start_browser():
    global _playwright, _browser
    _playwright = sync_playwright().start()
    _browser = _playwright.chromium.launch_persistent_context(
        user_data_dir="session", headless=False
    )
    page = _browser.new_page()
    page.goto(f"https://web.whatsapp.com/send?phone={PHONE_NUMBER}")
    page.wait_for_selector(
        '[aria-placeholder="Gib eine Nachricht ein."]', timeout=6000000
    )  # choose [#side] for quick testing or [data-testid="chat-list"]

    return page


def send_message(page, text):
    page.click('[aria-placeholder="Gib eine Nachricht ein."]')
    page.type('[aria-placeholder="Gib eine Nachricht ein."]', text)
    page.wait_for_timeout(1000)
    page.click('[aria-label="Senden"]')
    page.wait_for_timeout(2000)


def get_last_message(page):
    return page.locator('[data-testid="selectable-text"]').last.inner_text()
