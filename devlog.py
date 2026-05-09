# DevLog - Personal Developer Journal
# Author: SAIGANE77

entries = []

def add_entry(text):
    entries.append(text)
    print(f"✅ Entry added: {text}")

def list_entries():
    if not entries:
        print("No entries yet!")
    else:
        for i, entry in enumerate(entries, 1):
            print(f"{i}. {entry}")

def delete_entry(index):
    if index < 1 or index > len(entries):
        print("❌ Invalid entry number!")
    else:
        removed = entries.pop(index - 1)
        print(f"🗑️ Deleted entry: {removed}")

def main():
    print("Welcome to DevLog! 📓 - By SAIGANE77")
    print("Commands: add / list / delete / quit")

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == "add":
            text = input("What did you learn today? ")
            add_entry(text)
        elif command == "list":
            list_entries()
        elif command == "delete":
            list_entries()
            num = int(input("Enter entry number to delete: "))
            delete_entry(num)
        elif command == "quit":
            print("Goodbye! Keep learning! 🚀")
            break
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()