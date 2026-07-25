import os
import random
import tweepy
import time
from dotenv import load_dotenv

# 1. Cargamos las variables del archivo .env (Local) o Secrets (GitHub)
load_dotenv()

# 2. Configuración de las 4 llaves de tu API de X (Twitter)
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# 3. Mensajes en Español, Inglés, Francés y Portugués (Brasil)
mensajes = [
    # Español
    "Alcanza tus metas con SayanFitness. Disponible en Web y Android:",
    "Transforma tu estilo de vida con SayanFitness. Visita nuestra web y descarga la App:",
    "Entrena al máximo nivel con SayanFitness. Encuéntranos en la web y Play Store:",
    
    # Inglés
    "Reach your fitness goals with SayanFitness. Available on Web and Android:",
    "Transform your training with SayanFitness. Check our website and get the app:",
    "Boost your workouts with SayanFitness! Available on Web and Google Play Store:",
    
    # Francés
    "Atteignez vos objectifs avec SayanFitness. Disponible sur Web et Android:",
    "Transformez votre entraînement avec SayanFitness. Visitez notre site et téléchargez l'application:",
    
    # Portugués (Brasil)
    "Alcance seus objetivos com o SayanFitness. Disponível na Web e Android:",
    "Transforme seus treinos com o SayanFitness. Acesse nosso site e baixe o app:"
]

# Enlaces e información destacada
enlaces = [
    "🌐 sayanfitness.com | 📱 App SayanFitness en Google Play Store",
    "Visítanos en sayanfitness.com o busca SayanFitness en Play Store.",
    "🌐 sayanfitness.com — ¡Descarga la app SayanFitness en tu Android!",
    "Sitio web: sayanfitness.com / Android App: SayanFitness"
]

hashtags = ["#SayanFitness", "#FitnessApp", "#Fitness", "#Workout", "#Gym", "#AndroidApp", "#Health"]

def publicar_tweet():
    try:
        # Autenticación con API v2
        client = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )

        texto_tweet = (
            f"{random.choice(mensajes)}\n\n"
            f"{random.choice(enlaces)}\n\n"
            f"{random.choice(hashtags)} {random.choice(hashtags)} #{random.randint(1000, 9999)}"
        )

        client.create_tweet(text=texto_tweet)
        print(f"✅ Tweet enviado con éxito:\n{texto_tweet}")

    except Exception as e:
        print(f"❌ Error al enviar el tweet: {e}")

if __name__ == "__main__":
    publicar_tweet()