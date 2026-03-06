# ==============================
# BOT TWITTER / X AUTOMÁTICO
# Compatible con Render
# ==============================

import time
import random

# librerías selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# webdriver manager descarga el driver automáticamente
from webdriver_manager.chrome import ChromeDriverManager


# ==============================
# CONFIGURACIÓN DE CHROME
# ==============================

options = webdriver.ChromeOptions()

# modo headless necesario para servidores (sin interfaz gráfica)
options.add_argument("--headless")

# evita errores en servidores linux
options.add_argument("--no-sandbox")

# evita errores de memoria
options.add_argument("--disable-dev-shm-usage")

# desactiva gpu
options.add_argument("--disable-gpu")

# tamaño de ventana
options.add_argument("--window-size=1920,1080")


# iniciar navegador
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


# ==============================
# MENSAJES DEL BOT
# ==============================

mensajes = [

"Visita mi sitio web. Soluciones web accesibles para emprendedores.",
"Visit my website. Affordable web solutions for entrepreneurs.",
"Visitez mon site web. Solutions web abordables pour entrepreneurs.",
"Besuchen Sie meine Website. Weblösungen für Unternehmer.",
"Visite meu site. Soluções web acessíveis para empreendedores.",
"Visita il mio sito web. Soluzioni web economiche per imprenditori."

]


# ==============================
# ABRIR TWITTER
# ==============================

print("Abriendo X / Twitter...")

driver.get("https://x.com/home")

# esperar que cargue la página
time.sleep(10)


# ==============================
# FUNCIÓN PUBLICAR TWEET
# ==============================

def publicar():

    try:

        # elegir mensaje aleatorio
        tweet = random.choice(mensajes)

        wait = WebDriverWait(driver,20)

        # buscar caja de tweet
        caja = wait.until(

            EC.presence_of_element_located(
                (By.CSS_SELECTOR,'div[data-testid="tweetTextarea_0"]')
            )

        )

        # escribir tweet
        caja.send_keys(tweet)

        # esperar un poco
        time.sleep(2)

        # botón publicar
        boton = driver.find_element(By.CSS_SELECTOR,'div[data-testid="tweetButtonInline"]')

        boton.click()

        print("Tweet enviado:", tweet)

    except Exception as e:

        print("Error al publicar:", e)


# ==============================
# BUCLE DEL BOT
# ==============================

while True:

    publicar()

    # tiempo aleatorio entre tweets
    espera = random.randint(3600,7200)  # entre 1 y 2 horas

    print("Esperando",espera,"segundos para el próximo tweet")

    time.sleep(espera)
    


