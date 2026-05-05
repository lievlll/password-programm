from services.storage_service import StorageService
from services.password_service import PasswordService
from controllers.password_controller import PasswordController

storage = StorageService()
password_service = PasswordService()
controller = PasswordController(storage)

while True:
    print("\n=== Password Manager ===")
    print("1. Add")
    print("2. Generate password")
    print("3. Show all")
    print("4. Delete")
    print("5. Exit")

    choice = input("> ")

    if choice == "1":
        service = input("Service: ")
        username = input("Username: ")
        password = input("Password: ")
        controller.add(service, username, password)

    elif choice == "2":
        try:
            length = int(input("Length: "))
            pwd = password_service.generate(length)
            print("Password:", pwd)
        except:
            print("Error!")

    elif choice == "3":
        records = controller.show_all()
        for i in range(len(records)):
            r = records[i]
            print(i, r.service, r.username, r.password)

    elif choice == "4":
        try:
            index = int(input("Index: "))
            controller.delete(index)
        except:
            print("Error!")

    elif choice == "5":
        controller.save()
        break
