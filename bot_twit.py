# =========================================
# BOT TWITTER PARA RENDER FREE
# =========================================

import requests
import random
import time
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler


# =========================================
# SERVIDOR WEB FALSO (para Render)
# =========================================

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"bot running")

def start_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=start_server).start()


# =========================================
# COOKIES DE SESION
# =========================================

auth_token = os.getenv("AUTH_TOKEN")
ct0 = os.getenv("CT0")


# =========================================
# MENSAJES DEL BOT
# =========================================

mensajes = [

"Visita mi sitio web. Soluciones web accesibles para emprendedores. #web #emprendedores",

"Visit my website. Affordable web solutions for entrepreneurs. #startup #webdev",

"Visitez mon site web. Solutions web abordables pour entrepreneurs. #business #marketing",

"Besuchen Sie meine Website. Weblösungen für Unternehmer. #startup #digital",

"Visite meu site. Soluções web acessíveis para empreendedores. #negocios #web",

"Visita il mio sito web. Soluzioni web economiche per imprenditori. #startup #business"

]


# =========================================
# HEADERS PARA X
# =========================================

headers = {
"authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAA",
"x-csrf-token": ct0,
"content-type": "application/json"
}

cookies = {
"auth_token": auth_token,
"ct0": ct0
}


# =========================================
# PUBLICAR TWEET
# =========================================

def publicar():

    tweet = random.choice(mensajes)

    url = "https://api.twitter.com/1.1/statuses/update.json"

    data = {
        "status": tweet
    }

    r = requests.post(url, headers=headers, cookies=cookies, data=data)

    print("Status:", r.status_code)
    print("Tweet:", tweet)


# =========================================
# LOOP DEL BOT
# =========================================

while True:

    publicar()

    espera = random.randint(3600,7200)

    print("Esperando", espera, "segundos")

    time.sleep(espera)





