# BOT TWITTER MULTIIDIOMA

import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# CONFIGURACIÓN CHROME
options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")  
# abre el navegador maximizado

options.add_argument("--disable-blink-features=AutomationControlled")  
# oculta que el navegador está controlado por selenium

options.add_experimental_option("excludeSwitches", ["enable-automation"])  
# quita aviso de automatización

options.add_experimental_option("useAutomationExtension", False)  
# desactiva extensión automática de selenium

options.add_argument(r"user-data-dir=C:\botchrome")  
# usa tu sesión real de chrome para no loguearte cada vez


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver,20)
# espera inteligente hasta 20 segundos para encontrar elementos


# MENSAJES PRINCIPALES
mensajes = [

# Español
"Visita mi sitio web. Soluciones web accesibles para emprendedores.",

# Inglés
"Visit my website. Affordable web solutions for entrepreneurs.",

# Alemán
"Besuchen Sie meine Website. Günstige Webseiten für Unternehmer.",

# Francés
"Visitez mon site. Solutions web abordables pour entrepreneurs.",

# Portugués
"Visite meu site. Soluções web acessíveis para empreendedores.",
"Crie sua presença online hoje. Soluções web acessíveis para empreendedores.",

# Italiano
"Visita il mio sito web. Soluzioni web economiche per imprenditori.",

# Hindi (Indio)
"मेरी वेबसाइट देखें। उद्यमियों के लिए किफायती वेब समाधान।",
"अपना ऑनलाइन व्यवसाय शुरू करें। किफायती वेबसाइट समाधान।"
]


# FRASES EXTRA
extras = [

"Crece tu negocio online.",
"Start your digital business today.",
"Modern websites for modern entrepreneurs.",
"Tu negocio merece presencia digital.",
"Build your brand online.",
"Impulsa tu emprendimiento."
]


# HASHTAGS
hashtags = [

"#webdev",
"#webdesign",
"#startup",
"#entrepreneur",
"#digitalbusiness",
"#programming",
"#tech",
"#coding",
"#marketing",
"#onlinebusiness"
]


# FUNCIÓN PUBLICAR
def publicar():

    # genera tweet aleatorio para evitar duplicados
    tweet = (
        random.choice(mensajes) + " " +
        random.choice(extras) + " " +
        random.choice(hashtags) + " " +
        random.choice(hashtags) + " " +
        str(random.randint(1000,9999))
    )

    print("Abriendo X...")

    driver.get("https://x.com/home")

    time.sleep(7)  
    # espera a que cargue completamente


    print("Buscando caja del tweet...")

    caja = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'div[data-testid="tweetTextarea_0"]'))
    )

    driver.execute_script("arguments[0].focus();", caja)
    # enfoca la caja sin usar click (evita errores)

    time.sleep(1)

    caja.send_keys(tweet)
    # escribe el tweet


    print("Buscando botón publicar...")

    boton = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'button[data-testid="tweetButtonInline"]'))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", boton)
    # mueve la pantalla hasta el botón

    driver.execute_script("arguments[0].click();", boton)
    # click forzado con javascript


    print("✅ Tweet publicado:", tweet)



# LOOP INFINITO
print("Bot iniciado")

while True:

    publicar()

    espera = random.randint(90,180)  # entre 1.5 y 3 horas

    print("Esperando", round(espera/60), "minutos")

    time.sleep(espera * 60)  # convierte minutos a segundos
    #espera = 2  # minutos (modo prueba)

    #print("Esperando", espera, "minutos")

    #time.sleep(espera * 60)  # convierte minutos a segundos
    

