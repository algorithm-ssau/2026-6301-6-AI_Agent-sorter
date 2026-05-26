import time

from brain import GeminiBrain as NvidiaBrain
from io_handler import FileHandler
from schema import AgentPrompts

INPUT_PATH = "./data/input"
OUTPUT_PATH = "./data/output"


def run_agent():
    handler = FileHandler(INPUT_PATH, OUTPUT_PATH)
    brain = NvidiaBrain()
    prompts = AgentPrompts()

    print("--- ИИ-Агент запущен и готов к сортировке ---")

    while True:
        files_to_process = handler.list_files()

        if not files_to_process:
            print("[...] Новых файлов нет. Жду 10 секунд...")
            time.sleep(10)
            continue

        for file_path in files_to_process:
            print(f"[*] Обрабатываю: {file_path.name}")

            content = handler.read_content(file_path)
            if not content:
                continue

            raw_decision = brain.get_decision(prompts.SYSTEM_INSTRUCTION, content)
            category = prompts.clean_category(raw_decision)
            handler.move_to_category(file_path, category)

        print("--- Цикл завершен ---")
        time.sleep(1)


if __name__ == "__main__":
    try:
        run_agent()
    except KeyboardInterrupt:
        print("\n[!] Агент остановлен пользователем.")
