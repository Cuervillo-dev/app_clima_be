from fastapi import FastAPI
import requests
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_weather_url: str
    default_latitude: float
    default_longitude: float

    class Config:
        env_file = ".env"

settings = Settings()


app = FastAPI(title="API de Clima SRE", version="1.0")

@app.get("/clima")
def obtener_clima():
   
    url = f"{settings.api_weather_url}?latitude={settings.default_latitude}&longitude={settings.default_longitude}&current=temperature_2m"
    
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    temperatura = datos["current"]["temperature_2m"]
    
    return {
        "ubicacion": "Managua",
        "latitud": settings.default_latitude,
        "longitud": settings.default_longitude,
        "temperatura_actual": temperatura,
        "unidad": "°C"
    }