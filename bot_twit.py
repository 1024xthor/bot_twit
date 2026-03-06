# =====================================
# BOT TWITTER / X PARA RENDER
# SIN SELENIUM
# =====================================

import requests
import random
import time
import os

# =====================================
# COOKIES DE SESIÓN
# =====================================

auth_token = os.getenv("AUTH_TOKEN")
ct0 = os.getenv("CT0")

# =====================================
# MENSAJES DEL BOT
# =====================================

mensajes = [

"Visita mi sitio web. Soluciones web accesibles para emprendedores. #web #emprendedores",

"Visit my website. Affordable web solutions for entrepreneurs. #startup #webdev",

"Visitez mon site web. Solutions web abordables pour entrepreneurs. #business #marketing",

"Besuchen Sie meine Website. Weblösungen für Unternehmer. #startup #digital",

"Visite meu site. Soluções web acessíveis para empreendedores. #negocios #web",

"Visita il mio sito web. Soluzioni web economiche per imprenditori. #startup #business"

]

# =====================================
# CABECERAS HTTP
# =====================================

headers = {
"authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAA",
"x-csrf-token": ct0,
"content-type": "application/json"
}

cookies = {
"auth_token": auth_token,
"ct0": ct0
}

# =====================================
# FUNCIÓN PUBLICAR TWEET
# =====================================

def publicar():

    tweet = random.choice(mensajes)

    url = "https://api.twitter.com/1.1/statuses/update.json"

    data = {
        "status": tweet
    }

    r = requests.post(url, headers=headers, cookies=cookies, data=data)

    print("Respuesta:", r.status_code)
    print("Tweet:", tweet)

# =====================================
# BUCLE DEL BOT
# =====================================

while True:

    publicar()

    espera = random.randint(3600,7200)

    print("Esperando", espera, "segundos")

    time.sleep(espera)





