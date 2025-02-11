import os
import sys
import pyfiglet
import time
import itertools
import re 
from colorama import init, Fore, Style

init()

def get_console_size():
    return os.get_terminal_size().columns, os.get_terminal_size().lines

def center_text(text):
    width, _ = get_console_size()
    clean_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
    padding = (width - len(clean_text)) // 2
    return ' ' * padding + text + ' ' * (width - len(clean_text) - padding)

def center_cursor_and_text(prompt):
    width, _ = get_console_size()
    clean_prompt = re.sub(r'\x1b\[[0-9;]*m', '', prompt)
    x = (width - len(clean_prompt)) // 2
    sys.stdout.write(f"\r{' ' * x}{prompt}")
    sys.stdout.flush()

def load_figlet_font(font="slant"):
    try:
        return pyfiglet.Figlet(font=font)
    except Exception as e:
        print(f"Ошибка загрузки шрифта: {e}")
        sys.exit(1)

def display_banner(title):
    figlet = load_figlet_font()
    banner = figlet.renderText(title)
    return "\n".join(Fore.GREEN + center_text(line) + Style.RESET_ALL for line in banner.splitlines()) + "\n" * 2

def display_menu(options):
    menu = "\n".join(f"{Fore.YELLOW}{key}{Style.RESET_ALL}. {value['description']}" for key, value in options.items())
    return "\n".join(center_text(line) for line in menu.splitlines())

def show_loading_animation(text="Loading", duration=1):
    end_time = time.time() + duration
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    while time.time() < end_time:
        sys.stdout.write(f"\r{Fore.CYAN}{center_text(f'{text} {next(spinner)}')}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * get_console_size()[0] + "\n\n")
    sys.stdout.flush()

def welcome_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(display_banner("Spicetify Commander"))
    print(center_text(Fore.YELLOW + "Добро пожаловать в Spicetify Commander!" + Style.RESET_ALL))
    print(center_text(Fore.YELLOW + "Welcome to Spicetify Commander!" + Style.RESET_ALL) + "\n")
    show_loading_animation(duration=3)

def execute_command(command):
    print(Fore.YELLOW + center_text(f"Executing: {command}") + Style.RESET_ALL + "\n")
    os.system(f"powershell -Command \"{command}\"")
    print("\n")

def log_action(action):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {action}\n")

def choose_language():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(display_banner("Выбор языка / Language Selection"))
    menu = {"1": {"description": "Русский"}, "2": {"description": "English"}}
    print(display_menu(menu) + "\n")
    
    while True:
        center_cursor_and_text("    Выберите язык / Select language (1/2): ")
        choice = input().strip()
        if choice in ["1", "2"]:
            return choice
        print(Fore.RED + center_text("Некорректный ввод. Попробуйте снова." if choice == "1" else "Invalid input. Try again.") + Style.RESET_ALL + "\n")

def spicetify_menu(language):
    translations = {
        "1": {"ru": "Установка Spicetify CLI", "en": "Install Spicetify CLI"},
        "2": {"ru": "Установка Marketplace", "en": "Install Marketplace"},
        "3": {"ru": "Применение настроек", "en": "Apply Settings"},
        "4": {"ru": "Удаление расширений", "en": "Remove Extensions"},
        "5": {"ru": "Восстановление после ошибок", "en": "Restore Errors"},
        "6": {"ru": "Восстановление из резервной копии", "en": "Restore Backup"},
        "7": {"ru": "Обновление Spicetify", "en": "Update Spicetify"},
        "0": {"ru": "Выход", "en": "Exit"}
    }
    commands = {
        "1": "iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 | iex",
        "2": "iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-marketplace/main/resources/install.ps1 | iex",
        "3": "spicetify apply",
        "4": "spicetify restore",
        "5": "spicetify backup apply",
        "6": "spicetify restore backup",
        "7": "spicetify update",
    }
    lang = "ru" if language == "1" else "en"
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(display_banner("Spicetify ./Commander"))
        menu = {key: {"description": translations[key][lang]} for key in translations}
        print(display_menu(menu) + "\n")
        
        center_cursor_and_text("  Введите ваш выбор: " if lang == "ru" else "  Enter your choice: ")
        choice = input().strip()
        print("\n")
        
        if choice in commands:
            show_loading_animation("Обработка" if lang == "ru" else "Processing", duration=1)
            execute_command(commands[choice])
            log_action(f"Executed: {translations[choice][lang]}")
        elif choice == "0":
            break
        else:
            print(Fore.RED + center_text("Некорректный ввод. Попробуйте снова." if lang == "ru" else "Invalid input. Try again.") + Style.RESET_ALL + "\n")

def main():
    welcome_screen()
    language = choose_language()
    spicetify_menu(language)

if __name__ == "__main__":
    main()