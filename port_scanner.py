
import socket
import ipaddress

def scan_ports(host, ports):
    print(f"\nScanning {host}...\n")

    for port in ports:
        try:
            with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            ) as sock:

                sock.settimeout(1)
                result = sock.connect_ex((host, port))

                if result == 0:
                    print(f"[OPEN] Port {port}")
                else:
                    print(f"[CLOSED/FILTERED] Port {port}")

        except OSError as error:
            print(f"[ERROR] Port {port}: {error}")


def main():
    print("=== Local TCP Port Scanner ===")

    host = input(
        "Enter a loopback IP (default 127.0.0.1): "
    ).strip() or "127.0.0.1"

    try:
        address = ipaddress.ip_address(host)

        if not address.is_loopback or address.version != 4:
            print("Only local IPv4 loopback addresses are allowed.")
            return

    except ValueError:
        print("Invalid IP address.")
        return

    ports = [21, 22, 25, 53, 80, 443, 3306, 8080]

    scan_ports(host, ports)


if __name__ == "__main__":
    main()
