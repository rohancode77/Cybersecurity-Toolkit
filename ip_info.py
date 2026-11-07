
import socket

def get_ip_info():
    hostname = input("Enter a domain name (e.g. google.com): ")

    try:
        ip_address = socket.gethostbyname(hostname)

        print("\n--- IP Information ---")
        print("Hostname:", hostname)
        print("IP Address:", ip_address)

    except socket.gaierror:
        print("Unable to resolve hostname.")
        print("Please check the domain name or internet connection.")


if __name__ == "__main__":
    get_ip_info()
