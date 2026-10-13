import sys
from machine_info import get_machine_info
from echo_test import echo_server, echo_client
from time_synchronization import sntp_client
from simple_chat import chat_server, chat_client
from error_management import socket_settings, error_management_test

def main_menu():
    while True:
        print("Menu")
        print("1. Machine Information")
        print("2. Echo Test (Server)")
        print("3. Echo Test (Client)")
        print("4. SNTP Time Synchronization")
        print("5. Socket Settings")
        print("6. Simple Chat (Server)")
        print("7. Simple Chat (Client)")
        print("8. Error Management")
        print("0. Exit")

        choice = input("Select a module to run (0-8, 0 to exit)")

        if choice == '1':
            get_machine_info()
        elif choice == '2':
            echo_server()
        elif choice == '3':
            echo_client()
        elif choice == '4':
            sntp_client()
        elif choice == '5':
            socket_settings()
        elif choice == '6':
            chat_server()
        elif choice == '7':
            chat_client()
        elif choice == '8':
            error_management_test()
        elif choice == '0':
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main_menu()