"""
Login Test Module
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# User credentials
USERNAME = "mngr655650"  # Username
PASSWORD = "apebEqa"  # Password


def login(driver):
    """Perform login with credentials"""
    print("   🔑 Logging in...")
    
    try:
        wait = WebDriverWait(driver, 10)
        
        # Enter username
        username = wait.until(EC.presence_of_element_located((By.NAME, "uid")))
        username.clear()
        username.send_keys("mngr655650")
        print("      ✓ Username entered")
        
        # Enter password
        password = driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys("apebEqa")
        print("      ✓ Password entered")
        
        # Click login
        login_btn = driver.find_element(By.NAME, "btnLogin")
        login_btn.click()
        time.sleep(3)
        
        # Verify
        if "Manger Id" in driver.page_source:
            print("   ✅ Login successful")
            
            # Get manager ID
            try:
                manager = driver.find_element(By.XPATH, "//td[contains(text(),'Manger Id')]").text
                print(f"      ℹ️  {manager}")
            except:
                pass
        else:
            print("   ❌ Login failed - check credentials")
            
    except Exception as e:
        print(f"      ⚠️  Error: {str(e)}")
