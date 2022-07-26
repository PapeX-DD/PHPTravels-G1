# PHPTravels-G1

CONTENIDOS
---------------------

 * Introducción
 * Requerimientos
 * Instalación
 * Configuración
 * Troubleshooting
 
INTRODUCCIÓN
------------

En este proyecto se realiza la planificación y desarrollo de un ambiente de pruebas para una página web. El desarrollo de estas pruebas se realiza mediante la interfaz de programación de aplicaciones Selenium WebDriver, el cual es una estructura que permite la automatización de pruebas mediante interfaces brindadas por los navegadores de internet, los cuales se utilizan para simular un usuario físico que realiza las pruebas en esta página.

REQUERIMIENTOS
------------

Esta instalación requiere de lo siguiente:

* [Python](https://www.python.org/downloads/release/python-3105/)

* [Administrador de paquetes de Python](https://bootstrap.pypa.io/get-pip.py)

* [Selenium 4.2.0](https://pypi.org/project/selenium/)

* [Chrome WebDriver](https://chromedriver.chromium.org/downloads)

INSTALACIÓN
------------
 
 * Instalar Python en la computadora, en este caso se instaló la versión 3.10.5. 
    - Descargue el instalador desde la siguiente página y ejecútelo: 
        https://www.python.org/downloads/release/python-3105/.

 * Instalar el administrador de instalación de paquetes de Python (Pip)
    - Descargue el script desde la siguiente página y guárdelo en una ruta de su preferencia: 
        https://bootstrap.pypa.io/get-pip.py.

    - Abre el Command Promt o CMD en Windows y navegue con el comando cd hacia la ruta en donde habíamos guardado anteriormente el script descargado.

    - Una vez esté en la ruta correspondiente ejecutamos el comando:  py get-pip.py y presionamos enter.  

    - Empezará a descargar los archivos requeridos, usualmente este proceso tarda alrededor de 2 minutos en completarse.


 * Instalación de Selenium 4.2.0
    - En CMD o Command Promt ejecute el comando: pip install -U selenium

    - Comenzará a descargar los archivos o paquetes necesarios, este proceso usualmente tarda al rededor de 2 minutos en completarse.  


 * Descarga del WebDriver:
   - Ingrese al siguiente enlace: https://chromedriver.chromium.org/downloads

   - Seleccionar el archivo que corresponda a la versión del Google Chrome.

   - A continuación nos llevará a un sitio en donde podremos elegir el archivo zip a descargar de acuerdo a la versión de nuestro sistema operativo (Linux, MacOS, Windows).

CONFIGURACIÓN
-------------
 
 * Para iniciar nuestro ambiente de pruebas debemos ejecutarlo desde CMD o Windows Terminal con [python main.py].
 
 * El archivo correspondiente debe estar ubicado en la siguiente ruta: C:\PHPTravels-G1\).

TROUBLESHOOTING
---------------

 * Si al ejecutar el script en el punto de instalación del Pip nos arroja un error que dice "Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut
   from  Settings > Manage App Execution Aliases", realice lo siguiente:

   - Escribir en Inicio de Windows "Manage App Execution Aliases" y abrirlo.

   - Nos llevará a la configuración de Windows en donde debemos identificar el App Installer de Python en la lista y proceder a desactivarlo.

   - Una vez hecho esto cerramos el command promt y lo abrimos de nuevo para luego volver a ejecutar el script.
