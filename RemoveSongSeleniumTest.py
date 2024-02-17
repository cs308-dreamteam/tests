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
delete_song_button = driver.find_element(by="xpath", value='//*[@id="root"]/div/div[2]/table/tbody/tr[9]/td[6]/button')
delete_song_button.click()
end = time.time()


print(end - beginning)  ## 1.044651985168457
program_not_ended = False
monitor_thread.join()  ## CPU Usage: 51.4%, Memory Usage: 85.2%
