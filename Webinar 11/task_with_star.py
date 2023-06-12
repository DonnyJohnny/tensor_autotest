# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from time import sleep


path = Path.cwd()
options = Options()
options.add_experimental_option("prefs", {'download.default_directory': str(path), 'safebrowsing.enabled': 'false'})
browser = webdriver.Chrome(options=options)

try:
    browser.maximize_window()
    browser.get("https://sbis.ru/")
    footer = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".sbisru-Footer__container"))
    )
    browser.execute_script("arguments[0].scrollIntoView();", footer)
    plugin_link = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Скачать СБИС')]"))
    )
    plugin_link.click()

    sleep(1)
    plugin = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-id='plugin']"))
    )
    plugin.click()

    link = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Скачать (E')]"))
    )
    link.click()
    sleep(5)
    file = Path(path, "sbisplugin-setup-web.exe")
    assert file.exists(), "Плагин не был скачен"
    for file in path.glob('sbisplugin-setup-web.exe'):
        print(f'Размер файла: {round(int(file.stat().st_size) / 1048576, 2)} мб')

finally:
    browser.quit()
