from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import random
from hashlib import sha256



alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]



app = FastAPI(
    title="NovaFrame Studio API",
    description="Простое API для демонстрации возможностей FastAPI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно указать конкретные адреса
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модель данных для сообщений
class Message(BaseModel):
    sender: str
    content: str
    important: Optional[bool] = False

# Корневой маршрут
@app.get("/")
def read_root():
    return {
        "message": "Добро пожаловать в API студии NovaFrame!",
        "endpoints": [
            "/hello/{name}",
            "/about",
            "/send-message",
            "/status",
            "/getAPI"        
            
            ]
    }

# Персональное приветствие
@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "message": f"Привет, {name}! Мы рады видеть тебя в NovaFrame Studio."
    }


# Получение состояния API
@app.get("/status")
def status():
    return {
        "status": "🟢 В работе",
        "uptime": "24/7",
        "version": "1.0.0"
    }

# Приём текстового сообщения
@app.post("/send-message")
def send_message(message: Message):
    status = "✅ Получено важное сообщение!" if message.important else "📩 Сообщение получено."
    return {
        "from": message.sender,
        "content": message.content,
        "status": status
    }

@app.get("/getAPI")
def getAPI():
    api = f"{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}{alphabet[random.randint(0,61)]}"
    print(f"Пользователю был выдан api: {api}")
    return {
        "API hashed": sha256(api.encode()).hexdigest(),
        "api": f"{api}"
    }
@app.get("/about")  # Без пробела
def about_studio():
    return {
        "studio_name": "NovaFrame Studio",
        "founders": ["Ибрагим Нуруллаев", "Фирдавс Салайдинов"],
        "focus": "Видеопродакшн, цифровой дизайн и мультимедийные проекты"
    }
