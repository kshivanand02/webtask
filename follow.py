from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# --- Config ---
USERNAME = "upalapati123"
PASSWORD = "g/*+hUU,j#&hGc4"
TARGET_USER = "cbitosc"

# --- Setup driver ---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 25)

try:
    # 1. Open Instagram login page (force login switcher)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    
    try:
        wait.until(EC.presence_of_element_located((By.NAME, "username")))
    except:
        driver.save_screenshot("error_login_page.png")
        print("❌ Login page didn't load. Screenshot saved.")
        driver.quit()
        os._exit(1)

    # 2. Login
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(7)

    # 3. Skip 'Save Info' and 'Turn on Notifications'
    try:
        not_now = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]")))
        not_now.click()
        time.sleep(3)
    except:
        pass

    # 4. Search user
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    search_box.clear()
    search_box.send_keys(TARGET_USER)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    # 5. Follow if not already following
    try:
        follow_button = driver.find_element(By.XPATH, "//button[text()='Follow']")
        follow_button.click()
        print("✅ Followed the user.")
        time.sleep(2)
    except:
        print(" Already following or button not found.")

    # 6. Extract profile data
    name = driver.find_element(By.XPATH, "//h2").text if driver.find_elements(By.XPATH, "//h2") else "N/A"
    bio = driver.find_element(By.XPATH, "//div[@class='-vDIg']/span").text if driver.find_elements(By.XPATH, "//div[@class='-vDIg']/span") else "N/A"
    stats = driver.find_elements(By.XPATH, "//ul[@class='k9GMp ']/li")
    posts = stats[0].text.split("\n")[0] if len(stats) > 0 else "N/A"
    followers = stats[1].text.split("\n")[0] if len(stats) > 1 else "N/A"
    following = stats[2].text.split("\n")[0] if len(stats) > 2 else "N/A"

    # 7. Save to file
    with open("cbitosc_data.txt", "w", encoding='utf-8') as f:
        f.write(f"Username: {TARGET_USER}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Bio: {bio}\n")
        f.write(f"Posts: {posts}\n")
        f.write(f"Followers: {followers}\n")
        f.write(f"Following: {following}\n")

    print("✅ Data saved to cbitosc_data.txt")

finally:
    driver.quit()
