import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").fill("my test task")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_test_id("todo-title").click()
    page.get_by_text("All Active Completed").click()
    page.get_by_test_id("todo-title").click()
    page.get_by_test_id("todo-title").click()
    page.get_by_role("checkbox", name="Toggle Todo").check()
