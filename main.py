import os
from dotenv import load_dotenv
load_dotenv()

print("\n🚀 Автономный ИИ AAA-AI-DFH запущен!")
print("Он готов сам отвечать на вопросы.\n")

while True:
    user_input = input("Ты: ")
    if user_input.lower() in ['выход', 'exit', 'quit']:
        print("Пока! ИИ остановлен.")
        break
    
    # Здесь будет вызов настоящей модели
    print("ИИ: ", "Я автономный ИИ и сам отвечаю. Твой запрос: ", user_input)
    print("(В продакшене здесь будет Grok/OpenAI/Ollama)\n")