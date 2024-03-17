import os
import shutil
import sys
from pathlib import Path


def copy_files(src, dest):
    # Роблю перевірку, що директорія дійсно існує
    if not src.exists():
        print(f"Error: The source directory {src} does not exist.")
        return

    # Створення директорії куди будуть копіюватись файли
    dest.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        if item.is_dir():
            copy_files(item, dest)
        elif item.is_file():
            subdir = dest / item.suffix.lstrip('.')
            subdir.mkdir(exist_ok=True)
            shutil.copy(item, subdir)


def main():
    args = sys.argv[1:]

    # Вказую папку відки скопіювати і куди вставити скопійовані файли
    src_path = Path(args[0]) if args else Path('.')
    dest_path = Path(args[1]) if len(args) > 1 else Path('dist')

    # Копіювання файлів
    copy_files(src_path, dest_path)
    print(f"Files copied from {src_path} to {dest_path}.")


if __name__ == "__main__":
    main()


# Запуск функції copy_files з консолі:
# python3 task1.py <src_path> <dest_path/dist>
# якщо <dest_path/dist> не передавати, то папка dist створиться в корні папки проекту.