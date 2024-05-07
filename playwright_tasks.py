from robocorp import browser
from robocorp.tasks import task
from support import get_locator
from time import sleep
from RPA.Desktop import Desktop


@task
def example_on_playwright():
    """
    Example on Playwright
    """
    browser.configure(
        browser_engine="chromium",
        screenshot="only-on-failure",
        headless=False,
    )

    page = browser.goto("https://robocorp.com/portal")
    sleep(3)
    # page.wait_for_load_state("domcontentloaded")
    # page.wait_for_load_state("networkidle")
    # page.locator("//a[contains(@href, 'browser-automation')]").click()
    # links = page.locator("//a")
    # links.locator('text="Browser Automation"').click()
    # links.get_by_text("Browser Automation", exact=True).click()
    # page.locator("xpath=//input[@type='text']").fill("playwright")
    # page.locator(get_locator("portal-find-input")).fill("windows")
    # sleep(3)
    # Desktop().press_keys("ctrl", "p")
    page.get_by_role("link", name="Desktop Automation").click()
    page.get_by_role("link", name="Back to All").click()
    browser.screenshot()


# https://github.com/robocorp/robocorp/tree/master/browser
# https://github.com/robocorp/robocorp/blob/master/browser/docs/api/robocorp.browser.md#function-context
# https://playwright.dev/python/docs/api/class-browser#browser-new-context
# browser.configure_context(
#     user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# )


# @task
def example_on_selenium_demo_page():
    browser.configure(
        browser_engine="chromium",
        screenshot="only-on-failure",
        headless=False,
    )
    page = browser.goto("https://seleniumbase.io/demo_page")
    sleep(3)
    # Set the value directly using JavaScript
    range_input_selector = 'input[type="range"]'
    desired_value = 80
    page.eval_on_selector(
        range_input_selector, f"element => element.value = {desired_value}"
    )

    # Optionally, trigger the `input` and `change` events to simulate real user input
    page.dispatch_event(range_input_selector, "input")
    page.dispatch_event(range_input_selector, "change")
    browser.screenshot()
