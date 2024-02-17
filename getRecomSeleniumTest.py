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
recommendation_page_button = driver.find_element(by="xpath", value='//*[@id="root"]/div/div[1]/div[1]/div[3]/a')
recommendation_page_button.click()

for i in range(1, 30):
    try:
        recommended_song_name = driver.find_element(by="xpath", value=f'//*[@id="root"]/div/div[2]/div[2]/div/table/tbody/tr[{i}]/td[1]')
        print(recommended_song_name.text)
    except:
        break

print()

our_recommendation_tab_button = driver.find_element(by="xpath", value=f'//*[@id="root"]/div/div[2]/div[1]/button[2]')
our_recommendation_tab_button.click()

for i in range(1, 31):
    try:
        recommended_song_name = driver.find_element(by="xpath", value=f'//*[@id="root"]/div/div[2]/div[2]/div/table/tbody/tr[{i}]/td[1]')
        print(recommended_song_name.text)
    except:
        break

print()

spotify_recommendation_tab_button = driver.find_element(by="xpath", value=f'//*[@id="root"]/div/div[2]/div[1]/button[3]')
spotify_recommendation_tab_button.click()

for i in range(1, 31):
    try:
        recommended_song_name = driver.find_element(by="xpath", value=f'//*[@id="root"]/div/div[2]/div[2]/div/table/tbody/tr[{i}]/td[1]')
        print(recommended_song_name.text)
    except:
        break

print()

spotify_recommendation_tab_button = driver.find_element(by="xpath", value=f'//*[@id="root"]/div/div[2]/div[1]/button[4]')
spotify_recommendation_tab_button.click()

for i in range(1, 31):
    try:
        recommended_song_name = driver.find_element(by="xpath", value=f'//*[@id="root"]/div/div[2]/div[2]/div/table/tbody/tr[{i}]/td[1]')
        print(recommended_song_name.text)
    except:
        break

end = time.time()

print(end - beginning)  ## 5.692904949188232
program_not_ended = False
monitor_thread.join()  ## CPU Usage: 47.5%, Memory Usage: 84.1%

