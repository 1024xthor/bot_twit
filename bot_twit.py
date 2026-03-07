import os
import random
import tweepy

# CONFIGURACIÓN DE LLAVES (GitHub las pondrá aquí)
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# MENSAJES
mensajes = [
    "Visita mi sitio web. Soluciones web accesibles para emprendedores.",
    "Visit my website. Affordable web solutions for entrepreneurs.",
    "Besuchen Sie meine Website. Günstige Webseiten für Unternehmer.",
    "Visitez mon site. Solutions web abordables pour entrepreneurs.",
    "Visite meu site. Soluções web acessíveis para empreendedores.",
    "Visita il mio sito web. Soluzioni web economiche per imprenditori.",
    "मेरी वेबसाइट देखें। उद्यमियों के लिए किफायती वेब समाधान।"
]

extras = ["Crece tu negocio online.", "Start your digital business today.", "Impulsa tu emprendimiento."]
hashtags = ["#webdev", "#webdesign", "#startup", "#entrepreneur", "#digitalbusiness"]

def publicar():
    try:
        # Autenticación con la API v2 de Twitter
        client = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )

        # Generar tweet aleatorio
        tweet = (
            random.choice(mensajes) + " " +
            random.choice(extras) + " " +
            random.choice(hashtags) + " " +
            str(random.randint(1000, 9999))
        )

        # Publicar
        client.create_tweet(text=tweet)
        print(f"✅ Tweet publicado: {tweet}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    publicar()






