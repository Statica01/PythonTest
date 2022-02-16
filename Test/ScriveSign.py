from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
import io
from selenium.webdriver.support import expected_conditions as EC


#driver = webdriver.Ie(service=Service(IEDriverManager().install()))
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://staging.scrive.com/t/9221714692410699950/7348c782641060a9')

nameField = driver.find_element(By.ID, 'name').send_keys("Test")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

scrollToTarget = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'action-arrow')))

driver.execute_script('arguments[0].scrollIntoView(true);', scrollToTarget)

nextButton = driver.find_element(
    By.XPATH, '/html/body/div[1]/div/div[3]/div[4]/div[1]/a[1]').click()

driver.maximize_window()

WebDriverWait(driver, 5).until(lambda x: x.find_element(
    By.CSS_SELECTOR, '.above-overlay')) 

screenshotImage = driver.find_element(
    By.CLASS_NAME, 'above-overlay').screenshot_as_png

imageStream = io.BytesIO(screenshotImage)
im = Image.open(imageStream)
im.save('sImage.png')
#im.show()
signButton = driver.find_element(
    By.XPATH, '/html/body/div[1]/div/div[3]/div[4]/div[1]/a[1]').click()
time.sleep(20)

actual = WebDriverWait(driver, 50).until(lambda w: w.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[2]/div/div[1]/h1/span")).text
print("Result", actual)
expectedText = "Document signed!"
assert actual == expectedText, "Document not signed"

driver.close()

