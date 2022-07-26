from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import warnings

def timingTest(driver):
        # Este calcula dos tiempos o timings.
        # Performance de back-end: desde cuando el usuario empieza la navegación hasta cuando recibe la primera respuesta.
        # Performance del front-end: inicia cuando el usuario recibe la primera respuesta y hasta que la carga del DOM se complete.
       
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")

        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - responseStart

        print ('Calculando tiempos de respuesta')
        print ('Tiempo del Back End: ' + str(backendPerformance) +' ms')
        print ('Tiempo del Front End: ' + str(frontendPerformance)+' ms')

def bookingTest(driver):
    # Instancias del modulo de vuelos
    timingTest(driver)
    myFlightButton = driver.find_element_by_xpath(".//button[contains(.,'flights')]")
    mySearchButton = driver.find_element_by_xpath("//button[@type='button'][contains(.,'Search')]")
    fromAirport = driver.find_element_by_name('from')
    toAirport = driver.find_element_by_name('to')
    myFlightButton.click()
    fromAirport.send_keys('SJO')
    toAirport.send_keys('JFK')
    mySearchButton.click()

    # Instancias del modulo de ofertas 
    timingTest(driver)
    myBookButton = driver.find_element_by_xpath("//strong[contains(.,'USD 187')]")
    myBookButton.click()

    # Instancias del modulo de reserva (Informacion Personal)
    timingTest(driver)
    myFirstName = driver.find_element_by_name('firstname')
    myLastName = driver.find_element_by_name('lastname')
    myEmail = driver.find_element_by_name('email')
    myPhone = driver.find_element_by_name('phone')
    myAddress = driver.find_element_by_name('address')
    myFirstName.send_keys('Chanchito')
    myLastName.send_keys('Feliz')
    myEmail.send_keys('cfeliz@gstp.com')
    myPhone.send_keys('+91 1234-5678')
    myAddress.send_keys('Noida, India')
    
    # Instancias del modulo de reserva (Informacion del pasajero)
    timingTest(driver)
    tNameFirst = driver.find_element_by_name('firstname_1')
    tNameLast = driver.find_element_by_name('lastname_1')
    tNationality = Select(driver.find_element_by_xpath("//select[contains(@class,'form-select form-select nationality')]"))
    tMonthBirth = Select(driver.find_element_by_xpath("//select[contains(@name,'dob_month_1')]"))
    tDayBirth = Select(driver.find_element_by_xpath("//select[contains(@name,'dob_day_1')]"))
    tYearBirth = Select(driver.find_element_by_xpath("//select[contains(@name,'dob_year_1')]"))
    tPassportNo = driver.find_element_by_name('passport_1')
    tPassportIMonth = Select(driver.find_element_by_xpath("//select[contains(@name,'passport_issuance_month_1')]"))
    tPassportIDay = Select(driver.find_element_by_xpath("//select[contains(@name,'passport_issuance_day_1')]"))
    tPassportIYear = Select(driver.find_element_by_xpath("//select[contains(@name,'passport_issuance_year_1')]"))
    tPassportEMonth = Select(driver.find_element_by_xpath("//select[contains(@name,'passport_month_1')]"))
    tPassportEDay = Select(driver.find_element_by_xpath("//select[contains(@name,'passport_day_1')]"))
    tPassportEYear = Select(driver.find_element_by_xpath("//select[contains(@name,'passport_year_1')]"))
    myAgreement = driver.find_element_by_id('agreechb')
    myConfirmButton = driver.find_element_by_xpath("//button[@class='theme-btn book waves-effect'][contains(.,'Confirm Booking')]")
    tNameFirst.send_keys('Chanchito')
    tNameLast.send_keys('Feliz')
    tNationality.select_by_visible_text('India')
    tMonthBirth.select_by_index(12)
    tDayBirth.select_by_index(1)
    tYearBirth.select_by_index(21)
    tPassportNo.send_keys('111222333')
    tPassportIMonth.select_by_index(3)
    tPassportIDay.select_by_index(15)
    tPassportIYear.select_by_index(5)
    tPassportEMonth.select_by_index(6)
    tPassportEDay.select_by_index(21)
    tPassportEYear.select_by_index(2)
    driver.execute_script("arguments[0].click();", myAgreement)
    myConfirmButton.submit()

    # Modulo de confirmacion
    timingTest(driver)
    time.sleep(5)
    returnHome = driver.find_element_by_xpath("//a[@href='https://phptravels.net/'][contains(.,'Home')]")
    returnHome.click()
    timingTest(driver)
    time.sleep(5)

def performanceElementSearch(driver):
    # Revisa el que la pagina posea un elemento (element_present) en un tiempo especifico
    timeout = 5
    while True:
        try:
            element_present = EC.presence_of_element_located((By.ID, 'visa-tab'))
            WebDriverWait(driver, timeout).until(element_present)
            print("Elemento presente")
            break
        except TimeoutException as ex:
            print("No se encontro el elemento " + str(ex))
            break

def performanceData(driver):
    print('Google Chrome Performance data')
    performanceData = driver.execute_script("return window.performance.getEntries();")
    print (performanceData)
       

def main():
    caps = DesiredCapabilities.CHROME
    source = 'https://phptravels.net/' # URL
    PATH = 'C:\PHPTravels-G1\Chrome Driver\chromedriver.exe' # Ubicación del WebDriver
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    driver = webdriver.Chrome(PATH, desired_capabilities=caps)
    driver.implicitly_wait(0.5)
    driver.maximize_window()
    driver.get(source)
    performanceData(driver)
    performanceElementSearch(driver)
    timingTest(driver)
    bookingTest(driver)

warnings.filterwarnings("ignore")
main()