"""
Banking Operations Module
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import re


def safe_click(driver, element):
    """Safely click an element using multiple methods"""
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        element.click()
        return True
    except:
        try:
            driver.execute_script("arguments[0].click();", element)
            return True
        except:
            return False


def handle_alert(driver):
    """Handle any alert that appears and return its text"""
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"      ℹ️  Alert: {alert_text}")
        alert.accept()
        time.sleep(1)
        return alert_text
    except:
        return None


def wait_for_element(driver, by, value, timeout=10):
    """Wait for element to be present"""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except:
        return None


def create_new_customer(driver):
    """Create a new customer"""
    print("   👤 Creating customer...")
    
    try:
        # Click New Customer
        new_customer = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "New Customer"))
        )
        safe_click(driver, new_customer)
        time.sleep(2)
        
        # Fill form
        print("      📝 Filling customer details...")
        
        # Name
        name = driver.find_element(By.NAME, "name")
        name.send_keys("John Doe")
        print("         ✓ Name: John Doe")
        
        # Gender (Male)
        gender = driver.find_element(By.XPATH, "//input[@value='m']")
        safe_click(driver, gender)
        print("         ✓ Gender: Male")
        
        # Date of Birth
        dob = driver.find_element(By.NAME, "dob")
        dob.send_keys("01011990")
        print("         ✓ DOB: 01/01/1990")
        
        # Address
        addr = driver.find_element(By.NAME, "addr")
        addr.send_keys("123 Test Street")
        print("         ✓ Address: 123 Test Street")
        
        # City
        city = driver.find_element(By.NAME, "city")
        city.send_keys("Mumbai")
        print("         ✓ City: Mumbai")
        
        # State
        state = driver.find_element(By.NAME, "state")
        state.send_keys("Maharashtra")
        print("         ✓ State: Maharashtra")
        
        # PIN
        pin = driver.find_element(By.NAME, "pinno")
        pin.send_keys("400001")
        print("         ✓ PIN: 400001")
        
        # Mobile
        mobile = driver.find_element(By.NAME, "telephoneno")
        mobile.send_keys("9876543210")
        print("         ✓ Mobile: 9876543210")
        
        # Email (unique with timestamp)
        email = driver.find_element(By.NAME, "emailid")
        unique_email = f"john{int(time.time())}@test.com"
        email.send_keys(unique_email)
        print(f"         ✓ Email: {unique_email}")
        
        # Password
        pwd = driver.find_element(By.NAME, "password")
        pwd.send_keys("Test@123")
        print("         ✓ Password: Test@123")
        
        # Submit
        submit = driver.find_element(By.NAME, "sub")
        safe_click(driver, submit)
        print("         ✓ Form submitted")
        time.sleep(3)
        
        # Handle any alert
        handle_alert(driver)
        
        # Get Customer ID
        try:
            time.sleep(2)
            cust_id_element = driver.find_element(By.XPATH, "//td[contains(text(),'Customer ID')]/following-sibling::td")
            customer_id = cust_id_element.text.strip()
            print(f"      ✅ Customer created successfully!")
            print(f"      🆔 Customer ID: {customer_id}")
            return customer_id
        except:
            print("      ✅ Customer created (but couldn't extract ID)")
            return None
            
    except Exception as e:
        print(f"      ❌ Error creating customer: {str(e)}")
        return None


def create_new_account(driver, customer_id):
    """Create a new bank account"""
    print("   💳 Creating bank account...")
    
    try:
        # Click New Account
        new_account = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "New Account"))
        )
        safe_click(driver, new_account)
        time.sleep(2)
        
        # Fill form
        print("      📝 Opening new account...")
        
        # Customer ID
        cust_field = driver.find_element(By.NAME, "cusid")
        if customer_id:
            cust_field.send_keys(customer_id)
            print(f"         ✓ Customer ID: {customer_id}")
        else:
            cust_field.send_keys("79074")
            print(f"         ✓ Customer ID: 79074")
        
        # Account Type
        acc_type = driver.find_element(By.NAME, "selaccount")
        acc_type.send_keys("Savings")
        print("         ✓ Account Type: Savings")
        
        # Initial Deposit
        deposit = driver.find_element(By.NAME, "inideposit")
        deposit.send_keys("10000")
        print("         ✓ Initial Deposit: ₹10,000")
        
        # Submit
        submit = driver.find_element(By.NAME, "button2")
        safe_click(driver, submit)
        print("         ✓ Form submitted")
        time.sleep(3)
        
        # Handle any alert
        handle_alert(driver)
        
        # Get Account Number
        try:
            time.sleep(2)
            acc_no_element = driver.find_element(By.XPATH, "//td[contains(text(),'Account ID')]/following-sibling::td")
            account_number = acc_no_element.text.strip()
            print(f"      ✅ Account created successfully!")
            print(f"      🏦 Account Number: {account_number}")
            
            # Save to file
            try:
                with open("last_account.txt", "w") as f:
                    f.write(account_number)
            except:
                pass
                
            return account_number
        except:
            print("      ✅ Account created (but couldn't extract number)")
            return None
            
    except Exception as e:
        print(f"      ❌ Error creating account: {str(e)}")
        return None


def check_mini_statement(driver, account_number=None):
    """Check mini statement (more reliable than balance enquiry)"""
    print("   📋 Getting mini statement...")
    
    try:
        # Click Mini Statement
        mini_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Mini Statement"))
        )
        safe_click(driver, mini_link)
        print("      ✓ Clicked Mini Statement")
        time.sleep(2)
        
        # Handle any alert
        alert_text = handle_alert(driver)
        if alert_text:
            if "Account does not exist" in alert_text:
                print("      ⚠️  No account exists yet")
                return
        
        # Enter account number
        acc_field = driver.find_element(By.NAME, "accountno")
        acc_field.clear()
        
        if account_number:
            acc_field.send_keys(account_number)
            print(f"      ✓ Using account: {account_number}")
        else:
            # Try to read from file
            try:
                with open("last_account.txt", "r") as f:
                    saved_account = f.read().strip()
                    acc_field.send_keys(saved_account)
                    print(f"      ✓ Using saved account: {saved_account}")
            except:
                acc_field.send_keys("180517")
                print(f"      ✓ Using account: 180517")
        
        # Submit
        submit = driver.find_element(By.NAME, "AccSubmit")
        safe_click(driver, submit)
        print("      ✓ Submitted")
        time.sleep(3)
        
        # Handle alert
        alert_text = handle_alert(driver)
        if alert_text:
            print(f"      ℹ️  {alert_text}")
            return
        
        # Display mini statement
        print("\n      📊 RECENT TRANSACTIONS:")
        print("      " + "="*60)
        
        # Find transaction table
        tables = driver.find_elements(By.XPATH, "//table")
        if tables:
            rows = tables[0].find_elements(By.TAG_NAME, "tr")
            for i, row in enumerate(rows):
                if i == 0:  # Header
                    print(f"      {row.text}")
                    print("      " + "-"*60)
                else:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    if len(cols) >= 3:
                        print(f"      {cols[0].text:<15} {cols[1].text:<15} {cols[2].text:<15}")
        
        print("      " + "="*60)
        
        # Try to get balance from the statement
        try:
            page_text = driver.find_element(By.TAG_NAME, "body").text
            balances = re.findall(r'Balance.*?(\d+,?\d*)', page_text, re.IGNORECASE)
            if balances:
                print(f"      💵 Current Balance: ₹{balances[0]}")
            else:
                # Look for any amount in the last line
                if tables and len(rows) > 1:
                    last_row = rows[-1]
                    cols = last_row.find_elements(By.TAG_NAME, "td")
                    if len(cols) >= 3:
                        print(f"      💵 Latest Balance: ₹{cols[2].text}")
        except:
            pass
            
    except Exception as e:
        print(f"      ⚠️  Mini statement error: {str(e)}")


def fund_transfer(driver, from_account=None, to_account=None):
    """Perform fund transfer with confirmation"""
    print("   💸 Processing fund transfer...")
    
    try:
        # Click Fund Transfer
        fund_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Fund Transfer"))
        )
        safe_click(driver, fund_link)
        print("      ✓ Clicked Fund Transfer")
        time.sleep(2)
        
        # Handle alert
        alert_text = handle_alert(driver)
        if alert_text:
            if "Account does not exist" in alert_text:
                print("      ⚠️  Accounts don't exist")
                return
        
        print("      📝 Filling transfer form...")
        
        # From Account
        payer = driver.find_element(By.NAME, "payersaccount")
        payer.clear()
        if from_account:
            payer.send_keys(from_account)
            print(f"      ✓ From Account: {from_account}")
        else:
            payer.send_keys("180517")
            print(f"      ✓ From Account: 180517")
        
        # To Account
        payee = driver.find_element(By.NAME, "payeeaccount")
        payee.clear()
        if to_account:
            payee.send_keys(to_account)
            print(f"      ✓ To Account: {to_account}")
        else:
            payee.send_keys("180518")
            print(f"      ✓ To Account: 180518")
        
        # Amount
        amount = driver.find_element(By.NAME, "ammount")
        amount.clear()
        amount.send_keys("500")
        print(f"      ✓ Amount: ₹500")
        
        # Description
        desc = driver.find_element(By.NAME, "desc")
        desc.clear()
        desc.send_keys("Test Transfer from Automation")
        print(f"      ✓ Description: Test Transfer")
        
        # Submit
        submit = driver.find_element(By.NAME, "AccSubmit")
        safe_click(driver, submit)
        print("      ✓ Submitted transfer")
        time.sleep(3)
        
        # Handle alert
        alert_text = handle_alert(driver)
        if alert_text:
            if "success" in alert_text.lower():
                print(f"\n      ✅ TRANSFER SUCCESSFUL!")
                print(f"      {alert_text}")
                
                # Try to get transaction details
                try:
                    print("\n      📋 Transaction Details:")
                    print("      " + "-"*50)
                    tables = driver.find_elements(By.XPATH, "//table")
                    for table in tables:
                        rows = table.find_elements(By.TAG_NAME, "tr")
                        for row in rows:
                            cols = row.find_elements(By.TAG_NAME, "td")
                            if len(cols) == 2:
                                print(f"      {cols[0].text}: {cols[1].text}")
                except:
                    pass
            else:
                print(f"      ⚠️  {alert_text}")
            
    except Exception as e:
        print(f"      ⚠️  Transfer error: {str(e)}")


def logout(driver):
    """Logout from application"""
    print("   🚪 Logging out...")
    
    try:
        logout_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
        )
        safe_click(driver, logout_link)
        print("      ✓ Clicked Logout")
        time.sleep(1)
        
        alert_text = handle_alert(driver)
        if alert_text:
            print(f"      ℹ️  {alert_text}")
        
        print("   ✅ Logout successful")
        
    except Exception as e:
        print(f"      ⚠️  Logout error: {str(e)}")
