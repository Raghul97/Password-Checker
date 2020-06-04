#https://api.pwnedpasswords.com/range/
import requests
import hashlib
import sys


def hashing_password(password):
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first, last = hashed_password[:5], hashed_password[5:]
    print(first)
    return first, last


def get_data(first):
    url = 'https://api.pwnedpasswords.com/range/'
    response = requests.get(url + first)
    data = response.text.splitlines()
    return data


def checking_password(data, last, password):
    hacked = 0
    for value in data:
        tail, count = value.split(':')
        if tail == last:
            hacked = count
            break
        else:
            hacked = 0
    if hacked:
        print(f"your password '{password}' has been hacked for {hacked} times, Kindly change it ASAP.")
    else:
        print(f"Your password '{password}' has not been hacked, you are good to cointinue")
    return 'done!'


def main(original_password):
    for password in original_password:
        first, last = hashing_password(password)
        data = get_data(first)
        checking_password(data, last, password)

if __name__ == '__main__':
    original_password = sys.argv[1:]
    main(original_password)