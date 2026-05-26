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
