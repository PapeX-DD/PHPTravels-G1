from selenium import webdriver



source = 'https://phptravels.net/' #URL
PATH = 'C:\PHPTravels-G1\Chrome Driver\chromedriver.exe' #Ubicación del WebDriver
driver = webdriver.Chrome(PATH)
driver.get(source)


def timingTest():
        #Este calcula dos tiempos o timings.
        #Performance de back-end: desde cuando el usuario empieza la navegación hasta cuando recibe la primera respuesta.
        #Performance del front-end: inicia cuando el usuario recibe la primera respuesta y hasta que la carga del DOM se complete.
       
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")

        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - responseStart

        print ('Calculando tiempos de respuesta')
        print ('Tiempo del Back End: ' + str(backendPerformance) +' ms')
        print ('Tiempo del Front End: ' + str(frontendPerformance)+' ms')

        driver.quit()

timingTest()



