
# DRIVER_PATH = '/path/to/chromedriver'
# driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
# driver.get('https://google.com')
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://finviz.com/quote.ashx?t=nvda')
#print (driver)

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# driver.get("https://www.nintendo.com/")
print(driver.page_source)
r = driver.page_source
r_arr = r.split('</table>')
print(r_arr)

time.sleep(99999)
driver.quit()
