"""
Downloading pictures asyncronical
"""

import os
import asyncio


class PictureSaver:
    def __init__(self):
        self.save_directory = None
        self.statuses = {"test": True}

    def check_save_directory(self) -> bool:
        try:
            inputed_path = input("Директория для сохранения файлов:")
            abs_path = os.path.abspath(inputed_path)
            if not os.access(abs_path, os.W_OK):
                raise Exception
            self.save_directory = abs_path
        except Exception:
            print("Пожалуйста, выбери другую директорию.")
            self.check_save_directory()


async def main():
    pic_saver = PictureSaver()
    pic_saver.check_save_directory()


if __name__ == "__main__":
    asyncio.run(main())
