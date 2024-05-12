from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image
import pyscreenshot as ImageGrab
import matplotlib.pyplot as plt

# Function to summon Chrome
def summon_chrome():
    chrome_path = "/opt/google/chrome/chrome"
    profile_path = "/home/vardhin/.config/google-chrome/Profile 1"
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path  
    options.add_experimental_option("detach", True)
    options.add_argument(f"user-data-dir={profile_path}") 
    driver = webdriver.Chrome(options=options)
    return driver

# Function to handle login
def login(driver, username, password):
    driver.get("https://vtop.vit.ac.in/vtop/open/page")
    page2_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    page2_button.click()
    while True:
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button = driver.find_element(By.ID, "submitBtn")
        login_button.click()
        time.sleep(5)
        current_url = driver.current_url
        if current_url == "https://vtop.vit.ac.in/vtop/content?":
            print("Hooray! We've logged in successfully!")
            break
        else:
            print("Uh-oh, looks like the login failed. Let's give it another shot!")
            driver.refresh()

# Function to select Winter option
def select_winter_option(driver):
    try:
        dropdown_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "semesterSubId"))
        )
        dropdown_menu.click()
        options = dropdown_menu.find_elements(By.TAG_NAME, "option")
        for option in options:
            if "Winter" in option.text:
                option.click()
                break
        print("Winter option selected from the dropdown menu!")
    except Exception as e:
        print("An error occurred while selecting the Winter option:", e)

# Function to perform DA tasks
def perform_da_tasks(driver):
    da_upload_button = driver.find_element(By.XPATH, "//button[text()='DA Upload']")
    da_upload_button.click()
    print("Boom! DA Upload button clicked!")
    time.sleep(5)

# Function to scrape text
def scrape_text_to_file(driver):
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    text_elements = soup.find_all(text=True)
    full_text = "\n".join(text_elements)
    with open("website_text.txt", "w", encoding="utf-8") as file:
        file.write(full_text)
    print("Website text has been scraped and saved to 'website_text.txt' file!")

# Function to capture and extract text from image
def capture_and_extract_text():
    try:
        screenshot = ImageGrab.grab()
        screenshot.save("da_deadline.png")
        print("Screenshot captured and saved as 'da_deadline.png'")
        extracted_text = pytesseract.image_to_string("da_deadline.png", lang='eng', config='--psm 6')
        with open('da.txt', 'w') as file:
            file.write(extracted_text)
        print("Extracted text saved to 'da.txt'")
    except Exception as e:
        print("An error occurred while taking screenshot and extracting text:", e)

# Function to open and show image
def open_and_show_image(image_path):
    try:
        image = Image.open(image_path)
        plt.imshow(image)
        plt.axis('off')
        plt.show()
    except Exception as e:
        print("An error occurred while opening and showing the image:", e)

# Function to get DA
def get_da(username, password):
    driver = summon_chrome()
    login(driver, username, password)
    perform_da_tasks(driver)
    select_winter_option(driver)
    time.sleep(5)
    capture_and_extract_text()

username = "VARDHIN0369"
password = "TheDarkAzure#9"
get_da(username,password)
