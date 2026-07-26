import os
import random
import tweepy
import time
from dotenv import load_dotenv

# 1. Cargamos las variables
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

mensajes = [
    "Alcanza tus metas con SayanFitness. Disponible en Web y Android:",
    "Transforma tu estilo de vida con SayanFitness. Visita nuestra web y descarga la App:",
    "Entrena al máximo nivel con SayanFitness. Encuéntranos en la web y Play Store:",
    "Reach your fitness goals with SayanFitness. Available on Web and Android:",
    "Transform your training with SayanFitness. Check our website and get the app:",
    "Boost your workouts with SayanFitness! Available on Web and Google Play Store:",
    "Atteignez vos objectifs avec SayanFitness. Disponible sur Web et Android:",
    "Transformez votre entraînement avec SayanFitness. Visitez notre site et téléchargez l'application:",
    "Alcance seus objetivos com o SayanFitness. Disponível na Web e Android:",
    "Transforme seus treinos com o SayanFitness. Acesse nosso site e baixe o app:"
]

enlaces = [
    "🌐 sayanfitness.com | 📱 App SayanFitness en Google Play Store",
    "Visítanos en sayanfitness.com o busca SayanFitness en Play Store.",
    "🌐 sayanfitness.com — ¡Descarga la app SayanFitness en tu Android!",
    "Sitio web: sayanfitness.com / Android App: SayanFitness"
]

hashtags = ["#SayanFitness", "#FitnessApp", "#Fitness", "#Workout", "#Gym", "#AndroidApp", "#Health"]

def publicar_tweet():
    try:
        # Autenticación con API v1.1 (OAuth 1.0a - 100% GRATIS)
        auth = tweepy.OAuth1UserHandler(
            API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
        )
        api = tweepy.API(auth)

        texto_tweet = (
            f"{random.choice(mensajes)}\n\n"
            f"{random.choice(enlaces)}\n\n"
            f"{random.choice(hashtags)} {random.choice(hashtags)} #{random.randint(1000, 9999)}"
        )

        # Método de publicación gratuito
        api.update_status(status=texto_tweet)
        print(f"✅ Tweet enviado con éxito:\n{texto_tweet}")

    except Exception as e:
        print(f"❌ Error al enviar el tweet: {e}")

if __name__ == "__main__":
    publicar_tweet()
