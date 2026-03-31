"""
Security Tests Module
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def sql_injection_test(driver):
    """Test SQL Injection vulnerability"""
    print("   🔍 Running SQL Injection Test...")
    
    try:
        wait = WebDriverWait(driver, 10)
        
        # SQL injection payload
        username = wait.until(EC.presence_of_element_located((By.NAME, "uid")))
        username.clear()
        username.send_keys("' OR '1'='1' --")
        
        password = driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys("anything")
        
        login_btn = driver.find_element(By.NAME, "btnLogin")
        login_btn.click()
        
        time.sleep(2)
        
        # Check result
        if "Manger Id" in driver.page_source:
            print("   ❌ SQL Injection VULNERABLE!")
        else:
            print("   ✅ SQL Injection Test PASSED")
            
    except Exception as e:
        print(f"      ⚠️  Error: {str(e)}")


def brute_force_test(driver):
    """Test Brute Force protection"""
    print("   🔍 Running Brute Force Test...")
    
    try:
        wait = WebDriverWait(driver, 10)
        
        for attempt in range(1, 4):
            print(f"      Attempt {attempt}/3...")
            
            username = wait.until(EC.presence_of_element_located((By.NAME, "uid")))
            password = driver.find_element(By.NAME, "password")
            login_btn = driver.find_element(By.NAME, "btnLogin")
            
            username.clear()
            password.clear()
            
            username.send_keys(f"invalid_{attempt}")
            password.send_keys("wrong")
            
            login_btn.click()
            time.sleep(1)
            
            # Handle alert
            try:
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(1)
            except:
                pass
        
        print("   ✅ Brute Force Test Completed")
        
    except Exception as e:
        print(f"      ⚠️  Error: {str(e)}")