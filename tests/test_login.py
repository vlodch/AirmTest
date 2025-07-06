# tests/test_login.py

import pytest
from pages.login_page import LoginPage

VALID_USERNAME = "admin"
VALID_PASSWORD = "WSSJYHpAHpSPLR0fDXHG"


@pytest.mark.usefixtures("page")
class TestLogin:

    def test_login_valid_credentials(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        page.wait_for_selector('text=Crop Insurance', timeout=10000)
        assert page.is_visible('text=Crop Insurance')

    def test_login_invalid_credentials(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("admin", "wrongpassword")
        # Wait for error message or login form to remain
        page.wait_for_selector('#username')
        # Adjust this assertion to match your app's error handling
        assert login_page.get_error_message() is not None or page.is_visible('#username')

    def test_login_empty_fields(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.open_login_popup()
        login_page.wait_for_login_form()
        login_page.clear_fields()
        login_page.submit()
        # Should remain on login form or show error
        page.wait_for_selector('#username')
        assert login_page.get_error_message() is not None or page.is_visible('#username')

    def test_login_only_username(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.open_login_popup()
        login_page.wait_for_login_form()
        login_page.fill_username(VALID_USERNAME)
        login_page.fill_password('')
        login_page.submit()
        page.wait_for_selector('#username')
        assert login_page.get_error_message() is not None or page.is_visible('#username')

    def test_login_only_password(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.open_login_popup()
        login_page.wait_for_login_form()
        login_page.fill_username('')
        login_page.fill_password(VALID_PASSWORD)
        login_page.submit()
        page.wait_for_selector('#username')
        assert login_page.get_error_message() is not None or page.is_visible('#username')

    def test_password_field_masking(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.open_login_popup()
        login_page.wait_for_login_form()
        # Verify password field type is 'password'
        input_type = page.get_attribute('#password', 'type')
        assert input_type == 'password'

    def test_session_persistence(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        page.wait_for_selector('text=Crop Insurance', timeout=10000)
        page.reload()
        assert page.is_visible('text=Crop Insurance')

    def test_logout(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        page.wait_for_selector('text=Crop Insurance', timeout=10000)
        # Find and click logout button (adjust selector as needed)
        page.click('button:has-text("Logout")')
        page.wait_for_selector('button:has-text("Login")')
        assert page.is_visible('button:has-text("Login")')
