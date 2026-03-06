# ===============================
# BOT TWITTER / X PARA SERVIDORES
# Compatible con Render
# ===============================

import time
import random
import os

# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# descarga automática del driver
from webdriver_manager.chrome import ChromeDriverManager


# ===============================
# CONFIGURACIÓN DE CHROME
# ===============================

options = webdriver.ChromeOptions()

# modo headless obligatorio en servidores (sin interfaz gráfica)
options.add_argument("--headless=new")

# evita errores de permisos en contenedores
options.add_argument("--no-sandbox")

# evita errores de memoria
options.add_argument("--disable-dev-shm-usage")

# desactiva GPU
options.add_argument("--disable-gpu")

# tamaño de ventana virtual
options.add_argument("--window-size=1920,1080")

# user agent para que el navegador parezca real
options.add_argument(
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
)

# iniciar Chrome en servidores
service = Service(ChromeDriverManager().install())

options.binary_location = "/usr/bin/chromium"

driver = webdriver.Chrome(
    service=service,
    options=options
)


# ===============================
# MENSAJES DEL BOT
# ===============================

mensajes = [

"Visita mi sitio web. Soluciones web accesibles para emprendedores.",
"Visit my website. Affordable web solutions for entrepreneurs.",
"Visitez mon site web. Solutions web abordables pour entrepreneurs.",
"Besuchen Sie meine Website. Weblösungen für Unternehmer.",
"Visite meu site. Soluções web acessíveis para empreendedores.",
"Visita il mio sito web. Soluzioni web economiche per imprenditori."

]


# ===============================
# COOKIES DE SESIÓN (opcional)
# ===============================

# se leen desde variables de entorno de Render
auth_token = os.getenv("AUTH_TOKEN")
ct0 = os.getenv("CT0")


# ===============================
# ABRIR X / TWITTER
# ===============================

print("Abriendo X...")

driver.get("https://x.com")

time.sleep(5)


# ===============================
# CARGAR COOKIES SI EXISTEN
# ===============================

if auth_token and ct0:

    print("Cargando cookies de sesión")

    driver.add_cookie({
        "name": "auth_token",
        "value": auth_token,
        "domain": ".x.com",
        "path": "/"
    })

    driver.add_cookie({
        "name": "ct0",
        "value": ct0,
        "domain": ".x.com",
        "path": "/"
    })

    # recargar página con sesión
    driver.get("https://x.com/home")

    time.sleep(5)


# ===============================
# FUNCIÓN PUBLICAR TWEET
# ===============================

def publicar():

    try:

        tweet = random.choice(mensajes)

        wait = WebDriverWait(driver,20)

        # caja de tweet
        caja = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,'div[data-testid="tweetTextarea_0"]')
            )
        )

        caja.send_keys(tweet)

        time.sleep(2)

        # botón publicar
        boton = driver.find_element(
            By.CSS_SELECTOR,
            'div[data-testid="tweetButtonInline"]'
        )

        boton.click()

        print("Tweet enviado:", tweet)

    except Exception as e:

        print("Error publicando:", e)


# ===============================
# BUCLE DEL BOT
# ===============================

while True:

    publicar()

    # espera entre 1 y 2 horas
    espera = random.randint(3600,7200)

    print("Esperando",espera,"segundos")

    time.sleep(espera)




