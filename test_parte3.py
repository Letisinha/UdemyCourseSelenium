import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import conftest


@pytest.mark.usefixtures("setup_teardown")
class Test_parte03:
    def test_03_udemy(self):
        browser = conftest.browser
        # colocando o username
        username = browser.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        # colocando a senha
        password = browser.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        # clicar botão login
        btn = browser.find_element(By.ID, "login-button")
        btn.click()

        # adicionar item no carrinho
        AddCart1 = browser.find_element(By.XPATH, "//button[@name='add-to-cart-sauce-labs-backpack']").click()
        AddCart2 = browser.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # abrir o carrinho
        carrinho = browser.find_element(By.XPATH, '//*[@class="shopping_cart_link"]')
        carrinho.click()

        # fazer checkout
        browser.find_element(By.ID, "checkout").click()

        #preencher dados
        nome = browser.find_element(By.ID, "first-name").send_keys("nominho")
        sobrenome = browser.find_element(By.ID, "last-name").send_keys("sobrenominho")
        postal = browser.find_element(By.ID, "postal-code").send_keys("código postal")

        continuebtn = browser.find_element(By.ID, "continue").click()

        finishbtn = browser.find_element(By.ID, "finish").click()

        time.sleep(2)

        browser.quit()
