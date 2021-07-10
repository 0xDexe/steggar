#!/usr/bin/env python3

import sys
import argparse
import os.path
from getpass import getpass

from . import lsb

def main():
    banner_print()
    parser = argparse.ArgumentParser(description='OPEN SOURCE TOOL FOR STEGANOGRAHY | github.com/../')
    parser.add_argument('encode_string', help='String to encode', nargs='*')
    parser.add_argument('file_path', help='Path to file')
    parser.add_argument('-p', '--password', help='set password to encrypt or decrypt a hidden file', action='store_true')
    parser.add_argument('-b', '--bits', help='number of bits per byte (default is 2)', nargs='?', default=2, choices=['1', '2', '4'])
    parser.add_argument('-c', '--check', help='check free space of argument files', action='store_true')
    args = parser.parse_args()

    bits = int(args.bits)
    
    if args.check:
        for arg in args.a + [args.b]:
            if os.path.isfile(arg):
                lsb.HostElement(arg).print_free_space(bits)
        return

    password = filename = None   

    host = lsb.HostElement(args.file_path)

    if args.a:
        args.encode_string = args.encode_string[0]
        
        if os.path.isfile(args.encode_string):
            filename = args.encode_string
            with open(filename, 'rb') as myfile:
                message = myfile.read()
        else:
            message = args.encode_string.encode('utf-8')

        if args.password:
            while 1:
                password = getpass('Enter password :')
                password_2 = getpass('Verify password :')
                if password == password_2:
                    ##verified 
                    break
                ##do elif
 
        host.insert_message(message, bits, filename, password)
        host.save()
    else:
       if args.password:
            password = getpass('Enter password :')
       host.read_message(password)

if __name__== "__main__":
    main()

def banner_print():
    banner = """

    .d8888b. 88888888888 8888888888 .d8888b.   .d8888b.         d8888 8888888b.  
    d88P  Y88b    888     888       d88P  Y88b d88P  Y88b       d88888 888   Y88b 
    Y88b.         888     888       888    888 888    888      d88P888 888    888 
     "Y888b.      888     8888888   888        888            d88P 888 888   d88P 
        "Y88b.    888     888       888  88888 888  88888    d88P  888 8888888P"  
          "888    888     888       888    888 888    888   d88P   888 888 T88b   
    Y88b  d88P    888     888       Y88b  d88P Y88b  d88P  d8888888888 888  T88b  
     "Y8888P"     888     8888888888 "Y8888P88  "Y8888P88 d88P     888 888   T88b 


    """
    print("\033[92m {}\033[00m" .format(banner))