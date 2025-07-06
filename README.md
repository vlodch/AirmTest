# Playwright Python Automation

## Project Structure

- `pages/` - Page Object Model classes for each page.
- `tests/` - All test cases.
- `conftest.py` - Shared pytest fixtures for browser and page.
- `requirements.txt` - Project dependencies.

## Setup

Install dependencies using `pip install -r requirements.txt`
playwright install


## Run Tests

pytest
or 
pytest --html=report.html --self-contained-html - if HTML report is needed

## Extend

- Add new page objects in `pages/`.
- Add new test files in `tests/`.
- Use and extend fixtures in `conftest.py`.
