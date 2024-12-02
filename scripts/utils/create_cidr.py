# scripts/utils/create_cidr.py

import os
import requests

def get_public_ip():
    """Fetches the public IP address of the current machine."""
    try:
        response = requests.get("https://api.ipify.org?format=text")
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None

def create_cidr(ip):
    """Formats the public IP in CIDR notation."""
    if not ip:
        print("Invalid IP address provided.")
        return None
    return f"{ip}/32"

def write_to_file(public_ip, cidr):
    """Writes the public IP and CIDR to a file in the utils directory."""
    if not public_ip or not cidr:
        print("No valid data to write to file.")
        return

    utils_dir = os.path.dirname(__file__)
    cidr_file_path = os.path.join(utils_dir, "cidr.txt")
    
    try:
        with open(cidr_file_path, "w") as file:
            file.write("Public IP and CIDR Configuration:\n")
            file.write(f"Public IP: {public_ip}\n")
            file.write(f"CIDR: {cidr}\n")
        print(f"Details written to file: {cidr_file_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")

def main():
    """Main function to create and save public IP and CIDR."""
    print("Fetching public IP address...")
    public_ip = get_public_ip()
    
    if public_ip:
        print(f"Public IP: {public_ip}")
        cidr = create_cidr(public_ip)
        if cidr:
            print(f"Generated CIDR: {cidr}")
            write_to_file(public_ip, cidr)
    else:
        print("Failed to generate details.")

if __name__ == "__main__":
    main()
