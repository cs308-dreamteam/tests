from selenium import webdriver
import time
import psutil

program_not_ended = True
def monitor_usage():
    while program_not_ended:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%")
        time.sleep(1)

import threading
monitor_thread = threading.Thread(target=monitor_usage, daemon=True)
monitor_thread.start()

URL = "http://localhost:3001"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

beginning = time.time()
driver.get(URL)
username_holder = driver.find_element(by="id", value="username")
password_holder = driver.find_element(by="id", value="password")
username_holder.send_keys("efe")
password_holder.send_keys("SOME_PASSWORD")

login_submit_button = driver.find_element(by="xpath", value='//*[@id="root"]/div/div[2]/div[2]/div/div[1]/form/div[3]/input')
login_submit_button.submit()

driver.implicitly_wait(3)
add_page_button = driver.find_element(by="xpath", value='//*[@id="root"]/div/div[1]/div[1]/div[1]/a')
add_page_button.click()

title = driver.find_element(by="name", value='s_title')
artist = driver.find_element(by="name", value='s_artist')
album = driver.find_element(by="name", value='s_album')
genre = driver.find_element(by="name", value='s_genre')
rating = driver.find_element(by="name", value='s_rating')

title.send_keys("Folklore")
artist.send_keys("Opeth")
album.send_keys("Heritage")
genre.send_keys("Metal")
rating.send_keys("5")

submit_button = driver.find_element(by="xpath", value='//*[@id="root"]/div/div[2]/div[1]/form/input')
submit_button.click()
end = time.time()

print(end - beginning)  ## 1.1517219543457031
program_not_ended = False
monitor_thread.join()  ## CPU Usage: 43.2%, Memory Usage: 81.7%
