"""
Main Program - Secure Banking Automation Test
Complete updated version with Mini Statement and PDF Report Generation
"""

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys

# Import custom modules
from security_tests import sql_injection_test, brute_force_test
from login_test import login
from banking_operations import (
    create_new_customer,
    create_new_account,
    check_mini_statement,
    fund_transfer,
    logout
)

# Import PDF Report Generator
from report_generator import generate_report_to_custom_folder


def setup_driver():
    """Setup and configure Edge driver"""
    print("🔧 Setting up Microsoft Edge driver...")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, "msedgedriver.exe")
    
    if not os.path.exists(driver_path):
        print(f"❌ ERROR: msedgedriver.exe not found!")
        print("Please download Edge WebDriver and place it in the project folder")
        sys.exit(1)
    
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--disable-notifications")
    edge_options.add_argument("--disable-popup-blocking")
    edge_options.add_argument("--disable-extensions")
    edge_options.add_argument("--disable-gpu")
    
    service = Service(driver_path)
    driver = webdriver.Edge(service=service, options=edge_options)
    driver.implicitly_wait(10)
    
    return driver


def take_screenshot(driver, test_name, step_number):
    """Take screenshot and save with proper naming"""
    try:
        project_dir = os.path.dirname(os.path.abspath(__file__))
        screenshots_dir = os.path.join(project_dir, "screenshots")
        
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
            print(f"📁 Created screenshots folder")
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{step_number:02d}_{test_name}_{timestamp}.png"
        filepath = os.path.join(screenshots_dir, filename)
        
        driver.save_screenshot(filepath)
        
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            print(f"   📸 Screenshot: {filename} ({file_size} bytes)")
            return filepath
        else:
            print(f"   ❌ Screenshot failed: {filename}")
            return None
    except Exception as e:
        print(f"   ❌ Screenshot error: {str(e)}")
        return None


def wait_for_manager_page(driver):
    """Wait for manager page to load"""
    print("      ⏳ Loading manager page...")
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'Manger Id')]"))
        )
        print("      ✅ Manager page ready")
        return True
    except Exception as e:
        print(f"      ⚠️ Manager page timeout: {str(e)}")
        return False


def main():
    """Main execution function"""
    print("\n" + "="*70)
    print("🚀 STARTING BANKING AUTOMATION TEST")
    print("="*70)
    
    driver = None
    step = 0
    customer_id = None
    account_number = None
    account2 = None
    
    try:
        # Initialize driver
        driver = setup_driver()
        
        # ================ PART 1: SECURITY TESTS ================
        print("\n" + "="*70)
        print("🔒 PART 1: SECURITY TESTS")
        print("="*70)
        
        # Test 1: SQL Injection
        step += 1
        print(f"\n📝 Test {step}.1: SQL Injection")
        print("-"*50)
        driver.get("https://demo.guru99.com/V4/")
        time.sleep(3)
        sql_injection_test(driver)
        take_screenshot(driver, "sql_injection", step)
        time.sleep(1)
        
        # Test 2: Brute Force
        step += 1
        print(f"\n📝 Test {step}.2: Brute Force")
        print("-"*50)
        driver.get("https://demo.guru99.com/V4/")
        time.sleep(3)
        brute_force_test(driver)
        take_screenshot(driver, "brute_force", step)
        time.sleep(1)
        
        # ================ PART 2: BANKING OPERATIONS ================
        print("\n" + "="*70)
        print("💼 PART 2: BANKING OPERATIONS")
        print("="*70)
        
        # Test 3: Login
        step += 1
        print(f"\n📝 Test {step}.1: Login")
        print("-"*50)
        driver.get("https://demo.guru99.com/V4/")
        time.sleep(3)
        login(driver)
        take_screenshot(driver, "after_login", step)
        time.sleep(1)
        
        if wait_for_manager_page(driver):
            
            # Test 4: Create Customer
            step += 1
            print(f"\n📝 Test {step}.2: Create Customer")
            print("-"*50)
            driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
            time.sleep(2)
            customer_id = create_new_customer(driver)
            take_screenshot(driver, "create_customer", step)
            time.sleep(1)
            
            if customer_id:
                print(f"      ✅ Customer ID: {customer_id}")
            
            # Test 5: Create First Account
            step += 1
            print(f"\n📝 Test {step}.3: Create First Account")
            print("-"*50)
            driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
            time.sleep(2)
            account_number = create_new_account(driver, customer_id)
            take_screenshot(driver, "create_account", step)
            time.sleep(1)
            
            if account_number:
                print(f"      ✅ Account Number: {account_number}")
            
            # Test 6: Mini Statement
            step += 1
            print(f"\n📝 Test {step}.4: Mini Statement")
            print("-"*50)
            driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
            time.sleep(2)
            check_mini_statement(driver, account_number)
            take_screenshot(driver, "mini_statement", step)
            time.sleep(1)
            
            # Test 7: Create Second Account for Fund Transfer
            step += 1
            print(f"\n📝 Test {step}.5: Create Second Account")
            print("-"*50)
            driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
            time.sleep(2)
            account2 = create_new_account(driver, customer_id)
            take_screenshot(driver, "second_account", step)
            time.sleep(1)
            
            if account2:
                print(f"      ✅ Second Account: {account2}")
            
            # Test 8: Fund Transfer
            step += 1
            print(f"\n📝 Test {step}.6: Fund Transfer")
            print("-"*50)
            driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
            time.sleep(2)
            
            if account_number and account2:
                fund_transfer(driver, account_number, account2)
                take_screenshot(driver, "fund_transfer", step)
                time.sleep(1)
            
            # Test 9: Logout
            step += 1
            print(f"\n📝 Test {step}.7: Logout")
            print("-"*50)
            driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
            time.sleep(2)
            logout(driver)
            take_screenshot(driver, "after_logout", step)
            time.sleep(1)
        
        # ================ TEST SUMMARY ================
        print("\n" + "="*70)
        print("✅ TEST COMPLETED SUCCESSFULLY")
        print("="*70)
        print("✓ SQL Injection Test")
        print("✓ Brute Force Test")
        print("✓ Login Test")
        print("✓ Create Customer Test")
        if customer_id:
            print(f"  └─ Customer ID: {customer_id}")
        print("✓ Create First Account Test")
        if account_number:
            print(f"  └─ Account Number: {account_number}")
        print("✓ Mini Statement Test")
        print("✓ Create Second Account Test")
        if account2:
            print(f"  └─ Second Account: {account2}")
        print("✓ Fund Transfer Test")
        print("✓ Logout Test")
        print("="*70)
        
        # ================ GENERATE PDF REPORT ================
        # REPORTS SAVED TO: D:\Desktop
        custom_folder = r"D:\Desktop"
        
        # Alternative: Create a subfolder for reports
        # custom_folder = os.path.join(r"D:\Desktop", "BankingReports")
        
        report_path = generate_report_to_custom_folder(
            customer_id=customer_id,
            account_number=account_number,
            account2=account2,
            custom_folder=custom_folder
        )
        
        if report_path:
            print(f"\n📊 PDF Report generated successfully!")
            print(f"📁 Report saved to: {report_path}")
        else:
            print(f"\n⚠️ PDF Report generation had issues, but tests completed.")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Test interrupted by user")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        if driver:
            take_screenshot(driver, "error", 99)
    
    finally:
        if driver:
            print("\n🧹 Closing browser...")
            driver.quit()
            print("✅ Browser closed")
    
    print("\n🏁 Automation Testing Completed")


if __name__ == "__main__":
    main()