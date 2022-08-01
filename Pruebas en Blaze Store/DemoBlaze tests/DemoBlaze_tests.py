from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import warnings
from threading import Thread
from time import sleep, perf_counter

def timingTest(driver):
    # Este calcula los tiempos o timings del performance del back-end y del front-end.
    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    backendPerformance = responseStart - navigationStart
    frontendPerformance = domComplete - responseStart

    print ('Calculando tiempos de respuesta')
    print ('Tiempo del Back End: ' + str(backendPerformance) +' ms')
    print ('Tiempo del Front End: ' + str(frontendPerformance)+' ms')

def logInTest(driver):
    # Instancias del modulo de sing up
    timingTest(driver)
    myLogInButton = driver.find_element(By.XPATH, "(//a[@class='nav-link'])[5]")
    myLogInButton.click()
    time.sleep(1)

    # Instancias del sign up (Informacion Personal)
    timingTest(driver)
    myUserName = driver.find_element(By.XPATH, "((//label[text()='Username:'])[2]/following::input)[1]")
    myPassword = driver.find_element(By.XPATH, "(//label[text()='Password:'])[2]/following::input")
    time.sleep(1)
    myUserName.click()
    myUserName.send_keys("Chanchito")
    myPassword.click()
    myPassword.send_keys('12345')
    time.sleep(1)    
    myLogInButton = driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]")
    myLogInButton.click()

    # Modulo de confirmacion
    timingTest(driver)
    time.sleep(5)
    logOut = driver.find_element(By.XPATH, "(//a[@href='#'])[4]")
    logOut.click()
    timingTest(driver)
    time.sleep(5)

def performanceElementSearch(driver):
    # Revisa el que la pagina posea un elemento (element_present) en un tiempo especifico
    timeout = 5
    while True:
        try:
            element_present = EC.presence_of_element_located((By.XPATH, "(//a[@id='itemc'])[1]"))
            WebDriverWait(driver, timeout).until(element_present)
            print("Elemento presente")
            break
        except TimeoutException as ex:
            print("No se encontro el elemento " + str(ex))
            break

def performanceData(driver):
    # Imprime los logs de performance de Google Chrome.
    print('Google Chrome Performance data')
    performanceData = driver.execute_script("return window.performance.getEntries();")
    print (performanceData)


def multipleUsersTest(driver):
    # Realiza el test de multiples usuarios
    timingTest(driver)
    phoneLink = driver.find_element(By.XPATH,"(//a[@class='hrefch'])[1]")
    phoneLink.click()
    time.sleep(1)
    addtToCartBtn = driver.find_element(By.XPATH,"//div[contains(@class,'col-sm-12 col-md-6')]//a[1]")
    addtToCartBtn.click()
    cartbtn = driver.find_element(By.XPATH,"(//a[@class='nav-link'])[4]")
    cartbtn.click()

    #Modulo de confirmacion
    timingTest(driver)
    time.sleep(5)
    returnHome = driver.find_element(By.XPATH,"(//a[@class='nav-link'])[1]")
    returnHome.click()
    timingTest(driver)
    time.sleep(5)

def threadtasks(driver):
    # Crea un hilo de procesamiento, para procesos paralelos.
    threads = []
    for n in range (1,6):
        new_thread = Thread(target=multipleUsersTest(driver))
        threads.append(new_thread)
        new_thread.start()
    for t in threads:
        t.join()
    print ("Test done with 5 users")
    

       

def main():
    # Maneja los distintos modulos de pruebas.
    caps = DesiredCapabilities.CHROME
    source = 'https://www.demoblaze.com/index.html' 
    PATH = 'C:\Program Files (x86)\chromedriver.exe' 
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    driver = webdriver.Chrome(PATH, desired_capabilities=caps)
    driver.implicitly_wait(0.5)
    driver.maximize_window()
    driver.get(source)
    #performanceData(driver)
    #performanceElementSearch(driver)
    timingTest(driver)
    #logInTest(driver)
    #multipleUsersTest(driver)
    #threadtasks(driver)
    driver.close()

warnings.filterwarnings("ignore")
main()

