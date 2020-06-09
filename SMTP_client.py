#!/usr/bin/python3

# Script to communicate with an SMTP service / server
# Add username from text file support


import socket
import os
from colorama import Fore, Style
path = os.getcwd()

print("++ SMTP Client by iTryZz ++\n")

server = input(f"SMTPY({Fore.RED + path + Style.RESET_ALL}) SMTP server IP: ")
port = 25
command = input(f"SMTPY({Fore.RED + path + Style.RESET_ALL}) SMTP Command: ")

print(f"{server}\n{port}\n{command}\n(I will not catch any of your spelling errors, or incorrect commands)\n")

partial_cmd = []
partial_cmd.append(command)
partial_cmd.append('\r\n')
full_command = ''.join(partial_cmd)

# Init socket and send command
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.send("WhAtCha DoInG?".encode())
    serviceBanner = s.recv(1024).decode('utf-8')
    print("Service Banner: " + serviceBanner)
    s.send(full_command.encode('utf-8'))
    s.close()
except Exception as e:
    print(str(e))
    print(f"Thanks for using {Fore.GREEN}SMTPY")
    exit(1)
else:
    print(f"Thanks for using {Fore.GREEN}SMTPY")