class AgentPrompts:
    """Хранилище инструкций для ИИ-агента."""

    ALLOWED_CATEGORIES = ("Work", "Study", "Personal", "Finance")
    UNKNOWN_CATEGORY = "Unsorted"
    CATEGORY_DESCRIPTIONS = {
        "Work": "задачи, отчеты, деловая переписка, банкинг, проекты.",
        "Study": "университет, лекции, программирование, учебные заметки.",
        "Personal": "фитнес, хобби, рецепты, личные планы, покупки.",
        "Finance": "крипто-трейдинг, инвестиции, бюджеты.",
    }

    @classmethod
    def _format_categories(cls) -> str:
        lines = []
        for category in cls.ALLOWED_CATEGORIES:
            description = cls.CATEGORY_DESCRIPTIONS.get(category, "")
            lines.append(f"- {category}: {description}")
        return "\n".join(lines)

    # Главная инструкция для нейросети
    SYSTEM_INSTRUCTION = """
    Ты — эксперт по организации данных и персональный ассистент. 
    Твоя задача: прочитать содержимое текстового файла и определить его категорию.
    
    Используй только следующие категории:
    - Work: задачи, отчеты, деловая переписка, банкинг, проекты.
    - Study: университет, лекции, программирование, учебные заметки.
    - Personal: фитнес, хобби, рецепты, личные планы, покупки.
    - Finance: крипто-трейдинг, инвестиции, бюджеты.

    Важное правило: отвечай ТОЛЬКО ОДНИМ словом (названием категории). 
    Не пиши никаких пояснений.
    """

    @classmethod
    def get_system_instruction(cls) -> str:
        return (
            "Ты — эксперт по организации данных и персональный ассистент.\n"
            "Твоя задача: прочитать содержимое текстового файла и определить его категорию.\n\n"
            "Используй только следующие категории:\n"
            f"{cls._format_categories()}\n\n"
            "Важное правило: отвечай ТОЛЬКО ОДНИМ словом (названием категории).\n"
            "Не пиши никаких пояснений."
        )

    @staticmethod
    def clean_category(raw_response: str) -> str:
        """Очищает ответ ИИ от лишних знаков препинания и пробелов."""
        sanitized = raw_response.replace(".", "").replace("\"", "").strip()

        normalized = {
            "work": "Work",
            "study": "Study",
            "personal": "Personal",
            "finance": "Finance",
        }

        candidate = normalized.get(sanitized.casefold())
        if candidate:
            return candidate
        return AgentPrompts.UNKNOWN_CATEGORY


AgentPrompts.SYSTEM_INSTRUCTION = AgentPrompts.get_system_instruction()
