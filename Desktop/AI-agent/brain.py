import os
import google.generativeai as genai
from dotenv import load_dotenv

class GeminiBrain:
    """Класс для работы напрямую с Google Gemini API."""

    def __init__(self):
        load_dotenv()
        # Берем ключ из .env
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            print("[!] Ошибка: GEMINI_API_KEY не найден в .env")
            return

        # Твой код конфигурации
        genai.configure(api_key=api_key)
        
        # Твоя модель
        self.model_name = os.getenv("MODEL_NAME", "gemini-2.0-flash")
        self.model = genai.GenerativeModel(self.model_name)
        print(f"[Brain] Интеллект Gemini запущен на модели: {self.model_name}")

    def get_decision(self, system_prompt: str, file_content: str) -> str:
        """Отправляет запрос и возвращает категорию."""
        try:
            # Формируем запрос как в твоем примере
            full_query = f"{system_prompt}\n\nТекст для классификации:\n{file_content}"
            
            response = self.model.generate_content(full_query)
            
            if response and response.text:
                return response.text.strip()
            return "Unsorted"
            
        except Exception as e:
            print(f"[!] Ошибка Gemini: {e}")
            return "Unsorted"