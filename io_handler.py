import os import shutil from pathlib import Path


class IOHandler:
    """Класс для управления файловыми операциями: чтение, поиск и сортировка."""

    def __init__(self, input_path: str, output_path: str):
        self.input_dir = Path(input_path)
        self.output_dir = Path(output_path)
        
        # Автоматически создаем папки при запуске
        self.input_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def list_files(self):
        """Находит все текстовые файлы в папке input."""
        return [f for f in self.input_dir.iterdir() if f.is_file() and f.suffix in ['.txt', '.md']]

    def read_content(self, file_path: Path) -> str:
        """Читает содержимое файла. Возвращает пустую строку при ошибке."""
        try:
            # Читаем первые 2000 символов, чтобы не перегружать контекст ИИ
            content = file_path.read_text(encoding='utf-8')
            return content[:2000] 
        except Exception as e:
            print(f"[!] Ошибка чтения {file_path.name}: {e}")
            return ""

    def move_to_category(self, file_path: Path, category: str):
        """Перемещает файл в папку с названием категории."""
        # Очищаем название категории от лишних символов
        clean_category = category.strip().capitalize()
        target_path = self.output_dir / clean_category
        
        target_path.mkdir(exist_ok=True)
        
        try:
            shutil.move(str(file_path), str(target_path / file_path.name))
            print(f"[✓] Файл {file_path.name} отправлен в папку: {clean_category}")
        except Exception as e:
            print(f"[X] Не удалось переместить {file_path.name}: {e}")

