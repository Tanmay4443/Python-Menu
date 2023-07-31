import os
import subprocess

def clear_terminal():
    os.system('clear') 

def print_menu():
    clear_terminal()
    print("===== Main Menu =====")
    print("1. Linux Commands")
    print("2. Docker Commands")
    print("3. Network Tools")
    print("4. System Information")
    print("5. Process Management")
    print("0. Exit")

def run_linux_commands():
    while True:
        clear_terminal()
        print("===== Linux Commands Menu =====")
        print("1. List Files (ls)")
        print("2. Print Working Directory (pwd)")
        print("3. Disk Usage (df)")
        print("4. Show Network Interfaces (ifconfig)")
        print("5. Display System Information (uname -a)")
        print("6. Go Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            subprocess.run(["ls", "-al"])
        elif choice == '2':
            subprocess.run(["pwd"])
        elif choice == '3':
            subprocess.run(["df", "-h"])
        elif choice == '4':
            subprocess.run(["ifconfig"])
        elif choice == '5':
            subprocess.run(["uname", "-a"])
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

def run_docker_commands():
    while True:
        clear_terminal()
        print("===== Docker Commands Menu =====")
        print("1. List Containers")
        print("2. List Images")
        print("3. Start the Container")
        print("4. Stop the Container")
        print("5. Run a Container")
        print("6. Go Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            subprocess.run(["docker", "ps", "-a"])
        elif choice == '2':
            subprocess.run(["docker", "images"])
        elif choice == '3':
            container_name = input("Enter the name of the Container: ")
            subprocess.run(["docker", "start", container_name])
        elif choice == '4':
            stop_name = input("Enter the Container name or ID: ")
            subprocess.run(["docker", "stop", stop_name])
        elif choice == '5':
            container_name = input("Enter the name of the container to run: ")
            container_image = input("Enter the image name with version: ")
            subprocess.run(["docker", "run", "-it", "--name", container_name, container_image])
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
            
        input("Press Enter to continue...")

def run_network_tools():
    while True:
        clear_terminal()
        print("===== Network Tools Menu =====")
        print("1. Ping")
        print("2. Traceroute")
        print("3. Check Internet Connectivity")
        print("4. Go Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            host = input("Enter the host to ping: ")
            subprocess.run(["ping", host])
        elif choice == '2':
            host = input("Enter the host to traceroute: ")
            subprocess.run(["traceroute", host])
        elif choice == '3':
            subprocess.run(["ping", "-c", "3", "8.8.8.8"])  # Google's DNS server
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...")

def display_cpu_info():
    clear_terminal()
    print("===== CPU Information =====")
    subprocess.run(["lscpu"])
    input("Press Enter to continue...")

def display_memory_usage():
    clear_terminal()
    print("===== Memory Usage =====")
    subprocess.run(["free", "-h"])
    input("Press Enter to continue...")

def display_disk_usage():
    clear_terminal()
    print("===== Disk Space Usage =====")
    subprocess.run(["df", "-h"])
    input("Press Enter to continue...")

def run_system_info():
    while True:
        clear_terminal()
        print("===== System Information Menu =====")
        print("1. Display CPU Information")
        print("2. Display Memory Usage")
        print("3. Display Disk Space Usage")
        print("4. Go Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_cpu_info()
        elif choice == '2':
            display_memory_usage()
        elif choice == '3':
            display_disk_usage()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
def run_process_management():
    while True:
        clear_terminal()
        print("===== Process Management Menu =====")
        print("1. List Running Processes (top)")
        print("2. Process Status (ps)")
        print("3. Go Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            subprocess.run(["top"])
        elif choice == '2':
            subprocess.run(["ps", "aux"])
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            run_linux_commands()
        elif choice == '2':
            run_docker_commands()
        elif choice == '3':
            run_network_tools()
        elif choice == '4':
            run_system_info()
        elif choice == '5':
            run_process_management()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
