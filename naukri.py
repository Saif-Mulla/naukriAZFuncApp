from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

USERNAME = os.environ["NAUKRI_USERNAME"]
PASSWORD = os.environ["NAUKRI_PASSWORD"]

def run(USERNAME,PASSWORD):
    # Set up Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Use new headless mode
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36")  # Fake user-agent

    driver = webdriver.Chrome(options=options)

    try:
        # Open Naukri login page
        driver.get("https://www.naukri.com/mnjuser/profile")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

        # Wait for the username field to appear
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "usernameField")))
        username_field.send_keys(USERNAME)

        # Enter Password
        password_field = driver.find_element(By.ID, "passwordField")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)  # Wait for profile page to load

        # Navigate to Profile Update Section
        driver.get("https://www.naukri.com/mnjuser/profile")

        time.sleep(5)  # Wait for profile page to load
        print("Logged In")
        
        # ✅ Locate the Actual Edit Icon (Not the Hidden "Edit")
        edit_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//em[contains(@class, 'icon edit')]"))
        )

        # ✅ Click the Edit Icon (JavaScript Click if necessary)
        driver.execute_script("arguments[0].click();", edit_icon)
        print("Edit button clicked!")
        

        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Your Name']"))
        )   
        name_input.send_keys(Keys.CONTROL + "a")  # Select all text
        name_input.send_keys(Keys.BACKSPACE)  # Delete the selected text
        name_input.send_keys("Saif Saeed Mulla")
        print("Name updated")

        # ✅ Simulate pressing `TAB` to move focus out (Prevents validation issues)
        name_input.send_keys(Keys.TAB)
        time.sleep(2)

        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@id, 'saveBasicDetailsBtn')]"))
        )
        save_button.click()

        print("Profile updated successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()
