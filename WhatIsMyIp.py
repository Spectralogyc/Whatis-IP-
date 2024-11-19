import tkinter as tk
import requests
import socket

# Function to get the public IP
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.exceptions.RequestException:
        return "Unable to get public IP"

# Function to get the local IP
def get_local_ip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip
    except socket.error:
        return "Unable to get local IP"

# Function to display the IPs in the graphical interface
def show_ips():
    local_ip = get_local_ip()
    public_ip = get_public_ip()

    # Update the text in the interface
    label.config(text=f"Local IP: {local_ip}\nPublic IP: {public_ip}")

# Creating the main window
root = tk.Tk()
root.title("IP Checker")
root.geometry("300x150")

# Label to display the IPs
label = tk.Label(root, text="", font=("Arial", 12), justify="left")
label.pack(pady=20)

# Button to update the IPs
button = tk.Button(root, text="Check IPs", command=show_ips)
button.pack(pady=10)

# Start the graphical interface
root.mainloop()
