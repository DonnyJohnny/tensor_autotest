# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
login = ""

try:
    browser.get("https://sbis.ru/")
    contact = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".sbisru-Header__menu-link[href='/contacts']"))
    )
    contact.click()

    banner = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor"))
    )
    banner.click()

    handles = browser.window_handles
    browser.switch_to.window(handles[1])

    block = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".tensor_ru-Index__block4-content "
                                                         ".tensor_ru-Index__card-title"))
    )
    assert block.text == "Сила в людях", "Отсутствует блок новости 'Сила в людях'"
    link = browser.find_element(By.CSS_SELECTOR, ".tensor_ru-Header__menu-link[href='/about']")

    browser.execute_script("arguments[0].scrollIntoView();", link)

    link.click()

    assert browser.current_url == "https://tensor.ru/about", "Отрыта неверная ссылка"
finally:
    browser.quit()

