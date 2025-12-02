"""
conftest.py
Monkeypatch Selenium Chrome to use webdriver-manager if ChromeDriver is not on PATH.
This ensures Dash tests using dash.testing will automatically download ChromeDriver
and not fail with a 'chromedriver executable needs to be in PATH' error.

We patch only selenium.webdriver.Chrome, leaving other classes intact.
"""
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import selenium.webdriver as _selenium_webdriver
import warnings
import os


_original_chrome = getattr(_selenium_webdriver, "Chrome")


def _patched_chrome(*args, **kwargs):
    """Return a Chrome WebDriver that will use webdriver-manager to ensure
    a suitable chromedriver binary is installed and used when no explicit
    "service" is passed.
    """
    # If a service (with custom executable) is already supplied, keep it.
    if "service" not in kwargs:
        try:
            driver_path = ChromeDriverManager().install()
            kwargs["service"] = ChromeService(driver_path)
        except Exception as e:
            warnings.warn(f"webdriver-manager unable to install chromedriver: {e}")

    return _original_chrome(*args, **kwargs)


_selenium_webdriver.Chrome = _patched_chrome

# Ensure chromedriver binary is on PATH for processes that rely on PATH lookup
# instead of passing a Service. webdriver-manager will download the appropriate
# version into a cache; add that directory to PATH to avoid "chromedriver not in PATH" errors.
try:
    chromedriver_path = ChromeDriverManager().install()
    chromedriver_dir = os.path.dirname(chromedriver_path)
    current_path = os.environ.get("PATH", "")
    if chromedriver_dir not in current_path.split(os.pathsep):
        os.environ["PATH"] = chromedriver_dir + os.pathsep + current_path
except Exception:
    # If installation fails, warn but allow tests to continue; they may be skipped.
    warnings.warn("webdriver-manager failed to install chromedriver; integration tests may fail if driver is missing.")
