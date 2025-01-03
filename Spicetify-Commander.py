import os  

def main():
    commands = {
        "1": {"description": "Install Spicetify CLI", "command": "iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 | iex"},
        "2": {"description": "Install Marketplace for Spicetify", "command": "iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-marketplace/main/resources/install.ps1 | iex"},
        "3": {"description": "Apply Settings", "command": "spicetify apply"},
        "4": {"description": "Remove Installed Extensions", "command": "spicetify restore"},
        "5": {"description": "Restore Functionality After Errors", "command": "spicetify backup apply"},
        "6": {"description": "Restore from Backup", "command": "spicetify restore backup"},
        "7": {"description": "Update Spicetify", "command": "spicetify update"},
    }

    while True:
        print("\nAvailable Spicetify Commands:")
        for key, value in commands.items():
            print(f"{key}. {value['description']}")

        choice = input("Select one of the following commands to execute: ").strip()

        if choice in commands:
            command = commands[choice]["command"]
            print(f"Executing command: {command}")
            os.system(f"powershell -Command \"{command}\"")
            break 
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
