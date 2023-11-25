from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

import time
import pytest

@pytest.mark.usefixtures("setup")
class Test_E2E:

    def test_chrome(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(options=options)

        driver.implicitly_wait(2)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()

        driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            title_text = product.find_element(By.CSS_SELECTOR, "div h4 a").text.lower()
            if "blackberry" in title_text:
                product.find_element(By.XPATH, "div/button").click()
                break

        driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        driver.find_element(By.ID, "country").send_keys("ind")
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".suggestions")))
        countries = driver.find_elements(By.CSS_SELECTOR, ".suggestions")

        for country in countries:
            country_name = country.find_element(By.XPATH, "ul/li/a")
            if "india" in country_name.text.lower():
                country_name.click()
                break

        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "input[class~=btn-success]").click()

        alert_msg = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        print(alert_msg)
        assert "Success! Thank you!" in alert_msg

        time.sleep(2)

        driver.close()

    def test_edge(self):
        options = webdriver.EdgeOptions()
        driver = webdriver.Remote(options=options)

        driver.implicitly_wait(2)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()

        driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            title_text = product.find_element(By.CSS_SELECTOR, "div h4 a").text.lower()
            if "blackberry" in title_text:
                product.find_element(By.XPATH, "div/button").click()
                break

        driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        driver.find_element(By.ID, "country").send_keys("ind")
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".suggestions")))
        countries = driver.find_elements(By.CSS_SELECTOR, ".suggestions")

        for country in countries:
            country_name = country.find_element(By.XPATH, "ul/li/a")
            if "india" in country_name.text.lower():
                country_name.click()
                break

        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "input[class~=btn-success]").click()

        alert_msg = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        print(alert_msg)
        assert "Success! Thank you!" in alert_msg

        time.sleep(2)

        driver.close()

    def test_firefox(self):
        options = webdriver.FirefoxOptions()
        driver = webdriver.Remote(options=options)

        driver.implicitly_wait(2)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()

        driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            title_text = product.find_element(By.CSS_SELECTOR, "div h4 a").text.lower()
            if "blackberry" in title_text:
                product.find_element(By.XPATH, "div/button").click()
                break

        driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        driver.find_element(By.ID, "country").send_keys("ind")
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".suggestions")))
        countries = driver.find_elements(By.CSS_SELECTOR, ".suggestions")

        for country in countries:
            country_name = country.find_element(By.XPATH, "ul/li/a")
            if "india" in country_name.text.lower():
                country_name.click()
                break

        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "input[class~=btn-success]").click()

        alert_msg = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        print(alert_msg)
        assert "Success! Thank you!" in alert_msg

        time.sleep(2)

        driver.close()