import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import conftest


@pytest.mark.usefixtures("setup_teardown")
class Test_parte04:
    def test_04_udemy(self):
        browser = conftest.browser
        # colocando o username
        username = browser.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        # colocando a senha
        password = browser.find_element(By.ID, "password")
        password.send_keys("senha_invalida")

        # clicar botão login
        btn = browser.find_element(By.ID, "login-button")
        btn.click()

        assert len(browser.find_elements(By.CLASS_NAME, "title")) == 0

        time.sleep(1)

        browser.quit()
