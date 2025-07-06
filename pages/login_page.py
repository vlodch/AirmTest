# pages/login_page.py

from playwright.sync_api import Page


class LoginPage:
    URL = "https://airm-consulting.github.io/qc-test/"

    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto(self.URL)

    def open_login_popup(self):
        self.page.click('button:has-text("Login")')

    def wait_for_login_form(self):
        self.page.wait_for_selector('#username')
        self.page.wait_for_selector('#password')

    def fill_username(self, username: str):
        self.page.fill('#username', username)

    def fill_password(self, password: str):
        self.page.fill('#password', password)

    def submit(self):
        self.page.click('button.login-button')

    def login(self, username: str, password: str):
        self.open_login_popup()
        self.wait_for_login_form()
        self.fill_username(username)
        self.fill_password(password)
        self.submit()

    def get_error_message(self):
        # Adjust selector if your app displays error messages differently
        return self.page.inner_text('.login-error') if self.page.is_visible('.login-error') else None

    def clear_fields(self):
        self.page.fill('#username', '')
        self.page.fill('#password', '')
