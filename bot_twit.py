import tweepy
import os
import random
from dotenv import load_dotenv

# Cargamos las 5 variables de los Secrets
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# --- TU COLECCIÓN ORIGINAL DE 7 IDIOMAS ---
mensajes_globales = [
    "Visit my website. Affordable web solutions. #tech",        # Inglés
    "Visita mi sitio web. Soluciones web económicas. #tech",    # Español
    "Visitez mon site web. Solutions web abordables. #tech",    # Francés
    "Visite o meu site. Soluções web acessíveis. #tech",        # Portugués
    "Besuchen Sie meine Website. Günstige Web-Lösungen. #tech", # Alemán
    "Visita il mio sito web. Soluzioni web convenienti. #tech", # Italiano
    "मेरी वेबसाइट पर जाएँ। किफायती वेब समाधान। #tech"           # Hindi (Indio)
]

def publicar_tweet_mundial():
    try:
        # Autenticación v2 para evitar el error 403
        client = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )

        # Elegimos uno de los 7 idiomas y le ponemos un número para que X no lo bloquee
        texto = f"{random.choice(mensajes_globales)} {random.randint(1000, 9999)}"
        
        client.create_tweet(text=texto)
        print(f"✅ ¡ÉXITO GLOBAL! Publicado: {texto}")

    except Exception as e:
        print(f"❌ Error en la transmisión: {e}")

if __name__ == "__main__":
    publicar_tweet_mundial()







