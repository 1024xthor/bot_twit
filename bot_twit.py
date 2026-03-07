import os
import random
import tweepy
import time
from dotenv import load_dotenv

# 1. Cargamos las variables del archivo .env (Local) o Secrets (GitHub)
load_dotenv()

# 2. Configuración de las 4 llaves que tienes en tu escritorio
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# 3. Listas de mensajes multilingües
mensajes = [
    "Visita mi sitio web. Soluciones web accesibles.", # Español
    "Visit my website. Affordable web solutions.",     # Inglés
    "Besuchen Sie meine Website. Günstige Webseiten.", # Alemán
    "Visitez mon site. Solutions web abordables.",    # Francés
    "Visite meu site. Soluções web acessíveis.",      # Portugués
    "Visita il mio sito web. Soluzioni economiche.",   # Italiano
    "मेरी वेबसाइट देखें। किफायती वेब समाधान।"          # Hindi
]

extras = [
    "Crece tu negocio online.", 
    "Start your digital business today.", 
    "Impulsa tu emprendimiento.",
    "Soluciones profesionales."
]

hashtags = ["#webdev", "#webdesign", "#startup", "#entrepreneur", "#coding", "#tech"]

def publicar_tweet():
    try:
        # Forzamos API v2 (la única que el plan Free tolera un poco)
        client = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )

        texto_tweet = (
            f"{random.choice(mensajes)} {random.choice(extras)} "
            f"{random.choice(hashtags)} {random.randint(1000, 9999)}"
        )

        client.create_tweet(text=texto_tweet)
        print(f"✅ ¡EN LA NUBE SÍ! Tweet enviado: {texto_tweet}")

    except Exception as e:
        print(f"❌ Error en GitHub: {e}")

if __name__ == "__main__":
    # Si lo corres en VS Code, puedes probar un ciclo, 
    # pero en GitHub el tiempo lo manda el archivo YAML (cada hora).
    publicar_tweet()







