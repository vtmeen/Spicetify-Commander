import os

def main():
    commands = {
        "1": {"description": "Установка Spicetify CLI", "command": "iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 | iex"},
        "2": {"description": "Установка Marketplace для Spicetify", "command": "iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-marketplace/main/resources/install.ps1 | iex"},
        "3": {"description": "Применение настроек", "command": "spicetify apply"},
        "4": {"description": "Удаление установленных расширений", "command": "spicetify restore"},
        "5": {"description": "Восстановление работы при сбоях", "command": "spicetify backup apply"},
        "6": {"description": "Восстановить из бэкапа", "command": "spicetify restore backup"},
        "7": {"description": "Обновление Spicetify", "command": "spicetify update"},
    }

    while True:
        print("\nДоступные команды Spicetify:")
        for key, value in commands.items():
            print(f"{key}. {value['description']}")

        choice = input("Выберите одну из следующих команд для выполнения: ").strip()

        if choice in commands:
            command = commands[choice]["command"]
            print(f"Выполняется команда: {command}")
            os.system(f"powershell -Command \"{command}\"")
            break  # Добавлено break для выхода из цикла после выполнения команды
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()
