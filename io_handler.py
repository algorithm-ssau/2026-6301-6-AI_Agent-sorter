import os
import shutil
from pathlib import Path

class IOHandler:
    """Класс для управления файловыми операциями: чтение, поиск и сортировка."""

    def __init__(self, input_path: str, output_path: str):
        self.input_dir = Path(input_path)
        self.output_dir = Path(output_path)
        
        # Автоматически создаем папки при запуске
        self.input_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)

